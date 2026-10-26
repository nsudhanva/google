import { useSyncExternalStore } from "react";
import {
	type Attempt,
	EMPTY_PROGRESS,
	type ProgressData,
	parseProgress,
	recordAttempt,
} from "@/lib/progress";

const STORAGE_KEY = "gha-practice:progress";

/**
 * Practice history lives in this browser's localStorage. Reads and writes are wrapped so
 * private windows or blocked storage degrade to an in-memory session instead of crashing.
 */
let snapshot: ProgressData | null = null;
const listeners = new Set<() => void>();

function load(): ProgressData {
	try {
		const raw = window.localStorage.getItem(STORAGE_KEY);
		return raw ? parseProgress(JSON.parse(raw)) : EMPTY_PROGRESS;
	} catch {
		return EMPTY_PROGRESS;
	}
}

function save(data: ProgressData) {
	snapshot = data;
	try {
		window.localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
	} catch {
		// Storage unavailable: keep the in-memory snapshot for this session.
	}
	for (const listener of listeners) listener();
}

function getSnapshot(): ProgressData {
	snapshot ??= load();
	return snapshot;
}

function getServerSnapshot(): ProgressData {
	return EMPTY_PROGRESS;
}

function onStorage(event: StorageEvent) {
	if (event.key !== STORAGE_KEY) return;
	snapshot = load();
	for (const listener of listeners) listener();
}

function subscribe(listener: () => void) {
	if (listeners.size === 0) window.addEventListener("storage", onStorage);
	listeners.add(listener);
	return () => {
		listeners.delete(listener);
		if (listeners.size === 0) window.removeEventListener("storage", onStorage);
	};
}

export const progressStore = {
	record(questionId: string, attempt: Attempt) {
		save(recordAttempt(getSnapshot(), questionId, attempt));
	},
	reset() {
		save(EMPTY_PROGRESS);
	},
};

/** Current practice history; empty during SSR and hydration. */
export function useProgress(): ProgressData {
	return useSyncExternalStore(subscribe, getSnapshot, getServerSnapshot);
}
