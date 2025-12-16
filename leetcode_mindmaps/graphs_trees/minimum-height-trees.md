# Minimum height trees

## Problem Info
- **Link**: [Minimum height trees](https://leetcode.com/problems/minimum-height-trees/)
- **Category**: Graphs & Trees
- **Difficulty**: Medium
- **Status**: DONE

## Approach
### Data Structure
- Tree, BFS

### Time Complexity
- O(?)

## Things to Remember
- BFS to find height, brute force is intuitive but very time consuming.
- Soln - create adj map and edge count map.
- Add leaf nodes (edge cnt <=1) to a queue and start bfs.
- Base case is when number of nodes remaining is <= 2 then return leaf queue.
- dec n when you pop an ele from q.
