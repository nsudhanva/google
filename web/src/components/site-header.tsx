import { ClientOnly, Link, type LinkProps } from "@tanstack/react-router";
import { ListChecksIcon } from "lucide-react";
import { ModeToggle } from "@/components/mode-toggle";
import { buttonVariants } from "@/components/ui/button";
import { QUESTIONS } from "@/data/gha";
import { summarize } from "@/lib/progress";
import { useProgress } from "@/lib/progress-store";
import { cn } from "@/lib/utils";

const NAV: { to: LinkProps["to"]; label: string; exact?: boolean }[] = [
	{ to: "/", label: "Practice", exact: true },
	{ to: "/progress", label: "Progress" },
	{ to: "/about", label: "About" },
];

export function SiteHeader() {
	return (
		<header className="sticky top-0 z-40 border-b bg-background/85 backdrop-blur supports-[backdrop-filter]:bg-background/70">
			<div className="mx-auto flex h-14 max-w-3xl items-center gap-2 px-4 sm:px-6">
				<Link
					to="/"
					search={{}}
					className="mr-2 flex items-center gap-2 font-bold tracking-tight"
					aria-label="GHA practice home"
				>
					<ListChecksIcon className="size-5" aria-hidden />
					<span className="hidden sm:inline">GHA practice</span>
				</Link>
				<nav aria-label="Main" className="flex items-center gap-0.5">
					{NAV.map(({ to, label, exact }) => (
						<Link
							key={label}
							to={to}
							activeOptions={{ exact, includeSearch: false }}
							className={cn(
								buttonVariants({ variant: "ghost", size: "sm" }),
								"text-muted-foreground data-[status=active]:bg-muted data-[status=active]:text-foreground",
							)}
						>
							{label}
						</Link>
					))}
				</nav>
				<div className="ml-auto flex items-center gap-1">
					<ClientOnly>
						<MasteredCount />
					</ClientOnly>
					<ModeToggle />
				</div>
			</div>
		</header>
	);
}

function MasteredCount() {
	const { mastered, total } = summarize(QUESTIONS, useProgress());
	return (
		<Link
			to="/progress"
			className="hidden rounded-md px-2 py-1 text-sm text-muted-foreground tabular-nums hover:text-foreground sm:block"
		>
			{mastered}/{total} mastered
		</Link>
	);
}
