# Remove Element

**Problem Link:** [Remove Element](https://leetcode.com/problems/remove-element/)

**Category:** Google tagged

## Problem Understanding
- Input: Array `nums`, value `val`
- Output: k (number of elements != val). Modify `nums` in-place.
- Example: `[3,2,2,3], val=3` -> `[2,2,_,_]`, k=2.

## Approach

### Two Pointers (Reader/Writer)
- **Idea**: Writer pointer (`i`) only advances when Reader pointer (`j`) sees a valid element (not `val`).
- **Algorithm**:
  - `i = 0`
  - For `j` in range `n`:
    - If `nums[j] != val`:
      - `nums[i] = nums[j]`
      - `i++`
  - Return `i`

### Optimization (Swap with End)
- **Idea**: If removing is rare, swap current `val` with last element and reduce array size.
- **Algorithm**:
  - `i = 0`, `n = len(nums)`
  - While `i < n`:
    - If `nums[i] == val`:
      - `nums[i] = nums[n-1]`
      - `n--`
    - Else: `i++`
  - Return `n`
- **Benefit**: Minimum writes.

## Implementation
- **Python**:
  ```python
  i = 0
  for x in nums:
      if x != val:
          nums[i] = x
          i += 1
  return i
  ```

## Complexity Analysis
- **Time**: O(n)
- **Space**: O(1)

## Common Pitfalls
- **Order**: Elements order can be changed? Problem says "Order can be changed".

## Key Patterns
- **In-place Filter**: Two pointers.
