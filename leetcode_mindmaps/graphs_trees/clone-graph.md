# Clone Graph

## Problem Info
- **Link**: [Clone Graph](https://leetcode.com/problems/clone-graph/)
- **Category**: Graphs & Trees
- **Difficulty**: Medium
- **Status**: DONE

## Approach
### Data Structure
- Graph, DFS

### Time Complexity
- O(N+E)

## Things to Remember
- Similar to top two.
- Maintain a hashmap of old node to the copy.
- if the map contains, return that node.
- otherwise loop through each neighbor and call dfs on each and add to neighbors of the new node.
