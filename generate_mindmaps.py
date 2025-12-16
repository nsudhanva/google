#!/usr/bin/env python3
"""
Generate markmap-compatible mindmaps for LeetCode problems.
Uses structured data from Google Sheets including:
- Problem name, difficulty, data structure
- Time complexity
- Things to remember (key insights)
- Extra notes
"""

import json
import os
import re
from pathlib import Path


def get_problem_slug(url):
    """Extract the problem slug from LeetCode URL."""
    match = re.search(r"/problems/([\w-]+)/?", url)
    return match.group(1) if match else None


def slug_to_title(slug):
    """Convert slug to title case."""
    return " ".join(word.capitalize() for word in slug.split("-"))


def create_category_dir(sheet_name):
    """Create a sanitized directory name from sheet name."""
    sanitized = re.sub(r"[^\w\s-]", "", sheet_name.lower())
    sanitized = re.sub(r"[\s-]+", "_", sanitized)
    return sanitized


def generate_mindmap(problem):
    """Generate a markmap-compatible mindmap for a single problem."""
    url = problem["url"]
    slug = problem.get("slug") or get_problem_slug(url)
    if not slug:
        return None

    # Use name from sheet, fallback to slug
    title = problem.get("name") or slug_to_title(slug)
    sheet = problem["context"]["sheet"]
    difficulty = problem.get("difficulty") or "Unknown"
    data_structure = problem.get("data_structure") or ""
    time_complexity = problem.get("time_complexity") or "O(?)"
    things_to_remember = problem.get("things_to_remember") or ""
    extra_notes = problem.get("extra_notes") or []
    done = problem.get("done") or ""

    # Build the mindmap content
    mindmap = f"""# {title}

## Problem Info
- **Link**: [{title}]({url})
- **Category**: {sheet}
- **Difficulty**: {difficulty}
- **Status**: {done}

## Approach
"""

    if data_structure:
        mindmap += f"### Data Structure\n- {data_structure}\n\n"
    else:
        mindmap += "### Data Structure\n- *To be determined*\n\n"

    mindmap += f"""### Time Complexity
- {time_complexity}

## Things to Remember
"""

    if things_to_remember and things_to_remember.lower() not in ["things to remember", "revisit", ""]:
        # Split on common delimiters for better formatting
        notes = things_to_remember
        # Handle multiple sentences
        if ". " in notes and len(notes) > 100:
            sentences = [s.strip() for s in notes.split(". ") if s.strip()]
            for sentence in sentences:
                if not sentence.endswith("."):
                    sentence += "."
                mindmap += f"- {sentence}\n"
        else:
            mindmap += f"- {notes}\n"
    else:
        mindmap += "- *Add your key insights after solving*\n"

    # Add extra notes if present
    if extra_notes:
        mindmap += "\n## Additional Notes\n"
        for note in extra_notes:
            if note and note.strip():
                mindmap += f"- {note.strip()}\n"

    return mindmap


def main():
    """Main function to generate all mindmaps."""
    # Load the extracted problems
    with open("leetcode_problems.json", "r") as f:
        problems = json.load(f)

    print(f"Generating mindmaps for {len(problems)} problems...")

    # Create base directory
    base_dir = Path("leetcode_mindmaps")
    base_dir.mkdir(exist_ok=True)

    # Track stats
    created = 0
    skipped = 0
    category_files = {}

    for idx, problem in enumerate(problems, 1):
        # Get problem details
        slug = problem.get("slug") or get_problem_slug(problem["url"])
        if not slug:
            print(f"  Skipping invalid URL: {problem['url']}")
            continue

        # Create category directory
        sheet_name = problem["context"]["sheet"]
        category_dir = create_category_dir(sheet_name)
        full_dir = base_dir / category_dir
        full_dir.mkdir(exist_ok=True)

        # Generate mindmap content
        mindmap_content = generate_mindmap(problem)
        if not mindmap_content:
            continue

        # Save to file
        filename = f"{slug}.md"
        filepath = full_dir / filename

        # Check if file already has custom content (longer than generated)
        if filepath.exists():
            existing_content = filepath.read_text()
            # Skip if existing file has more content (custom additions)
            if len(existing_content) > len(mindmap_content) + 100:
                print(f"  Skipping (has custom content): {filepath}")
                skipped += 1
                continue

        with open(filepath, "w") as f:
            f.write(mindmap_content)
        created += 1

        # Track for summary
        if category_dir not in category_files:
            category_files[category_dir] = []
        category_files[category_dir].append(filename)

        if idx % 20 == 0:
            print(f"  Generated {idx}/{len(problems)}...")

    print(f"\n✓ Created {created} mindmaps, skipped {skipped} with custom content")
    print(f"\nOrganized into {len(category_files)} categories:")
    for category, files in sorted(category_files.items()):
        print(f"  - {category}: {len(files)} problems")

    print(f"\nMindmaps saved to: {base_dir.absolute()}")


if __name__ == "__main__":
    main()
