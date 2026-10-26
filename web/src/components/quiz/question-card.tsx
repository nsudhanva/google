import { MasteryBadge } from "@/components/mastery-badge";
import { AnswerFeedback } from "@/components/quiz/answer-feedback";
import {
	AnswerOption,
	type AnswerState,
} from "@/components/quiz/answer-option";
import { type Question, SECTIONS } from "@/data/gha";
import type { Mastery } from "@/lib/progress";
import { visibleOptions } from "@/lib/quiz";
import { cn } from "@/lib/utils";

function answerState(
	option: number,
	answer: number,
	pick: number | undefined,
): AnswerState {
	if (pick === undefined) return "idle";
	if (option === answer) return option === pick ? "correct-picked" : "correct";
	return option === pick ? "incorrect" : "dimmed";
}

export function QuestionCard({
	question,
	picks,
	mastery,
	onPick,
}: {
	question: Question;
	picks: readonly number[];
	/** Mastery before this attempt, so the badge doesn't change mid-question. */
	mastery: Mastery;
	onPick: (option: number) => void;
}) {
	const isScale = question.section === "likert";
	const complete = picks.length === question.steps.length;

	return (
		<article aria-labelledby={`q-${question.id}`}>
			<div className="flex flex-wrap items-center gap-2 text-sm text-muted-foreground">
				<span>{SECTIONS[question.section].blurb}</span>
				<MasteryBadge mastery={mastery} />
			</div>
			<h2
				id={`q-${question.id}`}
				className="mt-3 text-[clamp(1.6rem,4.2vw,2.4rem)] leading-[1.15] font-semibold tracking-tight text-balance"
			>
				{question.text}
			</h2>

			{question.steps.map((step, s) => {
				if (s > picks.length) return null;
				const pick = picks[s];
				const active = s === picks.length;
				const showPrompt = question.steps.length > 1 || !isScale;

				return (
					<section key={step.prompt} className="mt-8" aria-label={step.prompt}>
						{showPrompt && (
							<h3 className="mb-3 font-semibold">{step.prompt}</h3>
						)}
						<div className={cn("grid gap-2", isScale && "sm:grid-cols-5")}>
							{visibleOptions(question, s).map((option, n) => (
								<AnswerOption
									key={option}
									label={question.options[option]}
									shortcut={n + 1}
									layout={isScale ? "scale" : "list"}
									state={answerState(option, step.answer, pick)}
									onSelect={() => active && onPick(option)}
								/>
							))}
						</div>
						{pick !== undefined && (
							<AnswerFeedback correct={pick === step.answer} why={step.why} />
						)}
					</section>
				);
			})}

			{complete && (
				<p className="mt-6 border-t pt-4 text-sm text-muted-foreground">
					Source: {question.source}
				</p>
			)}
		</article>
	);
}
