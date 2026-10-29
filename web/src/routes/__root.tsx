import { TanStackDevtools } from "@tanstack/react-devtools";
import {
	createRootRoute,
	HeadContent,
	Link,
	Scripts,
} from "@tanstack/react-router";
import { TanStackRouterDevtoolsPanel } from "@tanstack/react-router-devtools";
import type { ReactNode } from "react";
import { SiteHeader } from "@/components/site-header";
import { ThemeProvider } from "@/components/theme-provider";
import { buttonVariants } from "@/components/ui/button";
import { getReadiness } from "@/server/functions";
import appCss from "../styles.css?url";

export const Route = createRootRoute({
	loader: () => getReadiness(),
	head: () => ({
		meta: [
			{ charSet: "utf-8" },
			{ name: "viewport", content: "width=device-width, initial-scale=1" },
			{ title: "Google LeetCode cards" },
			{
				name: "description",
				content:
					"Flashcards for the LeetCode problems Google asked in the last six months.",
			},
		],
		links: [{ rel: "stylesheet", href: appCss }],
	}),
	shellComponent: RootDocument,
	notFoundComponent: NotFound,
});

function RootDocument({ children }: { children: ReactNode }) {
	const data = Route.useLoaderData();
	return (
		// The theme script sets the `dark` class before hydration.
		<html lang="en" suppressHydrationWarning>
			<head>
				<HeadContent />
			</head>
			<body>
				<ThemeProvider>
					<SiteHeader readiness={data ?? 0} />
					{/* Every page fits the screen below the 3rem header; overflow scrolls only on very small screens. */}
					<main className="mx-auto flex h-[calc(100dvh-3rem)] w-full max-w-7xl flex-col overflow-y-auto px-3 py-3 sm:px-5">
						{children}
					</main>
				</ThemeProvider>
				<TanStackDevtools
					config={{ position: "bottom-right" }}
					plugins={[
						{
							name: "TanStack Router",
							render: <TanStackRouterDevtoolsPanel />,
						},
					]}
				/>
				<Scripts />
			</body>
		</html>
	);
}

function NotFound() {
	return (
		<div className="space-y-4">
			<h1 className="text-3xl font-semibold tracking-tight">Page not found</h1>
			<p className="text-muted-foreground">That page doesn't exist.</p>
			<Link to="/" className={buttonVariants()}>
				Go to study
			</Link>
		</div>
	);
}
