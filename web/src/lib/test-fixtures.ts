import type { Attempt, Grade, Problem } from "@/lib/types";

export const T0 = Date.UTC(2026, 0, 1);

export function problem(rank: number, extra: Partial<Problem> = {}): Problem {
	return {
		rank,
		id: rank,
		slug: `p${rank}`,
		title: `Problem ${rank}`,
		difficulty: "Medium",
		frequency: 10,
		url: "",
		topics: ["Array"],
		premium: false,
		description: null,
		...extra,
	};
}

export function attempt(
	slug: string,
	grade: Grade,
	at = T0,
	score: number | null = grade === "skip" ? null : 1,
): Attempt {
	return { slug, at, grade, guessed: [], score, hints: 0 };
}
