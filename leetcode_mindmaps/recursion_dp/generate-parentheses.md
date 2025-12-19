# Generate Parentheses

## Problem Info
- **Link**: [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/description/)
- **Category**: Recursion & DP
- **Difficulty**: Medium
- **Status**: DONE

## Problem Description
- Given `n` pairs of parentheses, write a function to _generate all combinations of well-formed parentheses_.
- **Example 1:**
- **Input:** n = 3
    **Output:** ["((()))","(()())","(())()","()(())","()()()"]
    

**Example 2:**
- **Input:** n = 1
    **Output:** ["()"]
- **Constraints:**
- * `1 <= n <= 8`

## Approach
### Data Structure
- Backtracking

### Time Complexity
- O(4^n/sqrt(n))

## Things to Remember
- Choice: add "(" or ")", constraint: should be valid - can add "(" if openCt < n and can add ")" if closeCt < openCt.
- Base cond: if openCt==closeCt ==n, we have found a res.
