# Running Sum of 1d Array

**Problem Link:** [Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/)
**Category:** Google tagged

## Problem Understanding
- `result[i] = sum(nums[0]...nums[i])`

## Approach

### Prefix Sum (In-Place)
- Each element becomes sum of itself and previous

## Implementation
```java
public int[] runningSum(int[] nums) {
    for (int i = 1; i < nums.length; i++) {
        nums[i] += nums[i - 1];
    }
    return nums;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
