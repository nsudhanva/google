import { createFileRoute } from "@tanstack/react-router";
import { searchSchema } from "@/lib/schemas";
import { queryOf, respond } from "@/server/http";
import { searchProblems } from "@/server/service";

/** GET /api/search?q=two+sum&limit=10: ranked problems for a free-text query. */
export const Route = createFileRoute("/api/search")({
	server: {
		handlers: {
			GET: ({ request }) =>
				respond(() => {
					const { q, limit } = searchSchema.parse(queryOf(request));
					return searchProblems(q, limit);
				}),
		},
	},
});
