# Min cost climbing stirs

## Problem Info
- **Link**: [Min cost climbing stirs](https://leetcode.com/problems/min-cost-climbing-stairs/description/)
- **Category**: Recursion & DP
- **Difficulty**: Easy
- **Status**: DONE

## Approach
### Data Structure
- DP

### Time Complexity
- O(n)

## Things to Remember
- I did Iterative DP, using mentioned formula at every step. Can also do recursive with memo.

## Additional Notes
- minCost[i] = cost[i] + Math.min(minCost[i - 1], minCost[i - 2]);
