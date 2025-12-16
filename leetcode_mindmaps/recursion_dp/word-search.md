# Word Search

## Problem Info
- **Link**: [Word Search](https://leetcode.com/problems/word-search/description/)
- **Category**: Recursion & DP
- **Difficulty**: Medium
- **Status**: DONE

## Approach
### Data Structure
- Backtracking, DFS

### Time Complexity
- O(m*n*3^w)

## Things to Remember
- Follows the basic backtracking structure.
- Have a visited matrix where you vist the current pos, check all 4 paths and if not, unvisit that position and proceed.
- Choice: each of 4 directions, choice to visit this index.
- Base cond: if end of word, true.
- if out of bounds OR not matching char OR already visited, false.
