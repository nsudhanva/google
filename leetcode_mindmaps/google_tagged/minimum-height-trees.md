# Minimum Height Trees

**Problem Link:** [Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees/)
**Category:** Google tagged

## Approach
### Topological Sort (Trim Leaves)
- Remove leaves layer by layer until 1-2 nodes remain

## Implementation
```java
public List<Integer> findMinHeightTrees(int n, int[][] edges) {
    if (n == 1) return Arrays.asList(0);
    
    List<Set<Integer>> adj = new ArrayList<>();
    for (int i = 0; i < n; i++) adj.add(new HashSet<>());
    for (int[] e : edges) {
        adj.get(e[0]).add(e[1]);
        adj.get(e[1]).add(e[0]);
    }
    
    List<Integer> leaves = new ArrayList<>();
    for (int i = 0; i < n; i++) {
        if (adj.get(i).size() == 1) leaves.add(i);
    }
    
    int remaining = n;
    while (remaining > 2) {
        remaining -= leaves.size();
        List<Integer> newLeaves = new ArrayList<>();
        for (int leaf : leaves) {
            int neighbor = adj.get(leaf).iterator().next();
            adj.get(neighbor).remove(leaf);
            if (adj.get(neighbor).size() == 1) newLeaves.add(neighbor);
        }
        leaves = newLeaves;
    }
    return leaves;
}
```
