import { useCallback, useMemo, useReducer } from "react";
import type { Question } from "@/data/gha";
import { progressStore } from "@/lib/progress-store";
import {
	createQuiz,
	isComplete,
	isCorrect,
	quizReducer,
	scoreSteps,
	shuffle as shuffled,
} from "@/lib/quiz";

/** Drives one practice run over `questions` and records each finished question. */
export function useQuiz(questions: readonly Question[]) {
	const byId = useMemo(
		() => new Map(questions.map((q) => [q.id, q])),
		[questions],
	);
	const [state, dispatch] = useReducer(quizReducer, questions, (qs) =>
		createQuiz(qs.map((q) => q.id)),
	);

	const run = useMemo(
		() => state.order.map((id) => byId.get(id)).filter((q) => q !== undefined),
		[state.order, byId],
	);
	const current = run[state.index];
	const picks = current ? (state.picks[current.id] ?? []) : [];

	const pick = useCallback(
		(option: number) => {
			if (!current) return;
			const next = quizReducer(state, {
				type: "pick",
				question: current,
				option,
			});
			if (next === state) return;
			dispatch({ type: "pick", question: current, option });
			const nextPicks = next.picks[current.id];
			if (isComplete(current, nextPicks)) {
				progressStore.record(current.id, {
					at: Date.now(),
					correct: isCorrect(current, nextPicks),
				});
			}
		},
		[current, state],
	);

	const go = useCallback(
		(delta: number) => dispatch({ type: "go", delta }),
		[],
	);
	const restart = useCallback(
		(order: string[]) => dispatch({ type: "restart", order }),
		[],
	);
	const shuffle = useCallback(
		() => restart(shuffled(questions.map((q) => q.id))),
		[questions, restart],
	);

	return {
		run,
		index: state.index,
		current,
		picks,
		allPicks: state.picks,
		done: current ? isComplete(current, picks) : false,
		score: scoreSteps(run, state.picks),
		pick,
		go,
		restart,
		startOver: useCallback(
			() => restart(questions.map((q) => q.id)),
			[questions, restart],
		),
		shuffle,
	};
}

export type QuizController = ReturnType<typeof useQuiz>;
