import { createFileRoute } from "@tanstack/react-router";
import { studySearchSchema } from "@/lib/schemas";
import { queryOf, respond } from "@/server/http";
import { getDeck } from "@/server/service";

/** GET /api/deck?set=again&topic=Graph+Theory: the next card in a study set. */
export const Route = createFileRoute("/api/deck")({
	server: {
		handlers: {
			GET: ({ request }) =>
				respond(() => getDeck(studySearchSchema.parse(queryOf(request)))),
		},
	},
});
