import { NotebookPenIcon } from "lucide-react";
import { type KeyboardEvent, type ReactNode, useState } from "react";
import { Button } from "@/components/ui/button";
import { Kbd } from "@/components/ui/kbd";
import { cn } from "@/lib/utils";

/**
 * Your answer to the problem, in your own words, written on the card's ruled lines.
 * Hidden when you have not written one; edited in place in the same box.
 * Cmd/Ctrl+Enter saves, Escape cancels.
 */
export function MyAnswer({
	note,
	editing,
	onEdit,
	onSave,
	onCancel,
}: {
	note: string | null;
	editing: boolean;
	onEdit: () => void;
	onSave: (text: string) => Promise<void>;
	onCancel: () => void;
}) {
	if (editing)
		return (
			<NoteEditor initial={note ?? ""} onSave={onSave} onCancel={onCancel} />
		);
	if (!note) return null;
	return (
		<NoteBox
			action={
				<Button variant="ghost" size="xs" onClick={onEdit}>
					Edit
					<Kbd className="hidden sm:inline-flex">M</Kbd>
				</Button>
			}
		>
			<p className="card-ruled max-h-[11.9em] overflow-y-auto whitespace-pre-wrap">
				{note}
			</p>
		</NoteBox>
	);
}

function NoteBox({
	action,
	children,
	className,
}: {
	action?: ReactNode;
	children: ReactNode;
	className?: string;
}) {
	return (
		<section
			aria-label="My answer"
			className={cn(
				"shrink-0 rounded-md border border-dashed border-primary/40 px-3 pt-1.5 pb-2 text-sm",
				className,
			)}
		>
			<header className="flex h-6 items-center gap-1.5 text-xs font-medium text-muted-foreground">
				<NotebookPenIcon className="size-3.5 text-primary" aria-hidden />
				My answer
				<span className="ml-auto">{action}</span>
			</header>
			{children}
		</section>
	);
}

function NoteEditor({
	initial,
	onSave,
	onCancel,
}: {
	initial: string;
	onSave: (text: string) => Promise<void>;
	onCancel: () => void;
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
		<NoteBox
			className="border-solid border-primary/70"
			action={
				!draft.trim() && initial && <span>Saving it empty deletes it</span>
			}
		>
			<form
				onSubmit={(event) => {
					event.preventDefault();
					save();
				}}
			>
				<textarea
					aria-label="My answer"
					autoFocus
					value={draft}
					maxLength={4000}
					placeholder="What you understood: the idea, the steps, the catch."
					onChange={(event) => setDraft(event.target.value)}
					onKeyDown={onKeyDown}
					className="card-ruled block field-sizing-content max-h-[11.9em] min-h-[3.4em] w-full resize-none bg-transparent [background-attachment:local] outline-none placeholder:text-muted-foreground"
				/>
				<div className="mt-2 flex items-center gap-2">
					<Button type="submit" size="xs" disabled={saving}>
						Save
						<Kbd className="hidden sm:inline-flex">⌘↵</Kbd>
					</Button>
					<Button type="button" size="xs" variant="ghost" onClick={onCancel}>
						Cancel
						<Kbd className="hidden sm:inline-flex">Esc</Kbd>
					</Button>
					{failed && (
						<p role="alert" className="text-xs text-destructive">
							Not saved. Try again.
						</p>
					)}
				</div>
			</form>
		</NoteBox>
	);
}
