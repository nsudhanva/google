import { createFileRoute } from "@tanstack/react-router";
import { respond } from "@/server/http";
import { listProblems } from "@/server/service";

/** GET /api/problems: every problem with its progress (no topics). */
export const Route = createFileRoute("/api/problems/")({
	server: { handlers: { GET: () => respond(listProblems) } },
});
