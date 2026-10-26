import { useEffect } from "react";
import type { QuizController } from "@/hooks/use-quiz";
import { visibleOptions } from "@/lib/quiz";

function isTypingTarget(target: EventTarget | null): boolean {
	return (
		target instanceof HTMLElement &&
		(target.isContentEditable ||
			["INPUT", "TEXTAREA", "SELECT"].includes(target.tagName))
	);
}

/** 1–5 answers the active step, Enter/→ advances once answered, ← goes back. */
export function useQuizKeyboard({
	current,
	picks,
	done,
	pick,
	go,
}: QuizController) {
	useEffect(() => {
		function onKeyDown(event: KeyboardEvent) {
			if (
				event.defaultPrevented ||
				event.metaKey ||
				event.ctrlKey ||
				event.altKey
			)
				return;
			if (isTypingTarget(event.target)) return;
			// Leave keys alone while a menu or dialog has focus.
			if (
				event.target instanceof HTMLElement &&
				event.target.closest("[role=menu],[role=dialog]")
			)
				return;

			const n = Number.parseInt(event.key, 10);
			if (current && !done && n >= 1) {
				const options = visibleOptions(current, picks.length);
				if (n <= options.length) pick(options[n - 1]);
			} else if (
				(event.key === "Enter" || event.key === "ArrowRight") &&
				(done || !current)
			) {
				// Enter on a focused button already clicks it.
				if (event.key === "Enter" && event.target instanceof HTMLButtonElement)
					return;
				go(1);
			} else if (event.key === "ArrowLeft") {
				go(-1);
			}
		}
		window.addEventListener("keydown", onKeyDown);
		return () => window.removeEventListener("keydown", onKeyDown);
	}, [current, picks.length, done, pick, go]);
}
