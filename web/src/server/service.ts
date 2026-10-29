import {
	type CardList,
	type CardState,
	type CardStatus,
	cardStates,
	cardStatus,
	queue,
} from "@/lib/scheduler";
import type { AttemptInput, StudySearch } from "@/lib/schemas";
import { scoreTopics } from "@/lib/scorer";
import { type SearchHit, search } from "@/lib/search";
import type { Approach, Problem } from "@/lib/types";
import { getContent } from "@/server/content";
import {
	allAttempts,
	dailyScores,
	deleteAttempts,
	insertAttempt,
} from "@/server/db";
import { currentReport, invalidateReport } from "@/server/scorer";

/**
 * Everything the app can do, as plain functions. Server functions (UI) and /api routes
 * (HTTP) are thin wrappers around these.
 */

export class NotFoundError extends Error {}

export interface StudyCard {
	problem: Problem;
	approach: Approach | null;
	state: CardState | null;
}

export interface StudyDeck {
	card: StudyCard | null;
	/** Cards left in the chosen set, including this one. */
	remaining: number;
	/** Every topic, most common first, for the guess picker. */
	topics: string[];
}

function problemOf(slug: string): Problem {
	const problem = getContent().bySlug.get(slug);
	if (!problem) throw new NotFoundError(`Unknown problem: ${slug}`);
	return problem;
}

function cardFor(problem: Problem, state: CardState | undefined): StudyCard {
	return {
		problem,
		approach: getContent().approaches[problem.slug] ?? null,
		state: state ?? null,
	};
}

export function getCard(slug: string): StudyCard {
	return cardFor(problemOf(slug), cardStates(allAttempts()).get(slug));
}

/** The pinned `slug` when it exists, else the next card in the study set. */
export function getDeck(filter: StudySearch): StudyDeck {
	const { problems, bySlug, topics } = getContent();
	const states = cardStates(allAttempts());
	const remaining = queue(problems, states, filter, Date.now());
	const pinned = filter.slug ? bySlug.get(filter.slug) : undefined;
	const problem = pinned ?? remaining[0];
	return {
		card: problem ? cardFor(problem, states.get(problem.slug)) : null,
		remaining: remaining.length,
		topics,
	};
}

/** Stores one validated answer and returns its topic score (null for a skip). */
export function recordAttempt(data: AttemptInput): { score: number | null } {
	const problem = problemOf(data.slug);
	const skip = data.grade === "skip";
	const score = skip ? null : scoreTopics(data.guessed, problem.topics).score;
	insertAttempt({
		slug: data.slug,
		grade: data.grade,
		guessed: skip ? [] : data.guessed,
		hints: data.hints,
		score,
		at: Date.now(),
	});
	invalidateReport();
	return { score };
}

/** Clears one problem's history, or everything when no slug is given. */
export function resetProgress(slug?: string) {
	if (slug) problemOf(slug);
	deleteAttempts(slug);
	invalidateReport();
}

export interface ProblemRow
	extends Pick<
		Problem,
		"rank" | "id" | "slug" | "title" | "difficulty" | "frequency" | "premium"
	> {
	status: CardStatus;
	list: CardList | null;
	reviews: number;
	lastScore: number | null;
	lastAt: number | null;
	due: number | null;
}

/** Every problem with its progress. Topics stay off so browsing does not spoil guesses. */
export function listProblems(): ProblemRow[] {
	const states = cardStates(allAttempts());
	const now = Date.now();
	return getContent().problems.map((p) => {
		const state = states.get(p.slug);
		return {
			rank: p.rank,
			id: p.id,
			slug: p.slug,
			title: p.title,
			difficulty: p.difficulty,
			frequency: p.frequency,
			premium: p.premium,
			status: cardStatus(state, now),
			list: state?.list ?? null,
			reviews: state?.reviews ?? 0,
			lastScore: state?.lastScore ?? null,
			lastAt: state?.lastAt ?? null,
			due: state?.due ?? null,
		};
	});
}

export function searchProblems(q: string, limit?: number): SearchHit[] {
	return search(getContent().searchIndex, q, limit);
}

export function getReadiness(): number {
	return currentReport().readiness;
}

export function getReport() {
	return { report: currentReport(), history: dailyScores() };
}
