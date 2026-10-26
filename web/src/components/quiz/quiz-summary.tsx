import { Link } from "@tanstack/react-router";
import { Button } from "@/components/ui/button";
import {
	Card,
	CardContent,
	CardDescription,
	CardHeader,
	CardTitle,
} from "@/components/ui/card";
import { type Question, SECTION_IDS, SECTIONS } from "@/data/gha";
import { isCorrect, scoreSteps } from "@/lib/quiz";

export function QuizSummary({
	run,
	picks,
	onRetry,
	onStartOver,
}: {
	run: readonly Question[];
	picks: Record<string, number[]>;
	onRetry: (ids: string[]) => void;
	onStartOver: () => void;
}) {
	const missed = run.filter((q) => !isCorrect(q, picks[q.id] ?? []));
	const sections = SECTION_IDS.map((id) => ({
		id,
		score: scoreSteps(
			run.filter((q) => q.section === id),
			picks,
		),
	})).filter(({ score }) => score.total > 0);

	return (
		<Card>
			<CardHeader>
				<CardTitle className="text-2xl tracking-tight">
					{missed.length === 0
						? "Every answer right."
						: `${missed.length} question${missed.length === 1 ? "" : "s"} to review.`}
				</CardTitle>
				<CardDescription>
					Results are saved to your{" "}
					<Link to="/progress" className="underline underline-offset-4">
						progress
					</Link>
					.
				</CardDescription>
			</CardHeader>
			<CardContent className="space-y-6">
				<dl className="divide-y border-y">
					{sections.map(({ id, score }) => (
						<div key={id} className="flex justify-between py-2.5">
							<dt>{SECTIONS[id].name}</dt>
							<dd className="font-semibold tabular-nums">
								{score.correct} / {score.total}
							</dd>
						</div>
					))}
				</dl>
				{missed.length > 0 && (
					<ul className="space-y-1.5 text-muted-foreground">
						{missed.map((q) => (
							<li key={q.id} className="leading-snug">
								{q.text}
							</li>
						))}
					</ul>
				)}
				<div className="flex flex-wrap gap-2">
					{missed.length > 0 && (
						<Button size="lg" onClick={() => onRetry(missed.map((q) => q.id))}>
							Retry the {missed.length} missed
						</Button>
					)}
					<Button size="lg" variant="outline" onClick={onStartOver}>
						Start over
					</Button>
				</div>
			</CardContent>
		</Card>
	);
}
