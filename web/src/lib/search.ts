import type { Difficulty, Problem } from "@/lib/types";

/** Where a hit matched, strongest first. A hit reports its weakest required match. */
const FIELDS = ["number", "title", "difficulty", "topic", "statement"] as const;
export type SearchField = (typeof FIELDS)[number];

export interface SearchHit {
	slug: string;
	id: number;
	rank: number;
	title: string;
	difficulty: Difficulty;
	field: SearchField;
	/** Statement excerpt around the match, for statement-only hits. */
	snippet: string | null;
}

interface Doc {
	problem: Problem;
	title: string;
	titleWords: string[];
	acronym: string;
	topicWords: string[];
	difficulty: string;
	plain: string;
	text: string;
}

export type SearchIndex = Doc[];

const NUMBER_QUERY = /^(?:lc|leetcode|#|no\.?|problem)?\s*(\d{1,5})$/i;
const SNIPPET_RADIUS = 60;
const ENTITIES: Record<string, string> = {
	"&lt;": "<",
	"&gt;": ">",
	"&amp;": "&",
	"&quot;": '"',
	"&#39;": "'",
	"&nbsp;": " ",
};

export function normalize(text: string): string {
	return text
		.toLowerCase()
		.normalize("NFKD")
		.replace(/[̀-ͯ]/g, "")
		.replace(/[^a-z0-9]+/g, " ")
		.trim();
}

function plainText(html: string | null): string {
	return (html ?? "")
		.replace(/<[^>]+>/g, " ")
		.replace(/&[a-z#0-9]+;/g, (entity) => ENTITIES[entity] ?? " ")
		.replace(/\s+/g, " ")
		.trim();
}

export function buildIndex(problems: Problem[]): SearchIndex {
	return problems.map((problem) => {
		const title = normalize(problem.title);
		const titleWords = title.split(" ");
		const plain = plainText(problem.description);
		return {
			problem,
			title,
			titleWords,
			acronym: titleWords.map((w) => w[0]).join(""),
			topicWords: normalize(problem.topics.join(" ")).split(" "),
			difficulty: problem.difficulty.toLowerCase(),
			plain,
			text: ` ${normalize(plain)} `,
		};
	});
}

/** Edit distance where a swap of neighbors counts once ("rian" → "rain"), capped at `max`. */
function withinEdits(a: string, b: string, max: number): boolean {
	if (Math.abs(a.length - b.length) > max) return false;
	let older: number[] = [];
	let previous = Array.from({ length: b.length + 1 }, (_, j) => j);
	for (let i = 1; i <= a.length; i++) {
		const current = [i];
		for (let j = 1; j <= b.length; j++) {
			const cost = a[i - 1] === b[j - 1] ? 0 : 1;
			current[j] = Math.min(
				previous[j] + 1,
				current[j - 1] + 1,
				previous[j - 1] + cost,
			);
			if (i > 1 && j > 1 && a[i - 1] === b[j - 2] && a[i - 2] === b[j - 1]) {
				current[j] = Math.min(current[j], older[j - 2] + 1);
			}
		}
		if (Math.min(...current) > max) return false;
		older = previous;
		previous = current;
	}
	return previous[b.length] <= max;
}

/** Best match of one query token in a document, or null when it matches nowhere. */
function matchToken(
	doc: Doc,
	token: string,
): { score: number; field: SearchField } | null {
	if (doc.titleWords.includes(token)) return { score: 60, field: "title" };
	if (doc.titleWords.some((w) => w.startsWith(token)))
		return { score: 45, field: "title" };
	if (doc.title.includes(token)) return { score: 30, field: "title" };
	const typos = token.length >= 8 ? 2 : 1;
	if (
		token.length >= 4 &&
		doc.titleWords.some((w) => withinEdits(token, w, typos))
	)
		return { score: 25, field: "title" };
	if (doc.difficulty === token) return { score: 20, field: "difficulty" };
	if (doc.topicWords.some((w) => w.startsWith(token)))
		return { score: 15, field: "topic" };
	if (doc.text.includes(` ${token}`)) return { score: 5, field: "statement" };
	return null;
}

function snippet(plain: string, token: string): string {
	const at = plain.toLowerCase().indexOf(token);
	if (at < 0) return plain.slice(0, 2 * SNIPPET_RADIUS);
	const start = Math.max(0, at - SNIPPET_RADIUS);
	const end = Math.min(plain.length, at + token.length + SNIPPET_RADIUS);
	return `${start > 0 ? "…" : ""}${plain.slice(start, end)}${end < plain.length ? "…" : ""}`;
}

function hit(doc: Doc, field: SearchField, snippetToken?: string): SearchHit {
	const { slug, id, rank, title, difficulty } = doc.problem;
	return {
		slug,
		id,
		rank,
		title,
		difficulty,
		field,
		snippet:
			field === "statement" && snippetToken
				? snippet(doc.plain, snippetToken)
				: null,
	};
}

/**
 * Ranks problems for a free-text query: LeetCode number, title (words, prefixes, acronym,
 * small typos), difficulty, topic or statement text. Every word must match somewhere; ties
 * go to the problem Google asks more often.
 */
export function search(
	index: SearchIndex,
	query: string,
	limit = 20,
): SearchHit[] {
	const raw = query.trim();
	const q = normalize(raw);
	if (!q) return [];
	const tokens = q.split(" ");
	const compact = tokens.join("");
	const number = NUMBER_QUERY.exec(raw)?.[1];

	const scored: { hit: SearchHit; score: number }[] = [];
	for (const doc of index) {
		if (number && doc.problem.id === Number(number)) {
			scored.push({ hit: hit(doc, "number"), score: 10_000 });
			continue;
		}
		// "lis" finds Longest Increasing Subsequence even though no word matches.
		if (compact.length >= 2 && doc.acronym === compact) {
			scored.push({ hit: hit(doc, "title"), score: 300 });
			continue;
		}
		const matches = tokens.map((t) => matchToken(doc, t));
		if (matches.some((m) => m === null)) continue;
		let score = 0;
		let weakest = 0;
		let weakestToken = tokens[0];
		matches.forEach((m, i) => {
			if (!m) return;
			score += m.score;
			const fieldRank = FIELDS.indexOf(m.field);
			if (fieldRank >= weakest) {
				weakest = fieldRank;
				weakestToken = tokens[i];
			}
		});
		if (doc.title === q) score += 500;
		else if (doc.title.startsWith(q)) score += 200;
		scored.push({ hit: hit(doc, FIELDS[weakest], weakestToken), score });
	}
	return scored
		.sort((a, b) => b.score - a.score || a.hit.rank - b.hit.rank)
		.slice(0, limit)
		.map((s) => s.hit);
}
