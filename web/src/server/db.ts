import { mkdirSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { DatabaseSync } from "node:sqlite";
import { dayKey } from "@/lib/scorer";
import type { Attempt, Grade } from "@/lib/types";

const DATABASE_PATH = resolve(
	process.env.DATABASE_PATH ?? "../data/progress.db",
);

const SCHEMA = `
CREATE TABLE IF NOT EXISTS attempts (
	id INTEGER PRIMARY KEY,
	slug TEXT NOT NULL,
	at INTEGER NOT NULL,
	grade TEXT NOT NULL CHECK (grade IN ('again', 'good', 'less', 'skip')),
	guessed TEXT NOT NULL DEFAULT '[]',
	score REAL,
	hints INTEGER NOT NULL DEFAULT 0
);
CREATE INDEX IF NOT EXISTS attempts_at ON attempts (at);
CREATE TABLE IF NOT EXISTS daily_scores (
	day TEXT PRIMARY KEY,
	at INTEGER NOT NULL,
	readiness REAL NOT NULL,
	coverage REAL NOT NULL,
	accuracy REAL
);
CREATE TABLE IF NOT EXISTS notes (
	slug TEXT PRIMARY KEY,
	text TEXT NOT NULL,
	at INTEGER NOT NULL
);
`;

let db: DatabaseSync | undefined;

function open(): DatabaseSync {
	if (!db) {
		mkdirSync(dirname(DATABASE_PATH), { recursive: true });
		db = new DatabaseSync(DATABASE_PATH);
		db.exec("PRAGMA journal_mode = WAL; PRAGMA busy_timeout = 5000;");
		db.exec(SCHEMA);
		migrate(db);
	}
	return db;
}

/** Brings databases made by older versions up to the current schema. */
function migrate(database: DatabaseSync) {
	const columns = database
		.prepare("SELECT name FROM pragma_table_info('attempts')")
		.all() as { name: string }[];
	if (!columns.some((c) => c.name === "hints")) {
		database.exec(
			"ALTER TABLE attempts ADD COLUMN hints INTEGER NOT NULL DEFAULT 0",
		);
	}
}

interface AttemptRow {
	slug: string;
	at: number;
	grade: Grade;
	guessed: string;
	score: number | null;
	hints: number;
}

/** The whole attempt log, oldest first. Card state and scores are replayed from it. */
export function allAttempts(): Attempt[] {
	const rows = open()
		.prepare(
			"SELECT slug, at, grade, guessed, score, hints FROM attempts ORDER BY at, id",
		)
		.all() as unknown as AttemptRow[];
	return rows.map((row) => ({ ...row, guessed: JSON.parse(row.guessed) }));
}

export function insertAttempt(attempt: Attempt) {
	open()
		.prepare(
			"INSERT INTO attempts (slug, at, grade, guessed, score, hints) VALUES (?, ?, ?, ?, ?, ?)",
		)
		.run(
			attempt.slug,
			attempt.at,
			attempt.grade,
			JSON.stringify(attempt.guessed),
			attempt.score,
			attempt.hints,
		);
}

/** Clears one problem's history, or everything when no slug is given. */
export function deleteAttempts(slug?: string) {
	const database = open();
	if (slug) {
		database.prepare("DELETE FROM attempts WHERE slug = ?").run(slug);
	} else {
		database.exec("DELETE FROM attempts; DELETE FROM daily_scores;");
	}
}

export interface DailyScore {
	day: string;
	readiness: number;
	coverage: number;
	accuracy: number | null;
}

export function saveDailyScore(at: number, score: Omit<DailyScore, "day">) {
	open()
		.prepare(
			`INSERT INTO daily_scores (day, at, readiness, coverage, accuracy)
			VALUES (?, ?, ?, ?, ?)
			ON CONFLICT (day) DO UPDATE SET
				at = excluded.at, readiness = excluded.readiness,
				coverage = excluded.coverage, accuracy = excluded.accuracy`,
		)
		.run(dayKey(at), at, score.readiness, score.coverage, score.accuracy);
}

export function dailyScores(limit = 60): DailyScore[] {
	const rows = open()
		.prepare(
			"SELECT day, readiness, coverage, accuracy FROM daily_scores ORDER BY day DESC LIMIT ?",
		)
		.all(limit) as unknown as DailyScore[];
	return rows.reverse();
}

/** Your own answer to a problem. Notes are not progress: clearing progress keeps them. */
export function noteFor(slug: string): string | null {
	const row = open()
		.prepare("SELECT text FROM notes WHERE slug = ?")
		.get(slug) as { text: string } | undefined;
	return row?.text ?? null;
}

/** Saves a note; empty text deletes it. */
export function saveNote(slug: string, text: string, at: number) {
	const database = open();
	if (!text) {
		database.prepare("DELETE FROM notes WHERE slug = ?").run(slug);
		return;
	}
	database
		.prepare(
			`INSERT INTO notes (slug, text, at) VALUES (?, ?, ?)
			ON CONFLICT (slug) DO UPDATE SET text = excluded.text, at = excluded.at`,
		)
		.run(slug, text, at);
}
