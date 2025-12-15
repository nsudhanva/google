# Pascal's Triangle

**Problem Link:** [Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/)
**Category:** Recursion & DP

## Implementation
```java
public List<List<Integer>> generate(int numRows) {
    List<List<Integer>> result = new ArrayList<>();
    
    for (int i = 0; i < numRows; i++) {
        List<Integer> row = new ArrayList<>();
        for (int j = 0; j <= i; j++) {
            if (j == 0 || j == i) row.add(1);
            else row.add(result.get(i-1).get(j-1) + result.get(i-1).get(j));
        }
        result.add(row);
    }
    return result;
}
```

## Complexity
- **Time**: O(n²)
- **Space**: O(n²)
