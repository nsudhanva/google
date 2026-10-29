import { ChevronLeftIcon, ChevronRightIcon } from "lucide-react";
import {
	type CSSProperties,
	type ReactNode,
	useLayoutEffect,
	useRef,
	useState,
} from "react";
import { Button } from "@/components/ui/button";
import { useHotkeys } from "@/hooks/use-hotkeys";
import { cn } from "@/lib/utils";

/** Font sizes to try, largest first; below the last one the content pages instead. */
const FONT_SIZES = [15, 14, 13, 12];
const COLUMN_GAP = 32;
const PAGER_HEIGHT = 28;

interface Layout {
	fontSize: number;
	pages: number;
	/** Column width while paged; 0 when everything fits on one page. */
	width: number;
}

/**
 * Fits its content in the box it is given, with no scrolling: it first shrinks the text,
 * then splits the content into side-by-side pages with a pager. With `arrowKeys`, ← and →
 * turn the pages.
 */
export function FitPages({
	children,
	className,
	arrowKeys = false,
}: {
	children: ReactNode;
	className?: string;
	arrowKeys?: boolean;
}) {
	const viewport = useRef<HTMLDivElement>(null);
	const content = useRef<HTMLDivElement>(null);
	const [layout, setLayout] = useState<Layout>({
		fontSize: FONT_SIZES[0],
		pages: 1,
		width: 0,
	});
	const [page, setPage] = useState(0);

	useLayoutEffect(() => {
		const box = viewport.current;
		const inner = content.current;
		if (!box || !inner) return;

		function measure() {
			if (!box || !inner) return;
			const fits = (fontSize: number) => {
				Object.assign(inner.style, {
					fontSize: `${fontSize}px`,
					height: "",
					columnWidth: "",
				});
				return inner.scrollHeight <= box.clientHeight;
			};
			const fontSize = FONT_SIZES.find(fits);
			if (fontSize) {
				setLayout({ fontSize, pages: 1, width: 0 });
				return;
			}
			const smallest = FONT_SIZES[FONT_SIZES.length - 1];
			const width = box.clientWidth;
			Object.assign(inner.style, {
				fontSize: `${smallest}px`,
				height: `${box.clientHeight - PAGER_HEIGHT}px`,
				columnWidth: `${width}px`,
				columnGap: `${COLUMN_GAP}px`,
			});
			const pages = Math.max(
				1,
				Math.round((inner.scrollWidth + COLUMN_GAP) / (width + COLUMN_GAP)),
			);
			setLayout({ fontSize: smallest, pages, width });
			setPage((p) => Math.min(p, pages - 1));
		}

		measure();
		const observer = new ResizeObserver(measure);
		observer.observe(box);
		// Images and fonts load late and change the content height.
		for (const img of inner.querySelectorAll("img")) {
			img.addEventListener("load", measure, { once: true });
		}
		return () => observer.disconnect();
	}, []);

	const paged = layout.pages > 1;
	const turn = (by: number) =>
		setPage((p) => Math.min(layout.pages - 1, Math.max(0, p + by)));
	useHotkeys(
		arrowKeys && paged
			? { ArrowLeft: () => turn(-1), ArrowRight: () => turn(1) }
			: {},
	);

	const style: CSSProperties = paged
		? {
				fontSize: layout.fontSize,
				height: `calc(100% - ${PAGER_HEIGHT}px)`,
				columnWidth: layout.width,
				columnGap: COLUMN_GAP,
				columnFill: "auto",
				transform: `translateX(-${page * (layout.width + COLUMN_GAP)}px)`,
			}
		: { fontSize: layout.fontSize };

	return (
		<div
			ref={viewport}
			className={cn("relative min-h-0 overflow-hidden", className)}
		>
			<div
				ref={content}
				style={style}
				className="transition-transform duration-200 motion-reduce:transition-none"
			>
				{children}
			</div>
			{paged && (
				<div className="absolute right-0 bottom-0 flex h-7 items-center gap-1 bg-card text-xs text-muted-foreground tabular-nums">
					<Button
						variant="ghost"
						size="icon-xs"
						aria-label="Previous page"
						disabled={page === 0}
						onClick={() => turn(-1)}
					>
						<ChevronLeftIcon />
					</Button>
					Page {page + 1} of {layout.pages}
					<Button
						variant="ghost"
						size="icon-xs"
						aria-label="Next page"
						disabled={page === layout.pages - 1}
						onClick={() => turn(1)}
					>
						<ChevronRightIcon />
					</Button>
				</div>
			)}
		</div>
	);
}
