import { createFileRoute } from "@tanstack/react-router";
import { PageHeader } from "@/components/page-header";
import { Separator } from "@/components/ui/separator";
import { SOURCES } from "@/data/sources";

export const Route = createFileRoute("/about")({
	head: () => ({ meta: [{ title: "About | GHA practice" }] }),
	component: AboutPage,
});

function AboutPage() {
	return (
		<article className="max-w-prose">
			<PageHeader title="About">
				Practice for the Google Hiring Assessment, a non-coding workstyle test
				given before interviews.
			</PageHeader>

			<div className="space-y-4 leading-relaxed">
				<h2 className="text-xl font-semibold tracking-tight">
					Where the questions come from
				</h2>
				<p>
					Real GHA items are rarely posted verbatim. This bank combines the few
					quoted items, the examples passers gave, prep-site scenarios and the
					documented format. Every question shows its source after you answer,
					so you can tell a quoted item from a reconstruction.
				</p>
				<p>
					For many scenarios only the Most and Least answers were reported. The
					other options were written to match the reported format and are marked
					as reconstructed.
				</p>

				<h2 className="pt-4 text-xl font-semibold tracking-tight">
					What the answers are based on
				</h2>
				<ul className="list-disc space-y-1.5 pl-5">
					<li>
						Pick one persona before you start and keep it across reshuffled
						triples.
					</li>
					<li>
						Answer statements at the extremes, and watch for absolutes and
						reworded twins.
					</li>
					<li>
						In scenarios, the Most Likely pick follows policy, even at the cost
						of a deadline. The Least Likely pick is the shortcut that comes with
						an excuse.
					</li>
				</ul>
				<p className="text-muted-foreground">
					That's the consensus from passer reports, not a guarantee. Some
					candidates failed following it.
				</p>
			</div>

			<Separator className="my-10" />

			<h2 className="mb-4 text-xl font-semibold tracking-tight">Sources</h2>
			<ol className="list-decimal space-y-2 pl-5 text-sm">
				{SOURCES.map((s) => (
					<li key={s.url}>
						<a
							href={s.url}
							target="_blank"
							rel="noreferrer"
							className="underline-offset-4 hover:underline"
						>
							{s.title}
						</a>
					</li>
				))}
			</ol>
		</article>
	);
}
