import {
	ClientOnly,
	createFileRoute,
	Link,
	stripSearchParams,
} from "@tanstack/react-router";
import { useState } from "react";
import { z } from "zod";
import { PageHeader } from "@/components/page-header";
import { Quiz } from "@/components/quiz/quiz";
import { buttonVariants } from "@/components/ui/button";
import { QUESTIONS, SECTION_IDS, SECTIONS, type Section } from "@/data/gha";
import { masteryOf } from "@/lib/progress";
import { useProgress } from "@/lib/progress-store";
import { cn } from "@/lib/utils";

const searchSchema = z.object({
	section: z
		.enum(["all", ...SECTION_IDS])
		.default("all")
		.catch("all"),
	mode: z.enum(["all", "review"]).default("all").catch("all"),
});

type PracticeSearch = z.infer<typeof searchSchema>;

export const Route = createFileRoute("/")({
	validateSearch: searchSchema,
	search: { middlewares: [stripSearchParams({ section: "all", mode: "all" })] },
	head: () => ({ meta: [{ title: "Practice | GHA practice" }] }),
	component: PracticePage,
});

function PracticePage() {
	const { section, mode } = Route.useSearch();

	return (
		<>
			<PageHeader title="Practice">
				{QUESTIONS.length} questions from candidate reports of the Google Hiring
				Assessment. Pick an answer to see whether it's right and why.
			</PageHeader>
			<Filters section={section} mode={mode} />
			<ClientOnly fallback={<QuizSkeleton />}>
				<PracticeSession
					key={`${section}:${mode}`}
					section={section}
					mode={mode}
				/>
			</ClientOnly>
		</>
	);
}

function Filters({ section, mode }: PracticeSearch) {
	const count = (s: "all" | Section) =>
		s === "all"
			? QUESTIONS.length
			: QUESTIONS.filter((q) => q.section === s).length;

	return (
		<div className="mb-8 space-y-3">
			<nav aria-label="Sections" className="flex flex-wrap gap-2">
				{(["all", ...SECTION_IDS] as const).map((s) => (
					<Link
						key={s}
						to="/"
						search={(prev) => ({ ...prev, section: s })}
						aria-current={s === section ? "page" : undefined}
						className={cn(
							buttonVariants({
								variant: s === section ? "default" : "outline",
								size: "sm",
							}),
							"rounded-full",
						)}
					>
						{s === "all" ? "All" : SECTIONS[s].name}
						<span className="tabular-nums opacity-70">{count(s)}</span>
					</Link>
				))}
			</nav>
			<nav aria-label="Question set" className="flex flex-wrap gap-1">
				{(
					[
						["all", "All questions"],
						["review", "Not yet mastered"],
					] as const
				).map(([m, label]) => (
					<Link
						key={m}
						to="/"
						search={(prev) => ({ ...prev, mode: m })}
						aria-current={m === mode ? "page" : undefined}
						className={cn(
							buttonVariants({ variant: "ghost", size: "sm" }),
							m === mode ? "bg-muted text-foreground" : "text-muted-foreground",
						)}
					>
						{label}
					</Link>
				))}
			</nav>
		</div>
	);
}

function PracticeSession({ section, mode }: PracticeSearch) {
	const progress = useProgress();
	// Freeze the question set for this run so mastering a question mid-run doesn't remove it.
	const [questions] = useState(() =>
		QUESTIONS.filter(
			(q) =>
				(section === "all" || q.section === section) &&
				(mode === "all" || masteryOf(progress.attempts[q.id]) !== "mastered"),
		),
	);

	if (questions.length === 0) {
		return (
			<div className="rounded-xl border border-dashed p-8 text-center">
				<p className="text-lg font-semibold">Everything here is mastered.</p>
				<p className="mt-1 text-muted-foreground">
					Practice the full set to keep it fresh, or pick another section.
				</p>
				<Link
					to="/"
					search={{ section, mode: "all" }}
					className={cn(buttonVariants(), "mt-4")}
				>
					Practice all questions
				</Link>
			</div>
		);
	}

	return <Quiz questions={questions} />;
}

function QuizSkeleton() {
	return (
		<div aria-hidden className="animate-pulse space-y-6">
			<div className="h-1.5 rounded-full bg-muted" />
			<div className="h-20 rounded-xl bg-muted" />
			<div className="grid gap-2 sm:grid-cols-5">
				{[0, 1, 2, 3, 4].map((i) => (
					<div key={i} className="h-24 rounded-xl bg-muted" />
				))}
			</div>
		</div>
	);
}
