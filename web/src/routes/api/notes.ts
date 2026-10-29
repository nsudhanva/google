import { createFileRoute } from "@tanstack/react-router";
import { noteSchema } from "@/lib/schemas";
import { bodyOf, respond } from "@/server/http";
import { saveNote } from "@/server/service";

/** PUT /api/notes {slug, text}: save your answer to a problem; empty text deletes it. */
export const Route = createFileRoute("/api/notes")({
	server: {
		handlers: {
			PUT: ({ request }) =>
				respond(async () => saveNote(noteSchema.parse(await bodyOf(request)))),
		},
	},
});
