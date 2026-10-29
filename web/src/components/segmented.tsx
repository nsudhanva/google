import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group";

/** A small one-of-N switch; clicking the active option keeps it selected. */
export function Segmented<T extends string>({
	label,
	value,
	options,
	onChange,
	className,
}: {
	label: string;
	value: T;
	options: { value: T; label: string }[];
	onChange: (value: T) => void;
	className?: string;
}) {
	return (
		<ToggleGroup
			aria-label={label}
			variant="outline"
			size="sm"
			className={className}
			value={[value]}
			onValueChange={(next) => {
				const picked = options.find((o) => o.value === next[0]);
				if (picked) onChange(picked.value);
			}}
		>
			{options.map((o) => (
				<ToggleGroupItem key={o.value} value={o.value}>
					{o.label}
				</ToggleGroupItem>
			))}
		</ToggleGroup>
	);
}
