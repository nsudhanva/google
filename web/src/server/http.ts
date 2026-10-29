import { ZodError } from "zod";
import { NotFoundError } from "@/server/service";

class BadRequestError extends Error {}

/** The request body as JSON; malformed JSON is the client's fault (400). */
export async function bodyOf(request: Request): Promise<unknown> {
	try {
		return await request.json();
	} catch {
		throw new BadRequestError("Body must be JSON");
	}
}

/**
 * Runs an /api handler: JSON for data, 204 for nothing, 400 for bad input, 404 for an
 * unknown problem. Anything else is a real error and propagates.
 */
export async function respond(
	run: () => unknown,
	status = 200,
): Promise<Response> {
	try {
		const data = await run();
		return data === undefined
			? new Response(null, { status: 204 })
			: Response.json(data, { status });
	} catch (error) {
		if (error instanceof ZodError) {
			return Response.json(
				{ error: "Invalid input", issues: error.issues },
				{ status: 400 },
			);
		}
		if (error instanceof BadRequestError) {
			return Response.json({ error: error.message }, { status: 400 });
		}
		if (error instanceof NotFoundError) {
			return Response.json({ error: error.message }, { status: 404 });
		}
		throw error;
	}
}

export function queryOf(request: Request): Record<string, string> {
	return Object.fromEntries(new URL(request.url).searchParams);
}
