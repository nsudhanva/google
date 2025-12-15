# Clone Graph

**Problem Link:** [Clone Graph](https://leetcode.com/problems/clone-graph/)
**Category:** Google tagged

## Problem Understanding
- Deep copy a graph with adjacency list

## Approach

### DFS with HashMap
- Map old node -> cloned node
- Recursively clone neighbors

## Implementation
```java
private Map<Node, Node> visited = new HashMap<>();

public Node cloneGraph(Node node) {
    if (node == null) return null;
    
    if (visited.containsKey(node)) {
        return visited.get(node);
    }
    
    Node clone = new Node(node.val);
    visited.put(node, clone);
    
    for (Node neighbor : node.neighbors) {
        clone.neighbors.add(cloneGraph(neighbor));
    }
    return clone;
}
```

## Complexity
- **Time**: O(V + E)
- **Space**: O(V)
