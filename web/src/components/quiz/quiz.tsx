import { ArrowLeftIcon, ArrowRightIcon, ShuffleIcon } from "lucide-react";
import { QuestionCard } from "@/components/quiz/question-card";
import { QuizSummary } from "@/components/quiz/quiz-summary";
import { Button } from "@/components/ui/button";
import { Kbd } from "@/components/ui/kbd";
import { Progress } from "@/components/ui/progress";
import type { Question } from "@/data/gha";
import { useQuiz } from "@/hooks/use-quiz";
import { useQuizKeyboard } from "@/hooks/use-quiz-keyboard";
import { masteryOf } from "@/lib/progress";
import { useProgress } from "@/lib/progress-store";

export function Quiz({ questions }: { questions: readonly Question[] }) {
	const quiz = useQuiz(questions);
	const progress = useProgress();
	useQuizKeyboard(quiz);

	const { run, index, current, picks, done, score } = quiz;
	const last = index === run.length - 1;
	const history = current ? (progress.attempts[current.id] ?? []) : [];
	// A finished question's newest attempt is this one; show mastery from before it.
	const mastery = masteryOf(done ? history.slice(0, -1) : history);

	return (
		<div>
			<div className="mb-8 space-y-2">
				<div className="flex items-baseline justify-between gap-4 text-sm text-muted-foreground">
					<span>
						{current ? `Question ${index + 1} of ${run.length}` : "Finished"}
					</span>
					<span aria-live="polite" className="tabular-nums">
						{score.correct} of {score.answered} correct
					</span>
				</div>
				<Progress
					value={score.total ? (score.answered / score.total) * 100 : 0}
					aria-label="Answered in this run"
				/>
			</div>

			{current ? (
				<QuestionCard
					key={current.id}
					question={current}
					picks={picks}
					mastery={mastery}
					onPick={quiz.pick}
				/>
			) : (
				<QuizSummary
					run={run}
					picks={quiz.allPicks}
					onRetry={quiz.restart}
					onStartOver={quiz.startOver}
				/>
			)}

			<div className="mt-10 flex flex-wrap items-center gap-2">
				<Button
					variant="outline"
					size="lg"
					onClick={() => quiz.go(-1)}
					disabled={index === 0}
				>
					<ArrowLeftIcon data-icon="inline-start" />
					Previous
				</Button>
				{current && (
					<Button
						size="lg"
						variant={done ? "default" : "outline"}
						onClick={() => quiz.go(1)}
					>
						{done ? (last ? "See results" : "Next question") : "Skip"}
						<ArrowRightIcon data-icon="inline-end" />
					</Button>
				)}
				<Button
					variant="ghost"
					size="lg"
					className="ml-auto"
					onClick={quiz.shuffle}
				>
					<ShuffleIcon data-icon="inline-start" />
					Shuffle and restart
				</Button>
			</div>
			<p className="mt-4 hidden flex-wrap items-center gap-x-4 gap-y-1 text-sm text-muted-foreground sm:flex">
				<span className="flex items-center gap-1.5">
					<Kbd>1</Kbd>–<Kbd>{current?.options.length ?? 5}</Kbd> answer
				</span>
				<span className="flex items-center gap-1.5">
					<Kbd>Enter</Kbd> next
				</span>
				<span className="flex items-center gap-1.5">
					<Kbd>←</Kbd> back
				</span>
			</p>
		</div>
	);
}
