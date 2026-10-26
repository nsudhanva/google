import { ClientOnly, createFileRoute, Link } from "@tanstack/react-router";
import { RotateCcwIcon } from "lucide-react";
import { MasteryBadge } from "@/components/mastery-badge";
import { PageHeader } from "@/components/page-header";
import {
	AlertDialog,
	AlertDialogAction,
	AlertDialogCancel,
	AlertDialogContent,
	AlertDialogDescription,
	AlertDialogFooter,
	AlertDialogHeader,
	AlertDialogTitle,
	AlertDialogTrigger,
} from "@/components/ui/alert-dialog";
import { Button, buttonVariants } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Progress } from "@/components/ui/progress";
import { QUESTIONS, SECTION_IDS, SECTIONS } from "@/data/gha";
import {
	type Attempt,
	masteryOf,
	summarize,
	summarizeBySection,
} from "@/lib/progress";
import { progressStore, useProgress } from "@/lib/progress-store";
import { cn } from "@/lib/utils";

export const Route = createFileRoute("/progress")({
	head: () => ({ meta: [{ title: "Progress | GHA practice" }] }),
	component: ProgressPage,
});

function ProgressPage() {
	return (
		<>
			<PageHeader title="Progress">
				A question is mastered once you answer it right twice in a row. One
				wrong answer puts it back into review. Progress is saved in this
				browser.
			</PageHeader>
			<ClientOnly
				fallback={<div className="h-64 animate-pulse rounded-xl bg-muted" />}
			>
				<ProgressDashboard />
			</ClientOnly>
		</>
	);
}

function ProgressDashboard() {
	const data = useProgress();
	const overall = summarize(QUESTIONS, data);
	const bySection = summarizeBySection(QUESTIONS, data);

	if (overall.seen === 0) {
		return (
			<div className="rounded-xl border border-dashed p-8 text-center">
				<p className="text-lg font-semibold">No answers yet.</p>
				<p className="mt-1 text-muted-foreground">
					Answer a few questions and your progress will show up here.
				</p>
				<Link to="/" className={cn(buttonVariants(), "mt-4")}>
					Start practicing
				</Link>
			</div>
		);
	}

	return (
		<div className="space-y-10">
			<dl className="grid grid-cols-3 gap-3">
				<Stat label="Mastered" value={`${overall.mastered}/${overall.total}`} />
				<Stat label="Needs work" value={String(overall.needsWork)} />
				<Stat
					label="Accuracy"
					value={
						overall.accuracy === null
							? "–"
							: `${Math.round(overall.accuracy * 100)}%`
					}
				/>
			</dl>

			<div className="flex flex-wrap gap-2">
				<Link
					to="/"
					search={{ mode: "review" }}
					className={buttonVariants({ size: "lg" })}
				>
					Practice what's not mastered
				</Link>
				<ResetProgress />
			</div>

			{SECTION_IDS.map((id) => {
				const summary = bySection[id];
				const questions = QUESTIONS.filter((q) => q.section === id);
				return (
					<section key={id} aria-labelledby={`section-${id}`}>
						<Card>
							<CardHeader className="gap-3">
								<div className="flex items-baseline justify-between gap-4">
									<CardTitle id={`section-${id}`} className="text-lg">
										{SECTIONS[id].name}
									</CardTitle>
									<span className="text-sm text-muted-foreground tabular-nums">
										{summary.mastered} of {summary.total} mastered
									</span>
								</div>
								<Progress
									value={(summary.mastered / summary.total) * 100}
									aria-label={`${SECTIONS[id].name} mastered`}
								/>
							</CardHeader>
							<CardContent>
								<ul className="divide-y">
									{questions.map((q) => (
										<QuestionRow
											key={q.id}
											text={q.text}
											attempts={data.attempts[q.id]}
										/>
									))}
								</ul>
							</CardContent>
						</Card>
					</section>
				);
			})}
		</div>
	);
}

function Stat({ label, value }: { label: string; value: string }) {
	return (
		<div className="rounded-xl border bg-card px-4 py-3">
			<dt className="text-sm text-muted-foreground">{label}</dt>
			<dd className="mt-1 text-2xl font-semibold tabular-nums">{value}</dd>
		</div>
	);
}

function QuestionRow({
	text,
	attempts,
}: {
	text: string;
	attempts: Attempt[] | undefined;
}) {
	const recent = attempts?.slice(-5) ?? [];
	return (
		<li className="flex items-center gap-3 py-2.5">
			<span className="min-w-0 flex-1 truncate" title={text}>
				{text}
			</span>
			{recent.length > 0 && (
				<span
					className="flex gap-1"
					role="img"
					aria-label={`Last ${recent.length}: ${recent.map((a) => (a.correct ? "right" : "wrong")).join(", ")}`}
				>
					{recent.map((a) => (
						<span
							key={a.at}
							className={cn(
								"size-2 rounded-full",
								a.correct ? "bg-success" : "bg-destructive",
							)}
						/>
					))}
				</span>
			)}
			<MasteryBadge mastery={masteryOf(attempts)} className="w-24" />
		</li>
	);
}

function ResetProgress() {
	return (
		<AlertDialog>
			<AlertDialogTrigger render={<Button variant="outline" size="lg" />}>
				<RotateCcwIcon data-icon="inline-start" />
				Reset progress
			</AlertDialogTrigger>
			<AlertDialogContent>
				<AlertDialogHeader>
					<AlertDialogTitle>Reset all progress?</AlertDialogTitle>
					<AlertDialogDescription>
						This clears every saved answer in this browser. It can't be undone.
					</AlertDialogDescription>
				</AlertDialogHeader>
				<AlertDialogFooter>
					<AlertDialogCancel>Keep progress</AlertDialogCancel>
					<AlertDialogAction
						variant="destructive"
						onClick={() => progressStore.reset()}
					>
						Reset progress
					</AlertDialogAction>
				</AlertDialogFooter>
			</AlertDialogContent>
		</AlertDialog>
	);
}
