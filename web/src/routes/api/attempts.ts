import { createFileRoute } from "@tanstack/react-router";
import { attemptSchema } from "@/lib/schemas";
import { bodyOf, respond } from "@/server/http";
import { recordAttempt } from "@/server/service";

/** POST /api/attempts {slug, grade, guessed, hints}: grade or skip a card. */
export const Route = createFileRoute("/api/attempts")({
	server: {
		handlers: {
			POST: ({ request }) =>
				respond(
					async () => recordAttempt(attemptSchema.parse(await bodyOf(request))),
					201,
				),
		},
	},
});
