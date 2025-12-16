# Course Schedule

## Problem Info
- **Link**: [Course Schedule](https://leetcode.com/problems/course-schedule/)
- **Category**: Graphs & Trees
- **Difficulty**: Medium
- **Status**: DONE

## Approach
### Data Structure
- Graph, DFS

### Time Complexity
- O(N+E)

## Things to Remember
- Way 1: (DFS recursive) have a map with each course mapping to an array of prereq.
- Then for each course run dfs.
- Base case is if crs is in visited - false.
- if prereq array is empty - true.
- then loop through prereqs and run dfs again.
- after the loop, remove from visited, and make prereq empty.

## Additional Notes
- Way 2: (DFS recursive 2) have a map with each course mapping to an array of prereq. Then for each course run dfs. Also have a states array for each course state. 0 - unvisited, 1 - visiting, 2 - visisted. Base case is if crs state is visiting - false. if crs state is visited - true. then loop through prereqs and run dfs again. after the loop, change from visiting to visited
