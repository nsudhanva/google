# Coin Change

**Problem Link:** [Coin Change](https://leetcode.com/problems/coin-change/)
**Category:** Recursion & DP

## Problem Understanding
- Find minimum coins to make amount

## Approach

### Bottom-Up DP
- `dp[i]` = min coins for amount `i`
- `dp[i] = min(dp[i], dp[i - coin] + 1)`

## Implementation
```java
public int coinChange(int[] coins, int amount) {
    int[] dp = new int[amount + 1];
    Arrays.fill(dp, amount + 1);
    dp[0] = 0;
    
    for (int coin : coins) {
        for (int x = coin; x <= amount; x++) {
            dp[x] = Math.min(dp[x], dp[x - coin] + 1);
        }
    }
    return dp[amount] > amount ? -1 : dp[amount];
}
```

## Complexity
- **Time**: O(amount * coins.length)
- **Space**: O(amount)
