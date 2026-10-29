import { useEffect, useState } from "react";
import type { SearchHit } from "@/lib/search";
import { searchProblems } from "@/server/functions";

const DEBOUNCE_MS = 120;
const MAX_QUERY = 200;

/** Server-ranked hits for a query, debounced; stale responses are dropped. */
export function useSearch(query: string, limit = 20): SearchHit[] {
	const [hits, setHits] = useState<SearchHit[]>([]);

	useEffect(() => {
		const q = query.trim().slice(0, MAX_QUERY);
		if (!q) {
			setHits([]);
			return;
		}
		let current = true;
		const timer = setTimeout(async () => {
			const next = await searchProblems({ data: { q, limit } }).catch(
				(error: unknown) => {
					console.error("Search failed", error);
					return [];
				},
			);
			if (current) setHits(next);
		}, DEBOUNCE_MS);
		return () => {
			current = false;
			clearTimeout(timer);
		};
	}, [query, limit]);

	return hits;
}
