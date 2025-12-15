# Number of Connected Components in an Undirected Graph

**Problem Link:** [Number of Connected Components](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)
**Category:** Google tagged

## Implementation
```java
public int countComponents(int n, int[][] edges) {
    int[] parent = new int[n];
    for (int i = 0; i < n; i++) parent[i] = i;
    
    int count = n;
    for (int[] e : edges) {
        int p1 = find(parent, e[0]), p2 = find(parent, e[1]);
        if (p1 != p2) {
            parent[p1] = p2;
            count--;
        }
    }
    return count;
}

private int find(int[] parent, int i) {
    while (parent[i] != i) {
        parent[i] = parent[parent[i]];
        i = parent[i];
    }
    return i;
}
```

## Complexity
- **Time**: O(E * α(N))
- **Space**: O(N)
