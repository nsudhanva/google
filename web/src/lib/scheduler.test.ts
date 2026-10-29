import { describe, expect, it } from "vitest";
import { cardStates, DAY, INTERVALS, queue } from "@/lib/scheduler";
import { attempt, problem, T0 } from "@/lib/test-fixtures";

describe("scheduler", () => {
	it("schedules each grade and keeps lists", () => {
		const states = cardStates([
			attempt("good", "good"),
			attempt("again", "good"),
			attempt("again", "again", T0 + DAY),
			attempt("less", "less"),
			attempt("skip", "skip"),
		]);
		expect(states.get("good")).toMatchObject({ box: 1, list: null });
		expect(states.get("good")?.due).toBe(T0 + INTERVALS[1]);
		expect(states.get("again")).toMatchObject({ box: 0, list: "again" });
		expect(states.get("less")).toMatchObject({ box: 2, list: "less" });
		expect(states.get("less")?.due).toBe(T0 + 2 * INTERVALS[2]);
		expect(states.get("skip")).toMatchObject({ reviews: 0, lastGrade: "skip" });
		// Skipping a card that is due much later never brings it back sooner.
		const later = cardStates([
			attempt("x", "less"),
			attempt("x", "skip", T0 + 1),
		]);
		expect(later.get("x")?.due).toBe(T0 + 2 * INTERVALS[2]);
	});

	it("orders due reviews (visit-again first), then new by rank", () => {
		const problems = [problem(1), problem(2), problem(3), problem(4)];
		const states = cardStates([
			attempt("p3", "good"),
			attempt("p4", "again"),
			attempt("p2", "skip"),
		]);
		const at = (t: number) =>
			queue(problems, states, { set: "smart" }, t).map((p) => p.slug);
		expect(at(T0 + 1)).toEqual(["p1"]);
		expect(at(T0 + 2 * DAY)).toEqual(["p4", "p3", "p1", "p2"]);
	});

	it("filters sets by list, topic, difficulty and missed topics", () => {
		const problems = [
			problem(1, { topics: ["Graph"], difficulty: "Hard" }),
			problem(2, { topics: ["Graph"] }),
			problem(3),
		];
		const states = cardStates([
			attempt("p1", "less", T0, 0.2),
			attempt("p2", "less", T0, 0.9),
			attempt("p3", "less"),
		]);
		const slugs = (filter: Parameters<typeof queue>[2]) =>
			queue(problems, states, filter, T0).map((p) => p.slug);
		expect(slugs({ set: "less", topic: "Graph", difficulty: "Hard" })).toEqual([
			"p1",
		]);
		expect(slugs({ set: "missed" })).toEqual(["p1"]);
	});

	it("limits a period to the problems asked in it, in that period's order", () => {
		const problems = [
			problem(1),
			problem(2, {
				asked: {
					"6m": { rank: 2, frequency: 9 },
					"30d": { rank: 2, frequency: 50 },
				},
			}),
			problem(3, {
				asked: {
					"6m": { rank: 3, frequency: 8 },
					"30d": { rank: 1, frequency: 90 },
				},
			}),
		];
		const order = queue(
			problems,
			new Map(),
			{ set: "smart", period: "30d" },
			T0,
		);
		expect(order.map((p) => p.slug)).toEqual(["p3", "p2"]);
	});
});
