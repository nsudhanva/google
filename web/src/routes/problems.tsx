import { createFileRoute, Link, useRouter } from "@tanstack/react-router";
import {
	ChevronLeftIcon,
	ChevronRightIcon,
	LockIcon,
	RotateCcwIcon,
	SearchIcon,
} from "lucide-react";
import { useRef, useState } from "react";
import { DifficultyBadge } from "@/components/difficulty-badge";
import { ListBadge } from "@/components/list-badge";
import { PageHeader } from "@/components/page-header";
import { Segmented } from "@/components/segmented";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import {
	Table,
	TableBody,
	TableCell,
	TableHead,
	TableHeader,
	TableRow,
} from "@/components/ui/table";
import { useFitCount } from "@/hooks/use-fit-count";
import { useHotkeys } from "@/hooks/use-hotkeys";
import { useSearch } from "@/hooks/use-search";
import { percent, timeFrom } from "@/lib/format";
import { PERIOD_LABEL, PERIODS, type Period } from "@/lib/types";
import { listProblems, resetProgress } from "@/server/functions";
import type { ProblemRow } from "@/server/service";

export const Route = createFileRoute("/problems")({
	head: () => ({ meta: [{ title: "Problems | Google LeetCode cards" }] }),
	loader: () => listProblems(),
	component: Problems,
});

const ROW_HEIGHT = 37;
/** Enough for every problem, so the pager counts all matches. */
const SEARCH_LIMIT = 1000;

const PERIOD_OPTIONS = PERIODS.map((value) => ({
	value,
	label: PERIOD_LABEL[value],
}));

function statusText(row: ProblemRow): string {
	if (row.status === "new") return "";
	if (row.status === "due" || row.due === null) return "Due now";
	return `Due ${timeFrom(row.due)}`;
}

function Problems() {
	const rows = Route.useLoaderData();
	const router = useRouter();
	const [query, setQuery] = useState("");
	const [period, setPeriod] = useState<Period>("6m");
	const [page, setPage] = useState(0);
	const tableArea = useRef<HTMLDivElement>(null);
	// One row of the box holds the table header.
	const pageSize = useFitCount(tableArea, ROW_HEIGHT) - 1;

	const hits = useSearch(query, SEARCH_LIMIT);
	// Only problems asked in the chosen period, in that period's frequency order.
	const inPeriod = rows
		.filter((r) => r.asked[period])
		.sort(
			(a, b) => (a.asked[period]?.rank ?? 0) - (b.asked[period]?.rank ?? 0),
		);
	const bySlug = new Map(inPeriod.map((r) => [r.slug, r]));
	const results = query.trim()
		? hits.flatMap((hit) => {
				const row = bySlug.get(hit.slug);
				return row ? [{ row, snippet: hit.snippet }] : [];
			})
		: inPeriod.map((row) => ({ row, snippet: null }));

	const pages = Math.max(1, Math.ceil(results.length / pageSize));
	const current = Math.min(page, pages - 1);
	const visible = results.slice(current * pageSize, (current + 1) * pageSize);
	const turn = (by: number) =>
		setPage(Math.min(pages - 1, Math.max(0, current + by)));
	useHotkeys({ ArrowLeft: () => turn(-1), ArrowRight: () => turn(1) });

	async function reset(slug: string) {
		await resetProgress({ data: { slug } });
		await router.invalidate();
	}

	return (
		<div className="flex h-full min-h-0 flex-col">
			<PageHeader
				title="Problems"
				actions={
					<div className="flex w-full flex-wrap items-center gap-2 sm:w-auto">
						<Segmented
							label="Asked in"
							value={period}
							options={PERIOD_OPTIONS}
							onChange={(next) => {
								setPeriod(next);
								setPage(0);
							}}
						/>
						<div className="relative w-full sm:w-72">
							<SearchIcon
								className="pointer-events-none absolute top-1/2 left-2.5 size-4 -translate-y-1/2 text-muted-foreground"
								aria-hidden
							/>
							<Input
								value={query}
								onChange={(e) => {
									setQuery(e.target.value);
									setPage(0);
								}}
								placeholder="Number, title, topic, or problem text"
								aria-label="Search problems"
								className="bg-card pl-8"
							/>
						</div>
					</div>
				}
			>
				{inPeriod.length} problems Google asked in the last{" "}
				{PERIOD_LABEL[period]}, most frequent first. Topics stay hidden unless
				you search for one.
			</PageHeader>

			<div
				ref={tableArea}
				className="min-h-0 flex-1 overflow-hidden rounded-sm bg-card shadow-[0_1px_0_var(--border)]"
			>
				<Table>
					<TableHeader>
						<TableRow>
							<TableHead className="w-12 text-right">Rank</TableHead>
							<TableHead className="hidden w-14 text-right sm:table-cell">
								Freq.
							</TableHead>
							<TableHead className="w-16">LC</TableHead>
							<TableHead>Problem</TableHead>
							<TableHead className="hidden sm:table-cell">Difficulty</TableHead>
							<TableHead className="hidden md:table-cell">Status</TableHead>
							<TableHead className="hidden text-right md:table-cell">
								Last topics
							</TableHead>
							<TableHead className="w-10">
								<span className="sr-only">Clear progress</span>
							</TableHead>
						</TableRow>
					</TableHeader>
					<TableBody>
						{visible.map(({ row, snippet }) => (
							<TableRow key={row.slug} className="h-[37px]">
								<TableCell className="text-right text-muted-foreground tabular-nums">
									{row.asked[period]?.rank}
								</TableCell>
								<TableCell className="hidden text-right text-muted-foreground tabular-nums sm:table-cell">
									{Math.round(row.asked[period]?.frequency ?? 0)}
								</TableCell>
								<TableCell className="text-muted-foreground tabular-nums">
									{row.id}
								</TableCell>
								<TableCell className="w-full max-w-0">
									<Link
										to="/"
										search={{ set: "all", slug: row.slug }}
										className="flex items-baseline gap-2 font-medium hover:text-primary hover:underline"
									>
										<span className="max-w-full shrink-0 truncate">
											{row.title}
										</span>
										{row.premium && (
											<LockIcon
												className="size-3.5 shrink-0 self-center text-muted-foreground"
												aria-label="Premium"
											/>
										)}
										{snippet && (
											<span className="hidden min-w-0 truncate text-xs font-normal text-muted-foreground md:inline">
												{snippet}
											</span>
										)}
									</Link>
								</TableCell>
								<TableCell className="hidden sm:table-cell">
									<DifficultyBadge difficulty={row.difficulty} />
								</TableCell>
								<TableCell className="hidden md:table-cell">
									<div className="flex items-center gap-2 text-muted-foreground">
										<ListBadge list={row.list} />
										{statusText(row)}
									</div>
								</TableCell>
								<TableCell className="hidden text-right tabular-nums md:table-cell">
									{row.lastScore === null ? "—" : percent(row.lastScore)}
								</TableCell>
								<TableCell>
									{row.lastAt && (
										<Button
											variant="ghost"
											size="icon-xs"
											aria-label={`Clear progress for ${row.title}`}
											title="Clear progress"
											onClick={() => reset(row.slug)}
										>
											<RotateCcwIcon />
										</Button>
									)}
								</TableCell>
							</TableRow>
						))}
					</TableBody>
				</Table>
				{visible.length === 0 && (
					<p className="px-4 py-8 text-center text-muted-foreground">
						No problem matches “{query}”.
					</p>
				)}
			</div>

			<nav
				aria-label="Pages"
				className="flex items-center justify-end gap-2 pt-2 text-sm text-muted-foreground tabular-nums"
			>
				{results.length > 0 &&
					`${current * pageSize + 1}–${current * pageSize + visible.length} of ${results.length}`}
				<Button
					variant="ghost"
					size="icon-sm"
					aria-label="Previous page"
					disabled={current === 0}
					onClick={() => turn(-1)}
				>
					<ChevronLeftIcon />
				</Button>
				<Button
					variant="ghost"
					size="icon-sm"
					aria-label="Next page"
					disabled={current >= pages - 1}
					onClick={() => turn(1)}
				>
					<ChevronRightIcon />
				</Button>
			</nav>
		</div>
	);
}
