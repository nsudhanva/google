#!/usr/bin/env python3
"""
Generate Mermaid mindmaps for LeetCode problems.
"""

import json
import os
import re
from pathlib import Path
from urllib.parse import urlparse


def get_problem_slug(url):
    """Extract the problem slug from LeetCode URL."""
    # Extract the problem slug from URLs like:
    # https://leetcode.com/problems/two-sum/description/
    # https://leetcode.com/problems/two-sum/
    match = re.search(r"/problems/([\w-]+)/?", url)
    return match.group(1) if match else None


def slug_to_title(slug):
    """Convert slug to title case."""
    return " ".join(word.capitalize() for word in slug.split("-"))


def create_category_dir(sheet_name):
    """Create a sanitized directory name from sheet name."""
    # Remove special characters and convert to lowercase with underscores
    sanitized = re.sub(r"[^\w\s-]", "", sheet_name.lower())
    sanitized = re.sub(r"[\s-]+", "_", sanitized)
    return sanitized


def generate_mindmap(problem):
    """Generate a Mermaid mindmap for a single problem."""
    url = problem["url"]
    slug = get_problem_slug(url)
    if not slug:
        return None

    title = problem.get("title") or slug_to_title(slug)
    sheet = problem["context"]["sheet"]
    notes = problem.get("notes", "")

    # Create the mindmap structure
    mindmap = f"""# {title}

**Problem Link:** [{title}]({url})

**Category:** {sheet}

## Problem-Solving Mindmap

```mermaid
mindmap
  root(({title}))
    Problem Understanding
      Read carefully
      Identify inputs/outputs
      Note constraints
      Ask clarifying questions
    Approach
      Brute Force
        Think simple first
        Analyze complexity
      Optimization
        Look for patterns
        Consider data structures
        Think about edge cases
    Implementation
      Write clean code
      Handle edge cases
      Test with examples
    Complexity Analysis
      Time complexity
      Space complexity
    Common Pitfalls
      Off-by-one errors
      Edge cases
      Integer overflow
```

## Key Insights

- **Pattern Recognition**: Identify the problem type (array, string, tree, graph, DP, etc.)
- **Data Structure Choice**: Choose the right data structure for optimal solution
- **Algorithm Strategy**: Greedy, two-pointers, sliding window, DFS/BFS, dynamic programming, etc.

## Things to Remember
"""

    if notes and notes != "Things to remember":
        mindmap += f"\n{notes}\n"
    else:
        mindmap += "\n*Add your notes after solving the problem*\n"

    mindmap += f"""
## Template Approach

1. **Understand**: Read the problem and examples
2. **Plan**: Choose approach and data structures  
3. **Code**: Implement solution
4. **Test**: Verify with test cases
5. **Optimize**: Improve time/space complexity if needed

---

*This mindmap was auto-generated. Update it with problem-specific insights after solving.*
"""

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

    # Track created files per category
    category_files = {}

    for idx, problem in enumerate(problems, 1):
        # Get problem details
        slug = get_problem_slug(problem["url"])
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

        # Skip if file already exists (don't overwrite problem-specific content)
        if filepath.exists():
            print(f"  Skipping existing: {filepath}")
            continue

        with open(filepath, "w") as f:
            f.write(mindmap_content)

        # Track for summary
        if category_dir not in category_files:
            category_files[category_dir] = []
        category_files[category_dir].append(filename)

        if idx % 10 == 0:
            print(f"  Generated {idx}/{len(problems)}...")

    print(f"\n✓ Successfully generated {len(problems)} mindmaps!")
    print(f"\nOrganized into {len(category_files)} categories:")
    for category, files in sorted(category_files.items()):
        print(f"  - {category}: {len(files)} problems")

    print(f"\nMindmaps saved to: {base_dir.absolute()}")


if __name__ == "__main__":
    main()
