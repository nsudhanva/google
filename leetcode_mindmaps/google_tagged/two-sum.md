# Two Sum

**Problem Link:** [Two Sum](https://leetcode.com/problems/two-sum/)
**Category:** Google tagged

## Problem Understanding
- Input: Array `nums`, integer `target`
- Output: Indices of two numbers that add up to `target`
- Constraints: Exactly one solution, can't use same element twice

## Approach

### Brute Force
- Check every pair `(i, j)` -> O(n²)

### Hash Map (Optimal)
- For each `x`, look for `target - x` in map
- One pass: check then add

## Implementation
```java
public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
        int complement = target - nums[i];
        if (map.containsKey(complement)) {
            return new int[] { map.get(complement), i };
        }
        map.put(nums[i], i);
    }
    return new int[] {};
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(n)

## Key Insight
- Trade space for time with HashMap
- Check *before* adding to handle duplicates correctly
