# Happy Number

**Problem Link:** [Happy Number](https://leetcode.com/problems/happy-number/)

**Category:** Google tagged

## Problem Understanding
- Input: Integer `n`
- Process: Replace `n` with sum of squares of digits.
- Output: `true` if reaches 1, `false` if cycles endlessly.

## Approach

### Hash Set (Cycle Detection)
- **Idea**: Track seen numbers. If seen again -> Cycle -> False.
- **Algorithm**:
  - `seen = set()`
  - While `n != 1`:
    - If `n` in `seen`: return `False`
    - `seen.add(n)`
    - `n = sum_sq_digits(n)`
  - Return `True`

### Floyd's Cycle-Finding (Fast/Slow Pointers)
- **Idea**: Treat process as linked list `n -> next_n`. Use Fast/Slow pointers to detect cycle.
- **Algorithm**:
  - `slow = n`, `fast = sum_sq(n)`
  - While `fast != 1` and `slow != fast`:
    - `slow = sum_sq(slow)`
    - `fast = sum_sq(sum_sq(fast))`
  - Return `fast == 1`
- **Space**: O(1) - No set needed.

## Implementation
- **Python**:
  ```python
  def get_next(n):
      total_sum = 0
      while n > 0:
          n, digit = divmod(n, 10)
          total_sum += digit ** 2
      return total_sum

  seen = set()
  while n != 1 and n not in seen:
      seen.add(n)
      n = get_next(n)
  return n == 1
  ```

## Complexity Analysis
- **Time**: O(log n) - Number of digits per step decreases. Cycle isn't long.
- **Space**: O(log n) to store set.

## Common Pitfalls
- **Infinite Loop**: Forgetting to check `seen`.
- **Digit extraction**: Correctly implementing `sum of squares`.

## Key Patterns
- **Cycle Detection**: Hash Set or Floyd's Algorithm.
