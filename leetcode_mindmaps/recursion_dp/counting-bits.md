# Counting Bits

**Problem Link:** [Counting Bits](https://leetcode.com/problems/counting-bits/)
**Category:** Recursion & DP

## Approach
### DP: dp[i] = dp[i >> 1] + (i & 1)

## Implementation
```java
public int[] countBits(int n) {
    int[] dp = new int[n + 1];
    for (int i = 1; i <= n; i++) {
        dp[i] = dp[i >> 1] + (i & 1);
    }
    return dp;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(n)
