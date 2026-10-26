import { describe, expect, it } from "vitest";
import type { Question } from "@/data/gha";
import {
	createQuiz,
	isCorrect,
	quizReducer,
	scoreSteps,
	shuffle,
	visibleOptions,
} from "@/lib/quiz";

const single: Question = {
	id: "single",
	section: "fact",
	text: "Pick B",
	options: ["A", "B", "C"],
	steps: [{ prompt: "Pick one", answer: 1, why: "" }],
	source: "",
};

const pair: Question = {
	id: "pair",
	section: "scenario",
	text: "Most then least",
	options: ["A", "B", "C", "D"],
	steps: [
		{ prompt: "Most", answer: 1, why: "" },
		{ prompt: "Least", answer: 3, why: "" },
	],
	source: "",
};

describe("quizReducer", () => {
	it("records a pick and locks the step", () => {
		let state = createQuiz(["single"]);
		state = quizReducer(state, { type: "pick", question: single, option: 0 });
		state = quizReducer(state, { type: "pick", question: single, option: 1 });
		expect(state.picks.single).toEqual([0]);
	});

	it("hides step 1's answer from step 2", () => {
		expect(visibleOptions(pair, 0)).toEqual([0, 1, 2, 3]);
		expect(visibleOptions(pair, 1)).toEqual([0, 2, 3]);

		let state = createQuiz(["pair"]);
		state = quizReducer(state, { type: "pick", question: pair, option: 0 });
		const rejected = quizReducer(state, {
			type: "pick",
			question: pair,
			option: 1,
		});
		expect(rejected).toBe(state);

		state = quizReducer(state, { type: "pick", question: pair, option: 3 });
		expect(state.picks.pair).toEqual([0, 3]);
		expect(isCorrect(pair, state.picks.pair)).toBe(false);
	});

	it("clamps navigation between the first question and the summary", () => {
		let state = createQuiz(["single", "pair"]);
		state = quizReducer(state, { type: "go", delta: -1 });
		expect(state.index).toBe(0);
		state = quizReducer(state, { type: "go", delta: 5 });
		expect(state.index).toBe(2);
	});

	it("restart clears only the restarted questions", () => {
		let state = createQuiz(["single", "pair"]);
		state = quizReducer(state, { type: "pick", question: single, option: 1 });
		state = quizReducer(state, { type: "pick", question: pair, option: 1 });
		state = quizReducer(state, { type: "restart", order: ["pair"] });
		expect(state).toEqual({
			order: ["pair"],
			index: 0,
			picks: { single: [1] },
		});
	});
});

describe("scoreSteps", () => {
	it("scores each step separately", () => {
		expect(scoreSteps([single, pair], { single: [1], pair: [1, 0] })).toEqual({
			correct: 2,
			answered: 3,
			total: 3,
		});
	});
});

describe("shuffle", () => {
	it("keeps every item and does not mutate the input", () => {
		const input = [1, 2, 3, 4, 5];
		const out = shuffle(input, () => 0);
		expect(out).toHaveLength(5);
		expect([...out].sort()).toEqual(input);
		expect(input).toEqual([1, 2, 3, 4, 5]);
	});
});
