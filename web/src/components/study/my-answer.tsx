import { type KeyboardEvent, useState } from "react";
import { Button } from "@/components/ui/button";
import { Kbd } from "@/components/ui/kbd";
import { Textarea } from "@/components/ui/textarea";
import { cn } from "@/lib/utils";

const BOX =
	"shrink-0 rounded-sm border-l-2 border-primary/70 bg-primary/5 px-3 py-2 text-sm";

/**
 * Your answer to the problem, in your own words. Hidden when you have not written one;
 * edited in place. Cmd/Ctrl+Enter saves, Escape cancels.
 */
export function MyAnswer({
	note,
	editing,
	onSave,
	onCancel,
	className,
}: {
	note: string | null;
	editing: boolean;
	onSave: (text: string) => Promise<void>;
	onCancel: () => void;
	className?: string;
}) {
	if (editing)
		return (
			<NoteEditor
				initial={note ?? ""}
				onSave={onSave}
				onCancel={onCancel}
				className={className}
			/>
		);
	if (!note) return null;
	return (
		<section
			aria-labelledby="my-answer-heading"
			className={cn(BOX, "max-h-[40%] overflow-y-auto", className)}
		>
			<h2 id="my-answer-heading" className="font-semibold text-primary">
				My answer
			</h2>
			<p className="whitespace-pre-wrap">{note}</p>
		</section>
	);
}

function NoteEditor({
	initial,
	onSave,
	onCancel,
	className,
}: {
	initial: string;
	onSave: (text: string) => Promise<void>;
	onCancel: () => void;
	className?: string;
}) {
	const [draft, setDraft] = useState(initial);
	const [saving, setSaving] = useState(false);
	const [failed, setFailed] = useState(false);

	async function save() {
		setSaving(true);
		setFailed(false);
		try {
			await onSave(draft);
		} catch {
			setFailed(true);
			setSaving(false);
		}
	}

	function onKeyDown(event: KeyboardEvent) {
		if (event.key === "Escape") onCancel();
		if (event.key === "Enter" && (event.metaKey || event.ctrlKey)) save();
	}

	return (
		<form
			className={cn(BOX, "space-y-2", className)}
			onSubmit={(event) => {
				event.preventDefault();
				save();
			}}
		>
			<label htmlFor="my-answer" className="block font-semibold text-primary">
				My answer
			</label>
			<Textarea
				id="my-answer"
				autoFocus
				value={draft}
				maxLength={4000}
				placeholder="What you understood: the idea, the steps, the catch."
				onChange={(event) => setDraft(event.target.value)}
				onKeyDown={onKeyDown}
				className="max-h-[30vh] min-h-20 bg-card"
			/>
			<div className="flex items-center gap-2">
				<Button type="submit" size="sm" disabled={saving}>
					Save
					<Kbd className="hidden sm:inline-flex">⌘↵</Kbd>
				</Button>
				<Button type="button" size="sm" variant="ghost" onClick={onCancel}>
					Cancel
					<Kbd className="hidden sm:inline-flex">Esc</Kbd>
				</Button>
				{failed && (
					<p role="alert" className="text-destructive">
						Not saved. Try again.
					</p>
				)}
				{!draft.trim() && initial && (
					<p className="text-muted-foreground">Saving empty text deletes it.</p>
				)}
			</div>
		</form>
	);
}
