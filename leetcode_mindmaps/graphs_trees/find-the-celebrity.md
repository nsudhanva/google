# Find the celebrity

## Problem Info
- **Link**: [Find the celebrity](https://leetcode.com/problems/find-the-celebrity/)
- **Category**: Graphs & Trees
- **Difficulty**: Medium
- **Status**: DONE

## Approach
### Data Structure
- Graph

### Time Complexity
- O(n)

## Things to Remember
- Easy, brute force is simply checking every pair.
- Otherwise get a candidate from 1 pass - if one person knows anyone else, they cannot be the candidate.
- Second pass you can use to check if they are actually the celebrity.
- Can also do with caching.
