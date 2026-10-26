import { CircleCheckIcon, CircleXIcon } from "lucide-react";
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert";
import { cn } from "@/lib/utils";

export function AnswerFeedback({
	correct,
	why,
}: {
	correct: boolean;
	why: string;
}) {
	const Icon = correct ? CircleCheckIcon : CircleXIcon;
	return (
		<Alert
			aria-live="polite"
			className={cn(
				"mt-4 animate-in border-l-4 px-4 py-3 text-base fade-in-0 slide-in-from-top-1 motion-reduce:animate-none",
				correct
					? "border-success/40 border-l-success bg-success-wash"
					: "border-destructive/40 border-l-destructive bg-destructive-wash",
			)}
		>
			<Icon className={correct ? "text-success" : "text-destructive"} />
			<AlertTitle
				className={cn(
					"font-bold",
					correct ? "text-success" : "text-destructive",
				)}
			>
				{correct ? "Correct" : "Not quite"}
			</AlertTitle>
			<AlertDescription className="text-base leading-relaxed text-foreground">
				{why}
			</AlertDescription>
		</Alert>
	);
}
