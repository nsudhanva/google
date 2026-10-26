import { describe, expect, it } from "vitest";
import { QUESTIONS } from "@/data/gha";
import {
	EMPTY_PROGRESS,
	MAX_ATTEMPTS,
	masteryOf,
	parseProgress,
	recordAttempt,
	summarize,
} from "@/lib/progress";

const right = { at: 1, correct: true };
const wrong = { at: 1, correct: false };

describe("masteryOf", () => {
	it.each([
		[[], "new"],
		[[wrong], "needs-work"],
		[[right], "learning"],
		[[wrong, right], "learning"],
		[[right, right], "mastered"],
		[[right, right, wrong], "needs-work"],
	] as const)("%j is %s", (attempts, expected) => {
		expect(masteryOf(attempts)).toBe(expected);
	});
});

describe("recordAttempt", () => {
	it("appends without mutating and caps history", () => {
		let data = EMPTY_PROGRESS;
		for (let i = 0; i < MAX_ATTEMPTS + 5; i++) {
			data = recordAttempt(data, "q", { at: i, correct: true });
		}
		expect(data.attempts.q).toHaveLength(MAX_ATTEMPTS);
		expect(data.attempts.q[0].at).toBe(5);
		expect(EMPTY_PROGRESS.attempts).toEqual({});
	});
});

describe("parseProgress", () => {
	it("falls back to empty on malformed data", () => {
		expect(parseProgress(null)).toBe(EMPTY_PROGRESS);
		expect(parseProgress({ version: 2, attempts: {} })).toBe(EMPTY_PROGRESS);
		expect(parseProgress({ version: 1, attempts: { q: [{ at: "x" }] } })).toBe(
			EMPTY_PROGRESS,
		);
	});

	it("keeps valid data", () => {
		const data = { version: 1, attempts: { q: [right] } };
		expect(parseProgress(data)).toEqual(data);
	});
});

describe("summarize", () => {
	it("counts mastery and accuracy", () => {
		const [a, b] = QUESTIONS;
		let data = recordAttempt(EMPTY_PROGRESS, a.id, right);
		data = recordAttempt(data, a.id, right);
		data = recordAttempt(data, b.id, wrong);
		expect(summarize([a, b], data)).toEqual({
			total: 2,
			seen: 2,
			mastered: 1,
			needsWork: 1,
			accuracy: 2 / 3,
		});
	});
});

describe("question bank", () => {
	it("has unique ids and valid answers", () => {
		const ids = new Set(QUESTIONS.map((q) => q.id));
		expect(ids.size).toBe(QUESTIONS.length);
		for (const q of QUESTIONS) {
			for (const [i, step] of q.steps.entries()) {
				expect(step.answer, q.id).toBeGreaterThanOrEqual(0);
				expect(step.answer, q.id).toBeLessThan(q.options.length);
				if (i === 1) expect(step.answer, q.id).not.toBe(q.steps[0].answer);
			}
		}
	});
});
