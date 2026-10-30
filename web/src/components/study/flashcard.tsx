import { ExternalLinkIcon, LightbulbIcon, RotateCcwIcon } from "lucide-react";
import { type ComponentProps, type ReactNode, useState } from "react";
import { AskedBadges } from "@/components/asked-badges";
import { ConfirmClear } from "@/components/confirm-clear";
import { DifficultyBadge } from "@/components/difficulty-badge";
import { FitPages } from "@/components/fit-pages";
import { InlineCode } from "@/components/inline-code";
import { Segmented } from "@/components/segmented";
import { Answer } from "@/components/study/answer";
import { CardHistory } from "@/components/study/card-history";
import { MyAnswer } from "@/components/study/my-answer";
import { TopicPicker } from "@/components/study/topic-picker";
import { Button, buttonVariants } from "@/components/ui/button";
import { Kbd } from "@/components/ui/kbd";
import { useHotkeys } from "@/hooks/use-hotkeys";
import { scoreTopics } from "@/lib/scorer";
import type { Grade } from "@/lib/types";
import { cn } from "@/lib/utils";
import type { StudyCard } from "@/server/service";

export interface Answered {
	grade: Grade;
	guessed: string[];
	hints: number;
}

const GRADE_ACTIONS: {
	grade: Exclude<Grade, "skip">;
	label: string;
	key: string;
	variant: "outline" | "default";
}[] = [
	{ grade: "again", label: "Visit again", key: "1", variant: "outline" },
	{ grade: "good", label: "Got it", key: "2", variant: "default" },
	{ grade: "less", label: "Visit less often", key: "3", variant: "outline" },
];

function Action({
	label,
	shortcut,
	...props
}: ComponentProps<typeof Button> & { label: string; shortcut: string }) {
	return (
		<Button {...props}>
			{label}
			<Kbd className="hidden sm:inline-flex">{shortcut}</Kbd>
		</Button>
	);
}

/**
 * One problem, sized to the screen: the statement on the left, the guess, hint and answer
 * on the right (one at a time on a phone). Remount it (key by slug) for a fresh guess.
 */
export function Flashcard({
	card,
	topics,
	busy,
	canGoBack,
	onBack,
	onAnswer,
	onSaveNote,
	onClear,
}: {
	card: StudyCard;
	topics: string[];
	busy: boolean;
	canGoBack: boolean;
	onBack: () => void;
	onAnswer: (answer: Answered) => void;
	/** Stores your answer and returns what was kept (null once deleted). */
	onSaveNote: (text: string) => Promise<string | null>;
	/** Deletes this problem's grades; your own answer stays. */
	onClear: () => Promise<void>;
}) {
	const { problem, approach, state } = card;
	const hints = approach?.hints ?? [];
	const [guessed, setGuessed] = useState<string[]>([]);
	const [hintsShown, setHintsShown] = useState(0);
	const [revealed, setRevealed] = useState(false);
	const [pane, setPane] = useState<"problem" | "answer">("problem");
	const [note, setNote] = useState(card.note);
	const [editing, setEditing] = useState(false);

	const toggle = (topic: string) =>
		setGuessed((g) =>
			g.includes(topic) ? g.filter((t) => t !== topic) : [...g, topic],
		);
	const answer = (grade: Grade) =>
		!busy && onAnswer({ grade, guessed, hints: hintsShown });
	const showHint = () => {
		setHintsShown((n) => Math.min(n + 1, hints.length));
		setPane("answer");
	};
	const reveal = () => {
		setRevealed(true);
		setPane("answer");
	};
	const editNote = () => {
		setEditing(true);
		setPane("answer");
	};
	const saveNote = async (text: string) => {
		setNote(await onSaveNote(text));
		setEditing(false);
	};
	const back = () => {
		if (revealed) setRevealed(false);
		else if (canGoBack) onBack();
	};

	useHotkeys({
		b: back,
		m: editNote,
		...(revealed
			? Object.fromEntries(
					GRADE_ACTIONS.map((a) => [a.key, () => answer(a.grade)]),
				)
			: { Enter: reveal, s: () => answer("skip"), h: showHint }),
	});

	return (
		<article
			aria-labelledby="problem-title"
			className="flex h-full min-h-0 flex-col overflow-hidden rounded-sm bg-card text-card-foreground shadow-[0_1px_0_var(--border),0_18px_40px_-24px_rgb(24_33_47/0.45)]"
		>
			<header className="card-margin flex flex-wrap items-center gap-x-3 gap-y-1 px-4 pt-3 pb-2 sm:px-6">
				<h1
					id="problem-title"
					className="mr-auto text-xl leading-tight font-bold tracking-tight sm:text-2xl"
				>
					{problem.title}
				</h1>
				<div className="flex flex-wrap items-center gap-x-3 gap-y-1 text-sm text-muted-foreground">
					<DifficultyBadge difficulty={problem.difficulty} />
					<AskedBadges asked={problem.asked} />
					<CardHistory state={state} />
					{state && (
						<ConfirmClear
							trigger={
								<Button
									variant="ghost"
									size="icon-xs"
									aria-label="Clear progress for this problem"
									title="Clear progress"
								/>
							}
							title={`Clear progress for ${problem.title}?`}
							description="This deletes its grades and takes it off your lists. Your own answer stays."
							onClear={onClear}
						>
							<RotateCcwIcon />
						</ConfirmClear>
					)}
					<a
						href={problem.url}
						target="_blank"
						rel="noreferrer"
						className={cn(
							buttonVariants({ variant: "ghost", size: "xs" }),
							"text-muted-foreground",
						)}
					>
						LeetCode {problem.id}
						<ExternalLinkIcon data-icon="inline-end" />
					</a>
				</div>
			</header>

			<Segmented
				label="Show"
				className="mx-4 mt-2 lg:hidden"
				value={pane}
				onChange={setPane}
				options={[
					{ value: "problem", label: "Problem" },
					{ value: "answer", label: revealed ? "Answer" : "Guess" },
				]}
			/>

			<div className="grid min-h-0 flex-1 lg:grid-cols-[minmax(0,1.45fr)_minmax(0,1fr)]">
				<Pane visible={pane === "problem"} className="px-4 py-3 sm:px-6">
					{problem.description ? (
						<FitPages arrowKeys className="statement h-full">
							<div
								// biome-ignore lint/security/noDangerouslySetInnerHtml: statements are allowlist-sanitized at ingest (src/google/sanitize.py)
								dangerouslySetInnerHTML={{ __html: problem.description }}
							/>
						</FitPages>
					) : (
						<p className="text-muted-foreground">
							This is a LeetCode Premium problem, so its statement is not stored
							here. Open it on LeetCode to read it.
						</p>
					)}
				</Pane>

				<Pane
					visible={pane === "answer"}
					className="gap-3 px-4 py-3 sm:px-6 lg:border-l lg:border-dashed"
				>
					{revealed ? (
						<FitPages>
							<Answer
								result={scoreTopics(guessed, problem.topics)}
								approach={approach}
							/>
						</FitPages>
					) : (
						<>
							<h2 className="font-semibold">Which topics does it use?</h2>
							<TopicPicker
								topics={topics}
								selected={guessed}
								onToggle={toggle}
							/>
							{hintsShown > 0 && (
								<ul className="space-y-1 rounded-md border border-warning/40 bg-warning-wash px-3 py-2 text-sm text-warning">
									{hints.slice(0, hintsShown).map((hint) => (
										<li key={hint} className="flex gap-2">
											<LightbulbIcon className="mt-0.5 size-4 shrink-0" />
											<span>
												<InlineCode text={hint} />
											</span>
										</li>
									))}
								</ul>
							)}
						</>
					)}
					<MyAnswer
						note={note}
						editing={editing}
						onEdit={editNote}
						onSave={saveNote}
						onCancel={() => setEditing(false)}
					/>
				</Pane>
			</div>

			<footer className="flex flex-wrap items-center gap-2 border-t px-4 py-2 sm:px-6">
				<Action
					variant="ghost"
					label="Back"
					shortcut="B"
					onClick={back}
					disabled={(!revealed && !canGoBack) || busy}
				/>
				<Action
					variant="ghost"
					label="My answer"
					shortcut="M"
					onClick={editNote}
					disabled={editing}
				/>
				{revealed ? (
					<div className="ml-auto flex flex-wrap justify-end gap-2">
						{GRADE_ACTIONS.map((a) => (
							<Action
								key={a.grade}
								variant={a.variant}
								label={a.label}
								shortcut={a.key}
								disabled={busy}
								onClick={() => answer(a.grade)}
							/>
						))}
					</div>
				) : (
					<>
						<Action
							variant="ghost"
							label="Skip"
							shortcut="S"
							onClick={() => answer("skip")}
							disabled={busy}
						/>
						<Action
							variant="outline"
							label={
								hints.length > 1
									? `Hint ${Math.min(hintsShown + 1, hints.length)} of ${hints.length}`
									: "Hint"
							}
							shortcut="H"
							onClick={showHint}
							disabled={hintsShown >= hints.length}
						/>
						<Action
							className="ml-auto"
							label="Show answer"
							shortcut="Enter"
							onClick={reveal}
						/>
					</>
				)}
			</footer>
		</article>
	);
}

/** A column on wide screens; on a phone only the chosen pane shows. */
function Pane({
	visible,
	className,
	children,
}: {
	visible: boolean;
	className?: string;
	children: ReactNode;
}) {
	return (
		<div
			className={cn(
				"min-h-0 flex-col lg:flex",
				visible ? "flex" : "hidden",
				className,
			)}
		>
			{children}
		</div>
	);
}
