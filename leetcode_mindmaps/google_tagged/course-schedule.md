# Course Schedule

**Problem Link:** [Course Schedule](https://leetcode.com/problems/course-schedule/)
**Category:** Google tagged

## Problem Understanding
- Can finish all courses? (Detect cycle in DAG)

## Approach

### Topological Sort (Kahn's BFS)
- Remove nodes with 0 in-degree iteratively
- If all removed, no cycle

## Implementation
```java
public boolean canFinish(int numCourses, int[][] prerequisites) {
    int[] indegree = new int[numCourses];
    List<List<Integer>> adj = new ArrayList<>();
    
    for (int i = 0; i < numCourses; i++) adj.add(new ArrayList<>());
    
    for (int[] prereq : prerequisites) {
        adj.get(prereq[1]).add(prereq[0]);
        indegree[prereq[0]]++;
    }
    
    Queue<Integer> queue = new LinkedList<>();
    for (int i = 0; i < numCourses; i++) {
        if (indegree[i] == 0) queue.offer(i);
    }
    
    int count = 0;
    while (!queue.isEmpty()) {
        int course = queue.poll();
        count++;
        for (int next : adj.get(course)) {
            if (--indegree[next] == 0) queue.offer(next);
        }
    }
    return count == numCourses;
}
```

## Complexity
- **Time**: O(V + E)
- **Space**: O(V + E)
