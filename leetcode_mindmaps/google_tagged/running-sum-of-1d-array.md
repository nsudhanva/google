# Running Sum of 1d Array

**Problem Link:** [Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/)

**Category:** Google tagged

## Problem Understanding
- Input: Array `nums`
- Output: `result[i] = sum(nums[0]...nums[i])`

## Approach

### Prefix Sum (In-Place)
- **Idea**: Each element `i` becomes `nums[i] + nums[i-1]`.
- **Algorithm**:
  - Loop `i` from 1 to `n-1`:
    - `nums[i] += nums[i-1]`
  - Return `nums`

## Implementation
- **Python**:
  ```python
  for i in range(1, len(nums)):
      nums[i] += nums[i-1]
  return nums
  ```

## Complexity Analysis
- **Time**: O(n)
- **Space**: O(1)

## Common Pitfalls
- **Start Index**: Start loop from 1.

## Key Patterns
- **Prefix Sum**: Base for range sum queries.
