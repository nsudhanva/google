# Palindrome Number

**Problem Link:** [Palindrome Number](https://leetcode.com/problems/palindrome-number/)

**Category:** Google tagged

## Problem Understanding
- Input: Integer `x`
- Output: `true` if palindrome (121 -> true, -121 -> false).
- Constraint: Follow up: Without converting to string?

## Approach

### String Conversion
- **Idea**: `str(x) == str(x)[::-1]`
- **Complexity**: O(log x) (digits) Time, O(log x) Space.

### Revert Half Number (Optimal)
- **Idea**: Revert the last half of the digits. Compare with first half.
- **Algorithm**:
  1. Base: If `x < 0` or (`x % 10 == 0` and `x != 0`), return `False`.
  2. `reverted = 0`
  3. While `x > reverted`:
     - `reverted = reverted * 10 + x % 10`
     - `x //= 10`
  4. Return `x == reverted` (even digits) or `x == reverted // 10` (odd digits).

## Implementation
- **Python**:
  ```python
  if x < 0 or (x % 10 == 0 and x != 0): return False
  rev = 0
  while x > rev:
      rev = rev * 10 + x % 10
      x //= 10
  return x == rev or x == rev // 10
  ```

## Complexity Analysis
- **Time**: O(log x)
- **Space**: O(1)

## Common Pitfalls
- **Negative Numbers**: -121 is NOT palindrome (reads 121-).
- **Trailing Zero**: 10 is NOT palindrome.
