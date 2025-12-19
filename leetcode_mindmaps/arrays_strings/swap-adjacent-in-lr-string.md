# swap adjacent in LR string

## Problem Info
- **Link**: [swap adjacent in LR string](https://leetcode.com/problems/swap-adjacent-in-lr-string/description/)
- **Category**: Arrays & Strings
- **Difficulty**: Medium
- **Status**: DONE

## Problem Description
- In a string composed of `'L'`, `'R'`, and `'X'` characters, like `"RXXLRXRXL"`, a move consists of either replacing one occurrence of `"XL"` with `"LX"`, or replacing one occurrence of `"RX"` with `"XR"`. Given the starting string `start` and the ending string `result`, return `True` if and only if there exists a sequence of moves to transform `start` to `result`.
- **Example 1:**
- **Input:** start = "RXXLRXRXL", result = "XRLXXRRLX"
    **Output:** true
    **Explanation:** We can transform start to result following these steps:
    RXXLRXRXL ->
    XRXLRXRXL ->
    XRLXRXRXL ->
    XRLXXRRXL ->
    XRLXXRRLX
    

**Example 2:**
- **Input:** start = "X", result = "L"
    **Output:** false
- **Constraints:**
- * `1 <= start.length <= 104`
  * `start.length == result.length`
  * Both `start` and `result` will only consist of characters in `'L'`, `'R'`, and `'X'`.

## Approach
### Data Structure
- Two pointers

### Time Complexity
- O(n)

## Things to Remember
- First ret false if number of X is not equal.
- then loop through both, find first matching L or R.
- both chars in the strings should be same.
- if R, then it can only move right and L can only move left.
- otherwise return false.
- Analogy: think of L and R as people in a straight line.
- they cannot pass each other and XRX cannot become RXX.
