"""Build data/problems.json from the Google six-month list and doocs/leetcode statements.

The CSV (liquidslr/leetcode-company-wise-problems) gives rank order, frequency and topics.
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

CSV_URL = (
    "https://raw.githubusercontent.com/liquidslr/leetcode-company-wise-problems/main/"
    "Google/3.%20Six%20Months.csv"
)
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
class Problem:
    rank: int
    id: int
    slug: str
    title: str
    difficulty: str
    frequency: float
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


def build_problems() -> list[Problem]:
    rows = list(csv.DictReader(io.StringIO(fetch(CSV_URL, "google-six-months.csv"))))
    index = parse_doocs_index(fetch(DOOCS_INDEX, "doocs-index.md"))

    missing = [row["Title"] for row in rows if title_key(row["Title"]) not in index]
    if missing:
        raise SystemExit(f"No doocs entry for: {missing}")

    entries = [index[title_key(row["Title"])] for row in rows]
    with ThreadPoolExecutor(max_workers=8) as pool:
        descriptions = list(pool.map(description, entries))

    return [
        Problem(
            rank=rank,
            id=entry.id,
            slug=slug_from_url(row["Link"]),
            title=row["Title"].strip(),
            difficulty=row["Difficulty"].capitalize(),
            frequency=float(row["Frequency"]),
            url=row["Link"],
            topics=[topic.strip() for topic in row["Topics"].split(",") if topic.strip()],
            premium=entry.premium,
            description=text,
        )
        for rank, (row, entry, text) in enumerate(zip(rows, entries, descriptions, strict=True), 1)
    ]


def ingest() -> None:
    problems = build_problems()
    document = {
        "sources": {
            "list": CSV_URL,
            "statements": "https://github.com/doocs/leetcode (CC BY-SA 4.0)",
            "fetchedAt": datetime.now(UTC).date().isoformat(),
        },
        "problems": [asdict(problem) for problem in problems],
    }
    PROBLEMS_PATH.write_text(json.dumps(document, indent=1, ensure_ascii=False) + "\n")
    premium = sum(problem.premium for problem in problems)
    print(f"Wrote {len(problems)} problems ({premium} premium) to {PROBLEMS_PATH}")
