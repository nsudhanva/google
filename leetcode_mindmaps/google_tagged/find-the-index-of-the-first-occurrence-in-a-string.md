# Find the Index of the First Occurrence in a String

**Problem Link:** [Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

**Category:** Google tagged

## Problem Understanding
- Input: `haystack`, `needle`
- Output: First index of `needle` in `haystack`, or -1.

## Approach

### Sliding Window (Brute Force)
- **Idea**: Check every substring of length `m`.
- **Complexity**: O((n-m)*m).

### Built-in
- **Idea**: `haystack.find(needle)`
- **Complexity**: Usually O(n+m) optimized.

### KMP (Knuth-Morris-Pratt)
- **Idea**: Preprocess `needle` to know how much to skip on mismatch.
- **LPS Array**: Longest Prefix Suffix.
- **Complexity**: O(n + m).

## Implementation (Sliding Window)
- **Python**:
  ```python
  if not needle: return 0
  for i in range(len(haystack) - len(needle) + 1):
      if haystack[i:i+len(needle)] == needle:
          return i
  return -1
  ```

## Complexity Analysis
- **Time**: O(n * m) worst case
- **Space**: O(1)

## Common Pitfalls
- **Empty Needle**: Should return 0.
- **Index Range**: `range` limit.

## Key Patterns
- **String Matching**: Sliding window or KMP for optimization.
