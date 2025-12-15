# Strobogrammatic Number II

**Problem Link:** [Strobogrammatic Number II](https://leetcode.com/problems/strobogrammatic-number-ii/)
**Category:** Recursion & DP

## Implementation
```java
public List<String> findStrobogrammatic(int n) {
    return helper(n, n);
}

private List<String> helper(int n, int m) {
    if (n == 0) return new ArrayList<>(Arrays.asList(""));
    if (n == 1) return new ArrayList<>(Arrays.asList("0", "1", "8"));
    
    List<String> middles = helper(n - 2, m);
    List<String> result = new ArrayList<>();
    
    for (String middle : middles) {
        if (n != m) result.add("0" + middle + "0");
        result.add("1" + middle + "1");
        result.add("6" + middle + "9");
        result.add("8" + middle + "8");
        result.add("9" + middle + "6");
    }
    return result;
}
```
