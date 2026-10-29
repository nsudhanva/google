/** Renders `backticked` spans of approach text as code. */
export function InlineCode({ text }: { text: string }) {
	return text.split(/(`[^`]+`)/).map((part, i) =>
		part.startsWith("`") && part.endsWith("`") ? (
			// biome-ignore lint/suspicious/noArrayIndexKey: parts of a fixed string never reorder
			<code key={i} className="rounded bg-muted px-1 font-mono text-[0.88em]">
				{part.slice(1, -1)}
			</code>
		) : (
			part
		),
	);
}
