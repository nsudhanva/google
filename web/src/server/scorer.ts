import { type ScoreReport, scoreReport } from "@/lib/scorer";
import { getContent } from "@/server/content";
import { allAttempts, saveDailyScore } from "@/server/db";

/**
 * Background scorer: recomputes the report off the request path after every attempt, and on
 * a timer so mastery decay and the daily trend stay current between sessions.
 */
const REFRESH_MS = 15 * 60_000;

interface ScorerState {
	report?: ScoreReport;
	timer?: ReturnType<typeof setInterval>;
}

// Kept on globalThis so dev-server module reloads do not start a second timer.
const store = globalThis as { __scorer?: ScorerState };
store.__scorer ??= {};
const scorer = store.__scorer;

function refresh(): ScoreReport {
	const now = Date.now();
	const report = scoreReport(getContent().problems, allAttempts(), now);
	if (report.graded > 0) saveDailyScore(now, report);
	scorer.report = report;
	return report;
}

/** Timer and post-attempt refreshes must not take the server down; readers retry. */
function refreshInBackground() {
	try {
		refresh();
	} catch (error) {
		console.error("Background scorer failed", error);
	}
}

function ensureRunning() {
	if (scorer.timer) return;
	scorer.timer = setInterval(refreshInBackground, REFRESH_MS);
	scorer.timer.unref?.();
}

export function currentReport(): ScoreReport {
	ensureRunning();
	return scorer.report ?? refresh();
}

/** Call after the attempt log changes. Readers get a fresh report either way. */
export function invalidateReport() {
	scorer.report = undefined;
	setImmediate(() => {
		if (!scorer.report) refreshInBackground();
	});
}
