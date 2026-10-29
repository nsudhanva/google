import { createFileRoute } from "@tanstack/react-router";
import { resetSchema } from "@/lib/schemas";
import { queryOf, respond } from "@/server/http";
import { resetProgress } from "@/server/service";

/** DELETE /api/progress?slug=two-sum clears one problem; ?all=true clears everything. */
export const Route = createFileRoute("/api/progress")({
	server: {
		handlers: {
			DELETE: ({ request }) =>
				respond(() => {
					const target = resetSchema.parse(queryOf(request));
					resetProgress("slug" in target ? target.slug : undefined);
				}),
		},
	},
});
