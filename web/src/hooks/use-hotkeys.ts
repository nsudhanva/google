import { useEffect, useRef } from "react";

type Handlers = Record<string, (event: KeyboardEvent) => void>;

function isTyping(target: EventTarget | null) {
	return (
		target instanceof HTMLElement &&
		(target.isContentEditable ||
			["INPUT", "TEXTAREA", "SELECT"].includes(target.tagName))
	);
}

/**
 * Single-key shortcuts (`event.key`, such as "Enter" or "1"). Ignored while typing in a
 * field, with a modifier held, or when a dialog or menu has focus.
 */
export function useHotkeys(handlers: Handlers) {
	const latest = useRef(handlers);
	latest.current = handlers;

	useEffect(() => {
		function onKeyDown(event: KeyboardEvent) {
			if (event.metaKey || event.ctrlKey || event.altKey) return;
			if (isTyping(event.target) || event.defaultPrevented) return;
			const target = event.target instanceof Element ? event.target : null;
			if (target?.closest("[role=dialog],[role=menu],[role=listbox]")) return;
			// Enter on a focused button or link activates that control, not the shortcut.
			// Toggle buttons (topic chips) toggle with Space and leave Enter to the shortcut.
			if (
				event.key === "Enter" &&
				target?.closest("button:not([aria-pressed]),a")
			)
				return;
			const handler = latest.current[event.key];
			if (!handler) return;
			event.preventDefault();
			handler(event);
		}
		window.addEventListener("keydown", onKeyDown);
		return () => window.removeEventListener("keydown", onKeyDown);
	}, []);
}
