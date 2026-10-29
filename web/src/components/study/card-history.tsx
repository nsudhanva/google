import { ListBadge } from "@/components/list-badge";
import { percent, timeFrom } from "@/lib/format";
import type { CardState } from "@/lib/scheduler";

export function CardHistory({ state }: { state: CardState | null }) {
	if (!state?.reviews) return <span>{state ? "Skipped earlier" : "New"}</span>;
	return (
		<>
			<span>
				Seen {state.reviews} {state.reviews === 1 ? "time" : "times"}, last{" "}
				{timeFrom(state.lastAt)}
				{state.lastScore !== null && `, topics ${percent(state.lastScore)}`}
			</span>
			<ListBadge list={state.list} />
		</>
	);
}
