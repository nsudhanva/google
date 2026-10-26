import { Badge } from "@/components/ui/badge";
import { MASTERY_LABEL, type Mastery } from "@/lib/progress";
import { cn } from "@/lib/utils";

const STYLES: Record<Mastery, string> = {
	new: "border-border bg-transparent text-muted-foreground",
	"needs-work": "bg-destructive-wash text-destructive",
	learning: "bg-secondary text-secondary-foreground",
	mastered: "bg-success-wash text-success",
};

export function MasteryBadge({
	mastery,
	className,
}: {
	mastery: Mastery;
	className?: string;
}) {
	return (
		<Badge variant="outline" className={cn(STYLES[mastery], className)}>
			{MASTERY_LABEL[mastery]}
		</Badge>
	);
}
