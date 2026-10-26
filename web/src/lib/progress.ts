import { z } from "zod";
import { type Question, SECTION_IDS, type Section } from "@/data/gha";

/** Attempts kept per question; older ones are dropped. */
export const MAX_ATTEMPTS = 20;

const attemptSchema = z.object({
	at: z.number(),
	correct: z.boolean(),
});

export const progressSchema = z.object({
	version: z.literal(1),
	attempts: z.record(z.string(), z.array(attemptSchema)),
});

export type Attempt = z.infer<typeof attemptSchema>;
export type ProgressData = z.infer<typeof progressSchema>;

export const EMPTY_PROGRESS: ProgressData = { version: 1, attempts: {} };

/** Parse stored progress, falling back to empty on anything malformed or from another version. */
export function parseProgress(raw: unknown): ProgressData {
	const result = progressSchema.safeParse(raw);
	return result.success ? result.data : EMPTY_PROGRESS;
}

export function recordAttempt(
	data: ProgressData,
	questionId: string,
	attempt: Attempt,
): ProgressData {
	const previous = data.attempts[questionId] ?? [];
	return {
		...data,
		attempts: {
			...data.attempts,
			[questionId]: [...previous, attempt].slice(-MAX_ATTEMPTS),
		},
	};
}

export type Mastery = "new" | "needs-work" | "learning" | "mastered";

export const MASTERY_LABEL: Record<Mastery, string> = {
	new: "New",
	"needs-work": "Needs work",
	learning: "Getting there",
	mastered: "Mastered",
};

/**
 * Mastered = the last two attempts were right. A wrong last attempt always means
 * "needs work", so one slip pulls a question back into review.
 */
export function masteryOf(attempts: readonly Attempt[] | undefined): Mastery {
	if (!attempts?.length) return "new";
	const last = attempts.at(-1);
	if (!last?.correct) return "needs-work";
	const previous = attempts.at(-2);
	return previous?.correct ? "mastered" : "learning";
}

export interface ProgressSummary {
	total: number;
	seen: number;
	mastered: number;
	needsWork: number;
	/** Share of all recorded attempts that were correct, 0–1; null before any attempt. */
	accuracy: number | null;
}

export function summarize(
	questions: readonly Question[],
	data: ProgressData,
): ProgressSummary {
	let seen = 0;
	let mastered = 0;
	let needsWork = 0;
	let attempts = 0;
	let correct = 0;
	for (const q of questions) {
		const history = data.attempts[q.id];
		const mastery = masteryOf(history);
		if (mastery !== "new") seen++;
		if (mastery === "mastered") mastered++;
		if (mastery === "needs-work") needsWork++;
		attempts += history?.length ?? 0;
		correct += history?.filter((a) => a.correct).length ?? 0;
	}
	return {
		total: questions.length,
		seen,
		mastered,
		needsWork,
		accuracy: attempts ? correct / attempts : null,
	};
}

export function summarizeBySection(
	questions: readonly Question[],
	data: ProgressData,
): Record<Section, ProgressSummary> {
	return Object.fromEntries(
		SECTION_IDS.map((s) => [
			s,
			summarize(
				questions.filter((q) => q.section === s),
				data,
			),
		]),
	) as Record<Section, ProgressSummary>;
}
