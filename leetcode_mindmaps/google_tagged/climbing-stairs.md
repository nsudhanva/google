# Climbing Stairs

**Problem Link:** [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
**Category:** Google tagged

## Problem Understanding
- Count ways to reach top taking 1 or 2 steps

## Approach

### Fibonacci DP
- `ways(n) = ways(n-1) + ways(n-2)`
- Only need last two values

## Implementation
```java
public int climbStairs(int n) {
    if (n <= 2) return n;
    
    int prev1 = 1, prev2 = 2;
    for (int i = 3; i <= n; i++) {
        int curr = prev1 + prev2;
        prev1 = prev2;
        prev2 = curr;
    }
    return prev2;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)

## Key Insight
- Classic DP, same as Fibonacci
