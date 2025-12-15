# Sum of All Subset XOR Totals

**Problem Link:** [Sum of All Subset XOR Totals](https://leetcode.com/problems/sum-of-all-subset-xor-totals/)
**Category:** Recursion & DP

## Implementation
```java
public int subsetXORSum(int[] nums) {
    return helper(nums, 0, 0);
}

private int helper(int[] nums, int idx, int curr) {
    if (idx == nums.length) return curr;
    return helper(nums, idx + 1, curr ^ nums[idx]) + helper(nums, idx + 1, curr);
}
```
