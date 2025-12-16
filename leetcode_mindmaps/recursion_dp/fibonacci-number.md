# Fibonacci Number

## Problem Info
- **Link**: [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/description/)
- **Category**: Recursion & DP
- **Difficulty**: Easy
- **Status**: DONE

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
