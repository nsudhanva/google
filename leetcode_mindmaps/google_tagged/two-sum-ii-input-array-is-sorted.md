# Two Sum II - Input Array Is Sorted

**Problem Link:** [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

**Category:** Google tagged

## Problem Understanding
- Input: Sorted array `numbers`, target.
- Output: Indices (1-based) adding to target.
- Constraint: Constant space O(1).

## Approach

### Hash Map
- **Idea**: Same as Two Sum I.
- **Space**: O(n). Fails constraint.

### Binary Search
- **Idea**: For each element, search remainder.
- **Time**: O(n log n). Slower than O(n).

### Two Pointers (Optimal)
- **Idea**: Start `l`, `r` at ends.
- **Algorithm**:
  - Sum = `nums[l] + nums[r]`
  - If `sum == target`: return `[l+1, r+1]`
  - If `sum < target`: `l++` (Need bigger sum)
  - If `sum > target`: `r--` (Need smaller sum)
- **Complexity**: O(n) Time, O(1) Space.

## Implementation
- **Python**:
  ```python
  l, r = 0, len(numbers) - 1
  while l < r:
      s = numbers[l] + numbers[r]
      if s == target: return [l+1, r+1]
      if s < target: l += 1
      else: r -= 1
  ```

## Complexity Analysis
- **Time**: O(n)
- **Space**: O(1)

## Common Pitfalls
- **1-based Index**: Problem asks for 1-based.
- **Unsorted**: This logic only works because sorted.

## Key Patterns
- **Two Pointers**: Sorted array pair finding.
