import { createFileRoute } from "@tanstack/react-router";
import { respond } from "@/server/http";
import { getReport } from "@/server/service";

/** GET /api/report: the background scorer's latest report and the daily trend. */
export const Route = createFileRoute("/api/report")({
	server: { handlers: { GET: () => respond(getReport) } },
});
