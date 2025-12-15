# Length of Last Word

**Problem Link:** [Length of Last Word](https://leetcode.com/problems/length-of-last-word/)

**Category:** Google tagged

## Problem Understanding
- Input: String `s` (words and spaces).
- Output: Length of last word.
- Constraints: Ignore trailing spaces.

## Approach

### Reverse Scan
- **Idea**: Start from end. Skip spaces. Count chars until next space or start.
- **Algorithm**:
  - `i = len(s) - 1`
  - While `i >= 0` and `s[i] == ' '`: `i--` (Skip trailing)
  - `length = 0`
  - While `i >= 0` and `s[i] != ' '`:
    - `length++`
    - `i--`
  - Return `length`

### Built-in Split
- **Idea**: `s.split()` handles spaces automatically. Take last element.
- **Code**: `return len(s.split()[-1]) if s.split() else 0`

## Implementation
- **Python**:
  ```python
  i = len(s) - 1
  length = 0
  while i >= 0 and s[i] == ' ':
      i -= 1
  while i >= 0 and s[i] != ' ':
      length += 1
      i -= 1
  return length
  ```

## Complexity Analysis
- **Time**: O(n)
- **Space**: O(1)

## Common Pitfalls
- **Trailing Spaces**: "Hello World   ".
- **Empty String/Spaces Only**: "   ".

## Key Patterns
- **String Parsing**: Reverse iteration.
