import { z } from "zod";
import { STUDY_SETS, type StudySet } from "@/lib/scheduler";
import { DIFFICULTIES, GRADES, PERIODS } from "@/lib/types";

const SET_KEYS = Object.keys(STUDY_SETS) as [StudySet, ...StudySet[]];

/** Search params of the study page, and the input of the next-card call. */
export const studySearchSchema = z.object({
	set: z.enum(SET_KEYS).catch("smart").default("smart"),
	period: z.enum(PERIODS).catch("6m").default("6m"),
	topic: z.string().optional().catch(undefined),
	difficulty: z.enum(DIFFICULTIES).optional().catch(undefined),
	/** Show this problem instead of the next one in the queue. */
	slug: z.string().optional().catch(undefined),
});
export type StudySearch = z.infer<typeof studySearchSchema>;

export const attemptSchema = z.object({
	slug: z.string().min(1),
	grade: z.enum(GRADES),
	guessed: z.array(z.string()).max(200).default([]),
	hints: z.number().int().min(0).max(10).default(0),
});
export type AttemptInput = z.output<typeof attemptSchema>;

/** Clear one problem (`slug`) or everything (`all`); unknown keys are rejected, never ignored. */
export const resetSchema = z.union([
	z.strictObject({ slug: z.string().min(1) }),
	z.strictObject({ all: z.union([z.literal(true), z.literal("true")]) }),
]);

export const searchSchema = z.object({
	q: z.string().max(200),
	limit: z.coerce.number().int().min(1).max(1000).default(20),
});
