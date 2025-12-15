# Generate Parentheses

**Problem Link:** [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
**Category:** Recursion & DP

## Problem Understanding
- Generate all valid combinations of n pairs of parentheses

## Approach

### Backtracking
- Track open and close counts
- Add '(' if open < n, ')' if close < open

## Implementation
```java
public List<String> generateParenthesis(int n) {
    List<String> result = new ArrayList<>();
    backtrack(result, "", 0, 0, n);
    return result;
}

private void backtrack(List<String> result, String curr, int open, int close, int n) {
    if (curr.length() == 2 * n) {
        result.add(curr);
        return;
    }
    if (open < n) backtrack(result, curr + "(", open + 1, close, n);
    if (close < open) backtrack(result, curr + ")", open, close + 1, n);
}
```

## Complexity
- **Time**: O(4^n / sqrt(n)) - Catalan number
- **Space**: O(n)
