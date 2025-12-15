# Evaluate Division

**Problem Link:** [Evaluate Division](https://leetcode.com/problems/evaluate-division/)
**Category:** Google tagged

## Problem Understanding
- Given a/b = k, evaluate queries like a/c

## Approach
### Graph DFS
- Build weighted graph, find path

## Implementation
```java
public double[] calcEquation(List<List<String>> equations, double[] values, 
                             List<List<String>> queries) {
    Map<String, Map<String, Double>> graph = new HashMap<>();
    
    for (int i = 0; i < equations.size(); i++) {
        String a = equations.get(i).get(0), b = equations.get(i).get(1);
        graph.computeIfAbsent(a, k -> new HashMap<>()).put(b, values[i]);
        graph.computeIfAbsent(b, k -> new HashMap<>()).put(a, 1.0 / values[i]);
    }
    
    double[] result = new double[queries.size()];
    for (int i = 0; i < queries.size(); i++) {
        result[i] = dfs(queries.get(i).get(0), queries.get(i).get(1), 
                        graph, new HashSet<>());
    }
    return result;
}

private double dfs(String src, String dst, Map<String, Map<String, Double>> graph, 
                   Set<String> visited) {
    if (!graph.containsKey(src)) return -1.0;
    if (src.equals(dst)) return 1.0;
    visited.add(src);
    for (Map.Entry<String, Double> e : graph.get(src).entrySet()) {
        if (!visited.contains(e.getKey())) {
            double result = dfs(e.getKey(), dst, graph, visited);
            if (result != -1.0) return e.getValue() * result;
        }
    }
    return -1.0;
}
```

## Complexity
- **Time**: O(Q * (V + E))
- **Space**: O(V + E)
