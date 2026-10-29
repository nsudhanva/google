import { Badge } from "@/components/ui/badge";
import type { Difficulty } from "@/lib/types";
import { cn } from "@/lib/utils";

const TONE: Record<Difficulty, string> = {
	Easy: "bg-success-wash text-success",
	Medium: "bg-warning-wash text-warning",
	Hard: "bg-destructive-wash text-destructive",
};

export function DifficultyBadge({ difficulty }: { difficulty: Difficulty }) {
	return (
		<Badge className={cn("font-semibold", TONE[difficulty])}>
			{difficulty}
		</Badge>
	);
}
