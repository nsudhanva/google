# LeetCode Problem Mindmaps

Interactive mindmap viewer for LeetCode problems, organized by category with detailed Java solutions.

## 🚀 Quick Start

```bash
# Start local server
python3 -m http.server 8000

# Open in browser
open http://localhost:8000
```

## 📁 Project Structure

```
├── index.html                     # Main viewer (Markmap-based)
├── leetcode_problems.json         # Extracted problems from Google Sheet
├── leetcode_mindmaps/             # Problem-specific mindmap files
│   ├── google_tagged/
│   ├── linked_lists/
│   ├── heaps/
│   ├── stacks_queues/
│   ├── recursion_dp/
│   ├── hashmaps/
│   ├── graphs_trees/
│   └── arrays_strings/
├── fetch_leetcode_problems.py     # Fetches problems from Google Sheet
├── generate_mindmaps.py           # Creates generic mindmap templates
├── generate_specific_mindmaps.py  # Problem-specific Java solutions (Part 1)
└── generate_specific_mindmaps_part2.py  # Problem-specific solutions (Part 2)
```

## 🔄 Updating After Google Sheet Changes

When you add/remove problems in the Google Sheet, run these steps:

### Step 1: Fetch Latest Problems from Sheet
```bash
uv run fetch_leetcode_problems.py
```
This updates `leetcode_problems.json` with the latest problems from all tabs.

### Step 2: Generate Mindmap Folders/Files for New Problems
```bash
uv run generate_mindmaps.py
```
This creates new `.md` files for any new problems (skips existing files).

### Step 3: Add Problem-Specific Content (Optional)
For new problems, add their specific content to either:
- `generate_specific_mindmaps.py` (PROBLEM_CONTENT dict)
- `generate_specific_mindmaps_part2.py` (PROBLEM_CONTENT_2 dict)

Then run:
```bash
uv run generate_specific_mindmaps.py
uv run generate_specific_mindmaps_part2.py
```

### Step 4: Commit and Push
```bash
git add -A
git commit -m "Update mindmaps from Google Sheet"
git push origin main
```

## 🛠️ Full Workflow Summary

```bash
# 1. Fetch latest from sheet
uv run fetch_leetcode_problems.py

# 2. Generate templates for new problems
uv run generate_mindmaps.py

# 3. (Optional) Add specific content to scripts, then:
uv run generate_specific_mindmaps.py
uv run generate_specific_mindmaps_part2.py

# 4. Commit and push
git add -A && git commit -m "Update mindmaps" && git push
```

## 🔐 Google Sheets API Setup

First-time setup only:

1. Enable Google Sheets API in Google Cloud Console
2. Create OAuth 2.0 credentials (Desktop app)
3. Download `credentials.json` to project root
4. Run `uv run fetch_leetcode_problems.py` and complete OAuth flow
5. `token.json` will be created for future use

## 📊 Current Coverage

- **Total Problems**: 103 unique problems
- **Categories**: 8 (Google tagged, Linked Lists, Heaps, Stacks & Queues, etc.)
- **All problems have Java implementations**

## ⌨️ Viewer Features

- **Collapsible nodes**: Click nodes to expand/collapse
- **Expand/Collapse All**: Button in header
- **Search**: Filter problems in sidebar
- **Interactive zoom/pan**: Mouse scroll and drag