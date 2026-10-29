import { existsSync, readFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { buildIndex, type SearchIndex } from "@/lib/search";
import type { Approach, Problem } from "@/lib/types";

/** Built by the Python tools at the repo root: `uv run google ingest`, then the approach pass. */
const DATA_DIR = resolve(process.env.DATA_DIR ?? "../data");

function readJson<T>(name: string, fallback: T): T {
	const path = join(DATA_DIR, name);
	return existsSync(path) ? JSON.parse(readFileSync(path, "utf8")) : fallback;
}

interface Content {
	problems: Problem[];
	bySlug: Map<string, Problem>;
	approaches: Record<string, Approach>;
	/** Every topic in the list, most common first. */
	topics: string[];
	searchIndex: SearchIndex;
}

let content: Content | undefined;

export function getContent(): Content {
	if (content) return content;
	const { problems } = readJson<{ problems: Problem[] }>("problems.json", {
		problems: [],
	});
	const counts = new Map<string, number>();
	for (const topic of problems.flatMap((p) => p.topics)) {
		counts.set(topic, (counts.get(topic) ?? 0) + 1);
	}
	content = {
		problems,
		bySlug: new Map(problems.map((p) => [p.slug, p])),
		approaches: readJson("approaches.json", {}),
		topics: [...counts].sort((a, b) => b[1] - a[1]).map(([topic]) => topic),
		searchIndex: buildIndex(problems),
	};
	return content;
}
