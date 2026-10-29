import { readFileSync } from "node:fs";
import { describe, expect, it } from "vitest";
import { buildIndex, search } from "@/lib/search";
import type { Problem } from "@/lib/types";

const { problems } = JSON.parse(
	readFileSync(new URL("../../../data/problems.json", import.meta.url), "utf8"),
) as { problems: Problem[] };
const index = buildIndex(problems);
const top = (query: string) => search(index, query, 5)[0];

describe("search over the real problem list", () => {
	it.each([
		"1",
		"#1",
		"lc 1",
		"LC1",
		"two sum",
		"Two Sum",
	])("finds Two Sum by number or title: %s", (query) =>
		expect(top(query)?.slug).toBe("two-sum"));

	it("matches title prefixes, acronyms and typos", () => {
		expect(top("lru")?.slug).toBe("lru-cache");
		expect(top("lis")?.slug).toBe("longest-increasing-subsequence");
		expect(top("trapping rian water")?.slug).toBe("trapping-rain-water");
		expect(top("median sorted")?.slug).toBe("median-of-two-sorted-arrays");
	});

	it("needs every word, and searches topics, difficulty and statements", () => {
		const hits = search(index, "hard dynamic", 50);
		expect(hits.length).toBeGreaterThan(5);
		for (const hit of hits) {
			const problem = problems.find((p) => p.slug === hit.slug);
			expect(problem?.difficulty).toBe("Hard");
			expect(problem?.topics).toContain("Dynamic Programming");
		}
		const statement = search(index, "reverse order linked", 50).find(
			(h) => h.slug === "add-two-numbers",
		);
		expect(statement?.field).toBe("statement");
		expect(statement?.snippet).toMatch(/reverse order/i);
	});
});
