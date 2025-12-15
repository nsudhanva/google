# Calculate Money in Leetcode Bank

**Problem Link:** [Calculate Money in Leetcode Bank](https://leetcode.com/problems/calculate-money-in-leetcode-bank/)

**Category:** Google tagged

## Problem Understanding
- Input: `n` days.
- Rules:
  - Monday starts with 1 more than prev Monday.
  - Next day = prev day + 1.
  - Week 1: 1, 2, 3, 4, 5, 6, 7
  - Week 2: 2, 3, 4, 5, 6, 7, 8
  - Week 3: 3, 4, 5, ...
- Output: Total money.

## Approach

### Simulation
- **Idea**: Loop `n` times, adding money.
- **Algorithm**:
  - `total = 0`, `monday = 1`, `daily = 1`
  - Loop `day` from 0 to n-1:
    - If `day % 7 == 0` (Monday): reset `daily` based on week
    - `total += daily`
    - `daily += 1`
  - Simpler:
    - `weeks = n // 7`, `days = n % 7`
    - Calculate full weeks using Arithmetic Progression.
    - Calculate remaining days.

### Arithmetic Progression (Math)
- **Idea**: Use Sum formula `n/2 * (2a + (n-1)d)`.
- **Full Weeks**:
  - Week 0 (start 1): Sum = 28
  - Week 1 (start 2): Sum = 28 + 7 = 35
  - Week k: Sum = 28 + 7*k
  - Sum of `w` weeks = `w * 28 + 7 * (w*(w-1)/2)`
- **Remaining Days**:
  - Start value `w + 1`.
  - Sum `d` days starting at `start`: `d * start + d*(d-1)/2`
- **Complexity**: O(1).

## Implementation (Math)
- **Python**:
  ```python
  limit = n // 7
  rem = n % 7
  week_sum = 28 * limit + 7 * (limit * (limit - 1)) // 2
  rem_start = limit + 1
  rem_sum = rem * rem_start + rem * (rem - 1) // 2
  return week_sum + rem_sum
  ```

## Complexity Analysis
- **Time**: O(1)
- **Space**: O(1)

## Common Pitfalls
- **Index Math**: 0-based vs 1-based weeks.

## Key Patterns
- **Math/Simulation**: Arithmetic series.
