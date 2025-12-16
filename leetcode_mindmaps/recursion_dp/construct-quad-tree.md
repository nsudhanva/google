# Construct quad tree

## Problem Info
- **Link**: [Construct quad tree](https://leetcode.com/problems/construct-quad-tree/description/)
- **Category**: Recursion & DP
- **Difficulty**: Medium
- **Status**: DONE

## Approach
### Data Structure
- Recursion

### Time Complexity
- O(n2)

## Things to Remember
- 2 ways of recursion - 1st: At each call, check if the grid has all same values, if not then divide into 4 recursively.
- 2nd: divide by 4 recursively till you reach length 1 when you return the value and is leaf.
- The later check if all 4 vals are same, if so, then can be combined into a single leaf, otherwise no.
