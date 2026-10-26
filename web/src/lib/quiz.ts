import type { Question } from "@/data/gha";

/** One run through a list of questions. Picks hold one option index per answered step. */
export interface QuizState {
	order: string[];
	index: number;
	picks: Record<string, number[]>;
}

export type QuizAction =
	| { type: "pick"; question: Question; option: number }
	| { type: "go"; delta: number }
	| { type: "restart"; order: string[] };

export function createQuiz(order: string[]): QuizState {
	return { order, index: 0, picks: {} };
}

/** The option a step hides: step 2 of a Most/Least pair can't reuse step 1's answer. */
export function hiddenOption(question: Question, step: number): number | null {
	return step === 1 ? question.steps[0].answer : null;
}

/** Option indices shown for a step, in display order. */
export function visibleOptions(question: Question, step: number): number[] {
	const hidden = hiddenOption(question, step);
	return question.options.map((_, i) => i).filter((i) => i !== hidden);
}

export function isComplete(
	question: Question,
	picks: readonly number[],
): boolean {
	return picks.length === question.steps.length;
}

/** True only when every step was answered correctly. */
export function isCorrect(
	question: Question,
	picks: readonly number[],
): boolean {
	return (
		isComplete(question, picks) &&
		question.steps.every((s, i) => picks[i] === s.answer)
	);
}

export function quizReducer(state: QuizState, action: QuizAction): QuizState {
	switch (action.type) {
		case "pick": {
			const { question, option } = action;
			const picks = state.picks[question.id] ?? [];
			if (isComplete(question, picks)) return state;
			if (!visibleOptions(question, picks.length).includes(option))
				return state;
			return {
				...state,
				picks: { ...state.picks, [question.id]: [...picks, option] },
			};
		}
		case "go": {
			// index === order.length is the summary screen.
			const index = Math.min(
				Math.max(state.index + action.delta, 0),
				state.order.length,
			);
			return index === state.index ? state : { ...state, index };
		}
		case "restart": {
			const picks = { ...state.picks };
			for (const id of action.order) delete picks[id];
			return { order: action.order, index: 0, picks };
		}
	}
}

export interface Score {
	correct: number;
	answered: number;
	total: number;
}

/** Step-level score across the questions in a run. */
export function scoreSteps(
	questions: readonly Question[],
	picks: QuizState["picks"],
): Score {
	let correct = 0;
	let answered = 0;
	let total = 0;
	for (const q of questions) {
		const p = picks[q.id] ?? [];
		total += q.steps.length;
		answered += p.length;
		correct += q.steps.filter((s, i) => p[i] === s.answer).length;
	}
	return { correct, answered, total };
}

export function shuffle<T>(
	items: readonly T[],
	random: () => number = Math.random,
): T[] {
	const out = [...items];
	for (let i = out.length - 1; i > 0; i--) {
		const j = Math.floor(random() * (i + 1));
		[out[i], out[j]] = [out[j], out[i]];
	}
	return out;
}
