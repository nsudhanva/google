# Sqrt(x)

**Problem Link:** [Sqrt(x)](https://leetcode.com/problems/sqrtx/)

**Category:** Google tagged

## Problem Understanding
- Input: Non-negative integer `x`
- Output: Square root of `x` rounded down (integer part).
- Constraint: No `pow(x, 0.5)` function.

## Approach

### Binary Search (Optimal)
- **Idea**: Search for `k` such that `k*k <= x` and `(k+1)*(k+1) > x`.
- **Search Space**: `[0, x]`
- **Algorithm**:
  - `l = 0`, `r = x`
  - While `l <= r`:
    - `mid = (l + r) // 2`
    - If `mid * mid == x`: return `mid`
    - If `mid * mid < x`: `l = mid + 1`, `ans = mid`
    - Else: `r = mid - 1`
  - Return `ans` (or `r`)

### Newton's Method (Math)
- **Idea**: Find root of `f(k) = k^2 - x = 0`.
- **Formula**: `k_new = (k + x/k) / 2`
- **Complexity**: O(log x) - Super fast convergence.

## Implementation (Binary Search)
- **Python**:
  ```python
  if x < 2: return x
  l, r = 2, x // 2
  while l <= r:
      mid = (l + r) // 2
      sq = mid * mid
      if sq == x: return mid
      elif sq < x: l = mid + 1
      else: r = mid - 1
  return r
  ```

## Complexity Analysis
- **Time**: O(log x)
- **Space**: O(1)

## Common Pitfalls
- **Overflow**: `mid * mid` can exceed Int max in Java/C++. Use `long` or division `x / mid`.
- **Loop Termination**: `l <= r` vs `l < r`. Returning `r` works because `r` will cross `l` and point to largest value <= sqrt.

## Key Patterns
- **Binary Search on Answer**: Searching in range `[0, x]`.
