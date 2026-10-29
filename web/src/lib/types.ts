export const DIFFICULTIES = ["Easy", "Medium", "Hard"] as const;
export type Difficulty = (typeof DIFFICULTIES)[number];

/** One row of data/problems.json (built by `uv run google ingest`). */
export interface Problem {
	rank: number;
	id: number;
	slug: string;
	title: string;
	difficulty: Difficulty;
	frequency: number;
	url: string;
	topics: string[];
	premium: boolean;
	/** Sanitized HTML statement; null for premium problems. */
	description: string | null;
}

/** One entry of data/approaches.json, written in ASD-STE100 Simplified Technical English. */
export interface Approach {
	insight: string;
	steps: string[];
	time: string;
	space: string;
	/** Nudges shown one at a time before the answer; they never name the technique. */
	hints: string[];
}

/**
 * What the learner did with a card. "again" adds it to the visit-again list, "less" to the
 * visit-less-often list, "good" clears both, and "skip" defers it without a grade.
 */
export const GRADES = ["again", "good", "less", "skip"] as const;
export type Grade = (typeof GRADES)[number];

export interface Attempt {
	slug: string;
	at: number;
	grade: Grade;
	guessed: string[];
	/** Topic-guess F1 in [0, 1]; null for skips. */
	score: number | null;
	/** How many hints the learner opened before answering. */
	hints: number;
}
