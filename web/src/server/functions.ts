import { createServerFn } from "@tanstack/react-start";
import {
	attemptSchema,
	resetSchema,
	searchSchema,
	studySearchSchema,
} from "@/lib/schemas";
import * as service from "@/server/service";

/** RPC wrappers the UI calls; the logic lives in @/server/service. */

export const getDeck = createServerFn({ method: "GET" })
	.validator(studySearchSchema)
	.handler(({ data }) => service.getDeck(data));

export const recordAttempt = createServerFn({ method: "POST" })
	.validator(attemptSchema)
	.handler(({ data }) => service.recordAttempt(data));

export const resetProgress = createServerFn({ method: "POST" })
	.validator(resetSchema)
	.handler(({ data }) =>
		service.resetProgress("slug" in data ? data.slug : undefined),
	);

export const listProblems = createServerFn({ method: "GET" }).handler(() =>
	service.listProblems(),
);

export const searchProblems = createServerFn({ method: "GET" })
	.validator(searchSchema)
	.handler(({ data }) => service.searchProblems(data.q, data.limit));

export const getReadiness = createServerFn({ method: "GET" }).handler(() =>
	service.getReadiness(),
);

export const getReport = createServerFn({ method: "GET" }).handler(() =>
	service.getReport(),
);
