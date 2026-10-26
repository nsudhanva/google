import { cva } from "class-variance-authority";
import { CheckIcon, XIcon } from "lucide-react";
import { cn } from "@/lib/utils";

export type AnswerState =
	| "idle"
	| "correct"
	| "correct-picked"
	| "incorrect"
	| "dimmed";

const optionVariants = cva(
	"group flex w-full items-start gap-3 rounded-xl border-2 px-4 text-left transition-colors outline-none focus-visible:ring-3 focus-visible:ring-ring/50 disabled:cursor-default",
	{
		variants: {
			state: {
				idle: "border-border bg-card hover:border-ring",
				correct: "border-success bg-success-wash",
				"correct-picked": "border-success bg-success-wash",
				incorrect: "border-destructive bg-destructive-wash",
				dimmed: "border-border bg-card opacity-55",
			},
			layout: {
				list: "py-3.5",
				scale: "py-3 sm:min-h-24 sm:flex-col sm:gap-2",
			},
		},
	},
);

const markerVariants = cva(
	"grid size-6 shrink-0 place-items-center rounded-md text-xs font-bold [&_svg]:size-3.5",
	{
		variants: {
			state: {
				idle: "border text-muted-foreground group-hover:border-ring group-hover:text-ring",
				correct: "bg-success text-background",
				"correct-picked": "bg-success text-background",
				incorrect: "bg-destructive text-background",
				dimmed: "border text-muted-foreground",
			},
		},
	},
);

const TAG: Partial<Record<AnswerState, string>> = {
	correct: "Correct answer",
	"correct-picked": "Your answer: correct",
	incorrect: "Your answer",
};

export function AnswerOption({
	label,
	shortcut,
	state,
	layout,
	onSelect,
}: {
	label: string;
	shortcut: number;
	state: AnswerState;
	layout: "list" | "scale";
	onSelect: () => void;
}) {
	const tag = TAG[state];

	return (
		<button
			type="button"
			onClick={onSelect}
			disabled={state !== "idle"}
			aria-label={tag ? `${label}. ${tag}` : `${shortcut}. ${label}`}
			className={optionVariants({ state, layout })}
		>
			<span aria-hidden className={markerVariants({ state })}>
				{state === "correct" || state === "correct-picked" ? (
					<CheckIcon />
				) : state === "incorrect" ? (
					<XIcon />
				) : (
					shortcut
				)}
			</span>
			<span className="flex flex-col gap-0.5">
				<span
					className={cn(
						layout === "scale" ? "font-medium" : "text-[1.05rem] leading-snug",
					)}
				>
					{label}
				</span>
				{tag && (
					<span
						className={cn(
							"text-sm font-semibold",
							state === "incorrect" ? "text-destructive" : "text-success",
						)}
					>
						{tag}
					</span>
				)}
			</span>
		</button>
	);
}
