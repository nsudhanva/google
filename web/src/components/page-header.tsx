import type { ReactNode } from "react";

export function PageHeader({
	title,
	children,
}: {
	title: string;
	children?: ReactNode;
}) {
	return (
		<header className="mb-8 space-y-2">
			<h1 className="text-3xl font-semibold tracking-tight">{title}</h1>
			{children && (
				<div className="max-w-prose text-muted-foreground">{children}</div>
			)}
		</header>
	);
}
