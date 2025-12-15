# Two Sum II - Input Array Is Sorted

**Problem Link:** [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
**Category:** Google tagged

## Problem Understanding
- Sorted array, find two indices (1-based) summing to target

## Approach

### Two Pointers
- Start at ends, move based on sum comparison

## Implementation
```java
public int[] twoSum(int[] numbers, int target) {
    int left = 0, right = numbers.length - 1;
    
    while (left < right) {
        int sum = numbers[left] + numbers[right];
        if (sum == target) {
            return new int[] { left + 1, right + 1 };
        } else if (sum < target) {
            left++;
        } else {
            right--;
        }
    }
    return new int[] {};
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
