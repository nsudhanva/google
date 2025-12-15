# LeetCode Problem Mindmaps

This repository contains **107 LeetCode problems** organized with Mermaid mindmaps to help understand problem-solving approaches.

## 📁 Structure

Mindmaps are organized into 8 categories matching the original Google Sheet tabs:

- **arrays_strings** (1 problem)
- **google_tagged** (51 problems)
- **graphs_trees** (2 problems)
- **hashmaps** (6 problems)
- **heaps** (6 problems)
- **linked_lists** (7 problems)
- **recursion_dp** (23 problems)
- **stacks_queues** (11 problems)

## 🎯 What's in Each Mindmap?

Each `.md` file contains:

- **Problem Link**: Direct link to the LeetCode problem
- **Mermaid Mindmap**: Visual diagram showing problem-solving approach
  - Problem Understanding
  - Approach (Brute Force & Optimization)
  - Implementation Guidelines
  - Complexity Analysis
  - Common Pitfalls
- **Key Insights**: Pattern recognition and strategy tips
- **Things to Remember**: Notes from the original spreadsheet (to be customized)
- **Template Approach**: Step-by-step problem-solving framework

## 🚀 Quick Start

### Viewing Mindmaps

1. **GitHub**: Mindmaps render automatically when viewing `.md` files on GitHub
2. **Local**: Use any Markdown viewer that supports Mermaid (VS Code, Obsidian, etc.)
3. **Online**: Use [Mermaid Live Editor](https://mermaid.live/)

### Example

Check out [`google_tagged/two-sum.md`](leetcode_mindmaps/google_tagged/two-sum.md) for an example mindmap.

## 📝 Customization

These mindmaps are templates! After solving each problem:

1. Update the "Things to Remember" section with specific insights
2. Add problem-specific patterns and edge cases
3. Note optimal time/space complexity
4. Add your solution approach details

## 🔧 Generation Scripts

This repository includes scripts to:

- **`fetch_leetcode_problems.py`**: Extract problems from Google Sheet using Google Sheets API
- **`generate_mindmaps.py`**: Generate Mermaid mindmaps for all problems
- **`update_sheet.py`**: Update Google Sheet with links to mindmap files (TBD)

### Running Scripts

```bash
# Set up environment
uv init
uv add google-api-python-client google-auth-httplib2 google-auth-oauthlib

# Extract problems from Google Sheet
uv run fetch_leetcode_problems.py

# Generate mindmaps
uv run generate_mindmaps.py
```

## 📊 Original Data Source

Data extracted from: [Google Leetcode Spreadsheet](https://docs.google.com/spreadsheets/d/1LL0wiWx8BP6ID_TAa48uTe1rxnp8MZAJxtJU0OMcZaQ/)

## 📄 License

MIT License - feel free to use and customize for your own learning!