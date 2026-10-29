import type { ReactNode } from "react";

/** Compact page title with an optional one-line description and actions on the right. */
export function PageHeader({
	title,
	children,
	actions,
}: {
	title: string;
	children?: ReactNode;
	actions?: ReactNode;
}) {
	return (
		<header className="mb-3 flex flex-wrap items-end gap-x-4 gap-y-2">
			<div className="min-w-0 flex-1">
				<h1 className="text-2xl font-semibold tracking-tight">{title}</h1>
				{children && (
					<p className="max-w-prose text-sm text-muted-foreground">
						{children}
					</p>
				)}
			</div>
			{actions}
		</header>
	);
}
