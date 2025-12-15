# Partition Equal Subset Sum

**Problem Link:** [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)
**Category:** Recursion & DP

## Problem Understanding
- Can array be partitioned into two equal sum subsets?

## Approach
### 0/1 Knapsack DP
- Target = totalSum / 2

## Implementation
```java
public boolean canPartition(int[] nums) {
    int sum = 0;
    for (int n : nums) sum += n;
    if (sum % 2 != 0) return false;
    
    int target = sum / 2;
    boolean[] dp = new boolean[target + 1];
    dp[0] = true;
    
    for (int num : nums) {
        for (int j = target; j >= num; j--) {
            dp[j] = dp[j] || dp[j - num];
        }
    }
    return dp[target];
}
```

## Complexity
- **Time**: O(n * sum)
- **Space**: O(sum)
