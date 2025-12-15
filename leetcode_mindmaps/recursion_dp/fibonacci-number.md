# Fibonacci Number

**Problem Link:** [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)
**Category:** Recursion & DP

## Implementation
```java
public int fib(int n) {
    if (n <= 1) return n;
    int a = 0, b = 1;
    for (int i = 2; i <= n; i++) {
        int temp = a + b;
        a = b;
        b = temp;
    }
    return b;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
