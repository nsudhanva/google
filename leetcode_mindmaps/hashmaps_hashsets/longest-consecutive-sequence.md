# Longest Consecutive sequence

## Problem Info
- **Link**: [Longest Consecutive sequence](https://leetcode.com/problems/longest-consecutive-sequence/description/)
- **Category**: Hashmaps & HashSets
- **Difficulty**: Medium
- **Status**: DONE but REVISIT

## Approach
### Data Structure
- BFS Solution was more intuitive

### Time Complexity
- O(n)

## Things to Remember
- Bruteforce - sort and check every consecutive while maintaining max.
- BFS - visualize as graph, create adj by adding list of prev and next numbers if exists, then maintain visted, for each key and not visited, add to q, while q not empty, remove, and for each nei not visited, add to q while inc size.
