# Fibonacci Number

## Problem Info
- **Link**: [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/description/)
- **Category**: Recursion & DP
- **Difficulty**: Easy
- **Status**: DONE

## Problem Description
- The **Fibonacci numbers** , commonly denoted `F(n)` form a sequence, called the **Fibonacci sequence** , such that each number is the sum of the two preceding ones, starting from `0` and `1`. That is,
- F(0) = 0, F(1) = 1
    F(n) = F(n - 1) + F(n - 2), for n > 1.
    

Given `n`, calculate `F(n)`.
- **Example 1:**
- **Input:** n = 2
    **Output:** 1
    **Explanation:** F(2) = F(1) + F(0) = 1 + 0 = 1.
    

**Example 2:**
- **Input:** n = 3
    **Output:** 2
    **Explanation:** F(3) = F(2) + F(1) = 1 + 1 = 2.
    

**Example 3:**
- **Input:** n = 4
    **Output:** 3
    **Explanation:** F(4) = F(3) + F(2) = 2 + 1 = 3.
- **Constraints:**
- * `0 <= n <= 30`

## Approach
### Data Structure
- DP, recursion, memo

### Time Complexity
- O(n)

## Things to Remember
- Just recursion - most time consuming.
- I did recursion with memo, space O(n).
- Better way, use 2 variables to store n-1 and n-2 ans and do iterative - space O(1).

## Additional Notes
- memo[n] = fib_rec(n - 1, memo) + fib_rec(n-2, memo);
