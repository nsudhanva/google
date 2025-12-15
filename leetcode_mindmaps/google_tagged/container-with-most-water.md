# Container With Most Water

**Problem Link:** [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

**Category:** Google tagged

## Problem Understanding
- Input: Array `height`
- Output: Max area of water. `min(h[i], h[j]) * (j - i)`

## Approach

### Brute Force
- **Idea**: All pairs using nested loops.
- **Complexity**: O(n²). TLE.

### Two Pointers (Greedy)
- **Idea**: Start max width. Shrink width to find higher heights.
- **Algorithm**:
  - `l = 0`, `r = n - 1`
  - `max_area = 0`
  - While `l < r`:
    - `area = min(h[l], h[r]) * (r - l)`
    - `max_area = max(max_area, area)`
    - **Move Logic**: Move the *shorter* line inward.
      - Why? Moving taller line can only decrease width and height (limited by shorter). Moving shorter *might* find a taller line.
- **Complexity**: O(n).

## Implementation
- **Python**:
  ```python
  l, r = 0, len(height) - 1
  max_area = 0
  while l < r:
      max_area = max(max_area, min(height[l], height[r]) * (r - l))
      if height[l] < height[r]: l += 1
      else: r -= 1
  return max_area
  ```

## Complexity Analysis
- **Time**: O(n)
- **Space**: O(1)

## Common Pitfalls
- **Moving logic**: Always move shorter line. If equal, move either (or both).

## Key Patterns
- **Two Pointers**: Shrinking window optimization.
