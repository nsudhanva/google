import { describe, expect, it } from "vitest";
import { DAY } from "@/lib/scheduler";
import { scoreReport, scoreTopics } from "@/lib/scorer";
import { attempt, problem, T0 } from "@/lib/test-fixtures";

const problems = [
	problem(1, { frequency: 90, topics: ["Array", "Graph"] }),
	problem(2, { frequency: 10, difficulty: "Easy" }),
];

describe("scorer", () => {
	it("scores a topic guess with F1", () => {
		expect(scoreTopics(["Array", "Graph"], ["Array", "Hash Table"])).toEqual({
			hits: ["Array"],
			missed: ["Hash Table"],
			extra: ["Graph"],
			score: 0.5,
		});
	});

	it("weights readiness by frequency, discounts hints, and decays with time", () => {
		const frequent = scoreReport(problems, [attempt("p1", "less")], T0);
		expect(frequent.readiness).toBeCloseTo(0.9);
		expect(frequent.coverage).toBe(0.5);
		const hinted = scoreReport(
			problems,
			[{ ...attempt("p1", "less"), hints: 1 }],
			T0,
		);
		expect(hinted.readiness).toBeLessThan(frequent.readiness);
		const later = scoreReport(problems, [attempt("p1", "less")], T0 + 30 * DAY);
		expect(later.readiness).toBeLessThan(frequent.readiness);
	});

	it("counts streaks, lists and the weakest topics", () => {
		const report = scoreReport(
			problems,
			[
				attempt("p2", "skip", T0 - DAY),
				{ ...attempt("p1", "again"), guessed: ["Array"], score: 0.67 },
			],
			T0,
		);
		expect(report).toMatchObject({
			graded: 1,
			streakDays: 2,
			// The day-old skip is past its delay, so it counts as new again.
			counts: { again: 1, new: 1 },
		});
		expect(report.topics.map((t) => [t.topic, t.recall])).toEqual([
			["Graph", 0],
			["Array", 1],
		]);
	});
});
