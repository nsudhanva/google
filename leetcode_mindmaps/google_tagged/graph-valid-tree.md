# Graph Valid Tree

**Problem Link:** [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/)
**Category:** Google tagged

## Problem Understanding
- Check if edges form a valid tree (connected, no cycles)

## Approach
- Valid tree: n nodes, n-1 edges, all connected

## Implementation
```java
public boolean validTree(int n, int[][] edges) {
    if (edges.length != n - 1) return false;
    
    List<List<Integer>> adj = new ArrayList<>();
    for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
    for (int[] e : edges) {
        adj.get(e[0]).add(e[1]);
        adj.get(e[1]).add(e[0]);
    }
    
    Set<Integer> visited = new HashSet<>();
    Queue<Integer> queue = new LinkedList<>();
    queue.offer(0);
    visited.add(0);
    
    while (!queue.isEmpty()) {
        int node = queue.poll();
        for (int neighbor : adj.get(node)) {
            if (!visited.contains(neighbor)) {
                visited.add(neighbor);
                queue.offer(neighbor);
            }
        }
    }
    return visited.size() == n;
}
```

## Complexity
- **Time**: O(V + E)
- **Space**: O(V + E)
