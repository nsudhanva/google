# Course Schedule

## Problem Info
- **Link**: [Course Schedule](https://leetcode.com/problems/course-schedule/)
- **Category**: Graphs & Trees
- **Difficulty**: Medium
- **Status**: DONE

## Problem Description
- There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you **must** take course `bi` first if you want to take course `ai`.
- * For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.



Return `true` if you can finish all courses. Otherwise, return `false`.
- **Example 1:**
- **Input:** numCourses = 2, prerequisites = [[1,0]]
    **Output:** true
    **Explanation:** There are a total of 2 courses to take. 
    To take course 1 you should have finished course 0. So it is possible.
    

**Example 2:**
- **Input:** numCourses = 2, prerequisites = [[1,0],[0,1]]
    **Output:** false
    **Explanation:** There are a total of 2 courses to take. 
    To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
- **Constraints:**
- * `1 <= numCourses <= 2000`
  * `0 <= prerequisites.length <= 5000`
  * `prerequisites[i].length == 2`
  * `0 <= ai, bi < numCourses`
  * All the pairs prerequisites[i] are **unique**.

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
