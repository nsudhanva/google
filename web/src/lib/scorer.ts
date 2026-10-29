import {
	type CardState,
	cardStates,
	cardStatus,
	DAY,
	INTERVALS,
} from "@/lib/scheduler";
import {
	type Attempt,
	DIFFICULTIES,
	type Difficulty,
	type Grade,
	type Problem,
} from "@/lib/types";

export interface TopicResult {
	hits: string[];
	missed: string[];
	extra: string[];
	/** F1 of the guess against the listed topics. */
	score: number;
}

export function scoreTopics(guessed: string[], actual: string[]): TopicResult {
	const truth = new Set(actual);
	const guess = new Set(guessed);
	const hits = actual.filter((t) => guess.has(t));
	const missed = actual.filter((t) => !guess.has(t));
	const extra = guessed.filter((t) => !truth.has(t));
	const total = guess.size + truth.size;
	return { hits, missed, extra, score: total ? (2 * hits.length) / total : 0 };
}

/**
 * How well a graded attempt went: half topic recall (each hint opened costs a quarter of
 * it), half the learner's own grade.
 */
const GRADE_VALUE: Record<Exclude<Grade, "skip">, number> = {
	again: 0,
	good: 0.8,
	less: 1,
};
const HINT_DISCOUNT = 0.75;
const RECENT_ATTEMPTS = 50;

function quality(attempt: Attempt): number | null {
	if (attempt.grade === "skip") return null;
	const recall = (attempt.score ?? 0) * HINT_DISCOUNT ** attempt.hints;
	return 0.5 * recall + 0.5 * GRADE_VALUE[attempt.grade];
}

/**
 * Memory fades between reviews: at the card's own interval, retention is ~70%.
 * Half-life is twice the box interval, never less than a day.
 */
function retention(state: CardState, now: number): number {
	const halfLife = Math.max(2 * INTERVALS[state.box], DAY);
	return 0.5 ** (Math.max(0, now - state.lastAt) / halfLife);
}

export interface ScoreReport {
	computedAt: number;
	/** Frequency-weighted mastery over the whole list, 0..1. */
	readiness: number;
	/** Share of problems graded at least once. */
	coverage: number;
	/** Mean topic score over the last 50 graded attempts. */
	accuracy: number | null;
	graded: number;
	streakDays: number;
	counts: { due: number; new: number; again: number; less: number };
	byDifficulty: {
		difficulty: Difficulty;
		mastery: number;
		seen: number;
		total: number;
	}[];
	/** Recall per topic: how often you named it when it applied. Weakest first. */
	topics: { topic: string; recall: number; seen: number }[];
}

function mean(values: number[]): number | null {
	return values.length
		? values.reduce((a, b) => a + b, 0) / values.length
		: null;
}

/** Calendar day in the server's time zone (set TZ), such as "2026-10-28". */
export function dayKey(at: number) {
	const d = new Date(at);
	const pad = (n: number) => String(n).padStart(2, "0");
	return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;
}

function streak(attempts: Attempt[], now: number): number {
	const days = new Set(attempts.map((a) => dayKey(a.at)));
	// Step back by calendar day, not by 24 hours, so daylight-saving days count once.
	const day = new Date(now);
	// Today without practice yet does not break a streak that ran through yesterday.
	if (!days.has(dayKey(day.getTime()))) day.setDate(day.getDate() - 1);
	let count = 0;
	while (days.has(dayKey(day.getTime()))) {
		count++;
		day.setDate(day.getDate() - 1);
	}
	return count;
}

function masteries(
	attempts: Attempt[],
	states: Map<string, CardState>,
	now: number,
): Map<string, number> {
	// Exponential moving average of attempt quality, latest attempt weighted most.
	const averages = new Map<string, number>();
	for (const attempt of attempts) {
		const q = quality(attempt);
		if (q === null) continue;
		const prev = averages.get(attempt.slug);
		averages.set(attempt.slug, prev === undefined ? q : (prev + q) / 2);
	}
	const result = new Map<string, number>();
	for (const [slug, average] of averages) {
		const state = states.get(slug);
		if (state) result.set(slug, average * retention(state, now));
	}
	return result;
}

function topicRecall(problems: Problem[], graded: Attempt[]) {
	const topicsOf = new Map(problems.map((p) => [p.slug, p.topics]));
	const tally = new Map<string, { hit: number; seen: number }>();
	for (const attempt of graded) {
		const guessed = new Set(attempt.guessed);
		for (const topic of topicsOf.get(attempt.slug) ?? []) {
			const entry = tally.get(topic) ?? { hit: 0, seen: 0 };
			entry.seen++;
			if (guessed.has(topic)) entry.hit++;
			tally.set(topic, entry);
		}
	}
	return [...tally]
		.map(([topic, { hit, seen }]) => ({ topic, recall: hit / seen, seen }))
		.sort((a, b) => a.recall - b.recall || b.seen - a.seen);
}

/** Attempts must be oldest first. */
export function scoreReport(
	problems: Problem[],
	attempts: Attempt[],
	now: number,
): ScoreReport {
	const states = cardStates(attempts);
	const mastery = masteries(attempts, states, now);
	const graded = attempts.filter((a) => a.grade !== "skip");
	const weight = problems.reduce((sum, p) => sum + p.frequency, 0);

	const counts = { due: 0, new: 0, again: 0, less: 0 };
	for (const p of problems) {
		const state = states.get(p.slug);
		const status = cardStatus(state, now);
		if (status === "due" || status === "new") counts[status]++;
		if (state?.list) counts[state.list]++;
	}

	return {
		computedAt: now,
		readiness: weight
			? problems.reduce(
					(sum, p) => sum + p.frequency * (mastery.get(p.slug) ?? 0),
					0,
				) / weight
			: 0,
		coverage: problems.length ? mastery.size / problems.length : 0,
		accuracy: mean(graded.slice(-RECENT_ATTEMPTS).map((a) => a.score ?? 0)),
		graded: graded.length,
		streakDays: streak(attempts, now),
		counts,
		byDifficulty: DIFFICULTIES.map((difficulty) => {
			const group = problems.filter((p) => p.difficulty === difficulty);
			return {
				difficulty,
				mastery: mean(group.map((p) => mastery.get(p.slug) ?? 0)) ?? 0,
				seen: group.filter((p) => mastery.has(p.slug)).length,
				total: group.length,
			};
		}),
		topics: topicRecall(problems, graded),
	};
}
