import type { Attempt, Grade, Problem } from "@/lib/types";

const MINUTE = 60_000;
const HOUR = 60 * MINUTE;
export const DAY = 24 * HOUR;

/** Leitner boxes: a card in box `b` comes back after `INTERVALS[b]`. */
export const INTERVALS = [
	10 * MINUTE,
	DAY,
	3 * DAY,
	7 * DAY,
	16 * DAY,
	35 * DAY,
	90 * DAY,
];
const TOP_BOX = INTERVALS.length - 1;
const SKIP_DELAY = HOUR;
/** "Visit less often" jumps two boxes and doubles the wait. */
const LESS_FACTOR = 2;

export type CardList = "again" | "less";

export interface CardState {
	box: number;
	due: number;
	list: CardList | null;
	reviews: number;
	lastAt: number;
	lastScore: number | null;
	lastGrade: Grade;
}

const UNSEEN: CardState = {
	box: 0,
	due: 0,
	list: null,
	reviews: 0,
	lastAt: 0,
	lastScore: null,
	lastGrade: "skip",
};

export function applyAttempt(
	state: CardState | undefined,
	attempt: Attempt,
): CardState {
	const prev = state ?? UNSEEN;
	const { at, grade } = attempt;
	// A skip only defers the card: it keeps its box, list and score, and never comes back sooner.
	if (grade === "skip") {
		const due = Math.max(prev.due, at + SKIP_DELAY);
		return { ...prev, lastAt: at, lastGrade: grade, due };
	}
	const box =
		grade === "again"
			? 0
			: Math.min(prev.box + (grade === "less" ? 2 : 1), TOP_BOX);
	const wait = INTERVALS[box] * (grade === "less" ? LESS_FACTOR : 1);
	return {
		box,
		due: at + wait,
		list: grade === "good" ? null : grade,
		reviews: prev.reviews + 1,
		lastAt: at,
		lastScore: attempt.score,
		lastGrade: grade,
	};
}

/** Replays the attempt log (oldest first) into the current state of every touched card. */
export function cardStates(attempts: Attempt[]): Map<string, CardState> {
	const states = new Map<string, CardState>();
	for (const attempt of attempts) {
		states.set(attempt.slug, applyAttempt(states.get(attempt.slug), attempt));
	}
	return states;
}

export const STUDY_SETS = {
	smart: "Due and new",
	due: "Due for review",
	new: "Not seen yet",
	again: "Visit again",
	less: "Visit less often",
	missed: "Missed topics",
	skipped: "Skipped",
	all: "All problems",
} as const;
export type StudySet = keyof typeof STUDY_SETS;

export type CardStatus = "new" | "due" | "later";

/** A skipped card that was never graded goes back to "new" once its skip delay ends. */
export function cardStatus(
	state: CardState | undefined,
	now: number,
): CardStatus {
	if (state && state.due > now) return "later";
	return !state || state.reviews === 0 ? "new" : "due";
}

const MISSED_BELOW = 0.5;

export function inSet(
	set: StudySet,
	state: CardState | undefined,
	now: number,
): boolean {
	const status = cardStatus(state, now);
	switch (set) {
		case "smart":
			return status !== "later";
		case "due":
			return status === "due";
		case "new":
			return status === "new";
		case "again":
		case "less":
			return state?.list === set;
		case "missed":
			return state?.lastScore != null && state.lastScore < MISSED_BELOW;
		case "skipped":
			return state?.lastGrade === "skip";
		case "all":
			return true;
	}
}

/**
 * Queue order: due reviews (visit-again first, then oldest due), then new problems by
 * Google frequency rank, then cards not yet due (soonest first).
 */
function priority(
	problem: Problem,
	state: CardState | undefined,
	now: number,
): number[] {
	switch (cardStatus(state, now)) {
		case "due":
			return [0, state?.list === "again" ? 0 : 1, state?.due ?? 0];
		case "new":
			return [1, 0, problem.rank];
		case "later":
			return [2, 0, state?.due ?? 0];
	}
}

function compare(a: number[], b: number[]) {
	for (let i = 0; i < a.length; i++) {
		if (a[i] !== b[i]) return a[i] - b[i];
	}
	return 0;
}

export interface QueueFilter {
	set: StudySet;
	topic?: string;
	difficulty?: Problem["difficulty"];
}

export function matchesFilter(
	problem: Problem,
	state: CardState | undefined,
	filter: QueueFilter,
	now: number,
): boolean {
	return (
		(!filter.topic || problem.topics.includes(filter.topic)) &&
		(!filter.difficulty || problem.difficulty === filter.difficulty) &&
		inSet(filter.set, state, now)
	);
}

/** The problems in a study set, in the order they will be shown. */
export function queue(
	problems: Problem[],
	states: Map<string, CardState>,
	filter: QueueFilter,
	now: number,
): Problem[] {
	return problems
		.filter((p) => matchesFilter(p, states.get(p.slug), filter, now))
		.map((p) => ({ p, key: priority(p, states.get(p.slug), now) }))
		.sort((a, b) => compare(a.key, b.key))
		.map(({ p }) => p);
}
