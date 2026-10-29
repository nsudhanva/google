import type { ErrorComponentProps } from "@tanstack/react-router";
import { Button } from "@/components/ui/button";

/** Browsers word a missing code file differently; all of them mean the app was updated. */
const STALE_BUILD =
	/dynamically imported module|Importing a module script failed|module script/i;

/**
 * Shown when a page fails to load. After a deploy, a tab opened earlier asks for code files
 * the new version no longer has; the router reloads once, and this covers the rest.
 */
export function RouteError({ error }: ErrorComponentProps) {
	const message = error instanceof Error ? error.message : String(error);
	const stale = STALE_BUILD.test(message);
	return (
		<div className="mx-auto mt-6 max-w-md rounded-sm border border-dashed bg-card/60 px-6 py-14 text-center">
			<h1 className="text-2xl font-semibold tracking-tight">
				{stale ? "The app was updated" : "This page did not load"}
			</h1>
			<p className="mt-2 text-muted-foreground">
				{stale
					? "Reload to get the new version. Your progress and notes are saved on the server."
					: message}
			</p>
			<Button className="mt-6" onClick={() => window.location.reload()}>
				Reload
			</Button>
		</div>
	);
}
