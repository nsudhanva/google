"""Build data/problems.json from the Google company lists and doocs/leetcode statements.

The CSVs (liquidslr/leetcode-company-wise-problems) give, for the last 30 days, 3 months and
6 months, which problems Google asked, in frequency order, with their topics. The 6-month list
is the full set; the shorter periods are subsets of it.
doocs/leetcode (CC BY-SA 4.0) gives the problem statement. Premium problems keep no statement:
the app links to LeetCode for those.
"""

import csv
import io
import json
import re
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from pathlib import Path

from google.sanitize import sanitize_html

LIST_URL = "https://raw.githubusercontent.com/liquidslr/leetcode-company-wise-problems/main/Google"
# Period key -> CSV file name in the company folder. The last one is the full problem set.
PERIODS = {
    "30d": "1.%20Thirty%20Days.csv",
    "3m": "2.%20Three%20Months.csv",
    "6m": "3.%20Six%20Months.csv",
}
DOOCS_RAW = "https://raw.githubusercontent.com/doocs/leetcode/main"
DOOCS_INDEX = f"{DOOCS_RAW}/solution/README_EN.md"

DATA_DIR = Path("data")
CACHE_DIR = DATA_DIR / ".cache"
PROBLEMS_PATH = DATA_DIR / "problems.json"

DESCRIPTION = re.compile(r"<!-- description:start -->(.*?)<!-- description:end -->", re.S)
INDEX_LINK = re.compile(r"\[(.+)\]\((/solution/.+)\)")


@dataclass(frozen=True)
class DoocsEntry:
    id: int
    path: str
    premium: bool


@dataclass(frozen=True)
class Asked:
    rank: int
    frequency: float


@dataclass(frozen=True)
class Problem:
    id: int
    slug: str
    title: str
    difficulty: str
    # Rank and frequency for each period in which Google asked the problem.
    asked: dict[str, Asked]
    url: str
    topics: list[str]
    premium: bool
    description: str | None


def title_key(title: str) -> str:
    return re.sub(r"[^a-z0-9]", "", title.lower())


def fetch(url: str, cache_name: str) -> str:
    """GET a URL once; later runs read the cached copy."""
    path = CACHE_DIR / cache_name
    if path.exists():
        return path.read_text()
    with urllib.request.urlopen(url, timeout=60) as response:
        text = response.read().decode()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    return text


def parse_doocs_index(markdown: str) -> dict[str, DoocsEntry]:
    entries: dict[str, DoocsEntry] = {}
    for line in markdown.splitlines():
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 5 or not cells[0].isdigit():
            continue
        if link := INDEX_LINK.match(cells[1]):
            title, path = link.groups()
            entries[title_key(title)] = DoocsEntry(int(cells[0]), path, "🔒" in cells[-1])
    return entries


def readme(entry: DoocsEntry) -> str:
    return fetch(f"{DOOCS_RAW}{entry.path}", f"doocs/{entry.id:04d}.md")


def description(entry: DoocsEntry) -> str | None:
    if entry.premium:
        return None
    match = DESCRIPTION.search(readme(entry))
    return sanitize_html(match.group(1)) if match else None


def slug_from_url(url: str) -> str:
    return urllib.parse.urlparse(url).path.rstrip("/").rsplit("/", 1)[-1]


def period_rows(period: str) -> list[dict[str, str]]:
    text = fetch(f"{LIST_URL}/{PERIODS[period]}", f"google-{period}.csv")
    return list(csv.DictReader(io.StringIO(text)))


def asked_by_slug() -> dict[str, dict[str, Asked]]:
    asked: dict[str, dict[str, Asked]] = {}
    for period in PERIODS:
        for rank, row in enumerate(period_rows(period), 1):
            stat = Asked(rank=rank, frequency=float(row["Frequency"]))
            asked.setdefault(slug_from_url(row["Link"]), {})[period] = stat
    return asked


def build_problems() -> list[Problem]:
    rows = period_rows(list(PERIODS)[-1])
    asked = asked_by_slug()
    index = parse_doocs_index(fetch(DOOCS_INDEX, "doocs-index.md"))

    missing = [row["Title"] for row in rows if title_key(row["Title"]) not in index]
    if missing:
        raise SystemExit(f"No doocs entry for: {missing}")

    entries = [index[title_key(row["Title"])] for row in rows]
    with ThreadPoolExecutor(max_workers=8) as pool:
        descriptions = list(pool.map(description, entries))

    return [
        Problem(
            id=entry.id,
            slug=slug_from_url(row["Link"]),
            title=row["Title"].strip(),
            difficulty=row["Difficulty"].capitalize(),
            asked=asked[slug_from_url(row["Link"])],
            url=row["Link"],
            topics=[topic.strip() for topic in row["Topics"].split(",") if topic.strip()],
            premium=entry.premium,
            description=text,
        )
        for row, entry, text in zip(rows, entries, descriptions, strict=True)
    ]


def ingest() -> None:
    problems = build_problems()
    document = {
        "sources": {
            "lists": {period: f"{LIST_URL}/{name}" for period, name in PERIODS.items()},
            "statements": "https://github.com/doocs/leetcode (CC BY-SA 4.0)",
            "fetchedAt": datetime.now(UTC).date().isoformat(),
        },
        "problems": [asdict(problem) for problem in problems],
    }
    PROBLEMS_PATH.write_text(json.dumps(document, indent=1, ensure_ascii=False) + "\n")
    premium = sum(problem.premium for problem in problems)
    print(f"Wrote {len(problems)} problems ({premium} premium) to {PROBLEMS_PATH}")
