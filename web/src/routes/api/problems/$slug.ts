import { createFileRoute } from "@tanstack/react-router";
import { respond } from "@/server/http";
import { getCard } from "@/server/service";

/** GET /api/problems/two-sum: the full card (statement, topics, approach, hints, state). */
export const Route = createFileRoute("/api/problems/$slug")({
	server: {
		handlers: { GET: ({ params }) => respond(() => getCard(params.slug)) },
	},
});
