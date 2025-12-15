# Contains Duplicate

**Problem Link:** [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

**Category:** Google tagged

## Problem Understanding
- Input: Array `nums`
- Output: `true` if any value appears at least twice, `false` distinct.

## Approach

### Hash Set
- **Idea**: Track seen elements.
- **Algorithm**:
  - Loop `num` in `nums`:
    - If `num` in `set`: return `True`
    - Add to `set`
  - Return `False`
- **One-liner**: `return len(set(nums)) != len(nums)`

### Sorting
- **Idea**: Sort, then check adjacent.
- **Complexity**: O(n log n). Slower but O(1) space if sort is in-place (usually not for inputs).

## Implementation
- **Python**:
  ```python
  seen = set()
  for n in nums:
      if n in seen: return True
      seen.add(n)
  return False
  ```

## Complexity Analysis
- **Time**: O(n)
- **Space**: O(n)

## Common Pitfalls
- **Time Limit**: Using List instead of Set for lookup (O(n^2)).

## Key Patterns
- **Hash Set**: Usage for uniqueness.
