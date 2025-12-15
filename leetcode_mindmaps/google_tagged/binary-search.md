# Binary Search

**Problem Link:** [Binary Search](https://leetcode.com/problems/binary-search/)
**Category:** Google tagged

## Problem Understanding
- Find target in sorted array, return index or -1

## Approach

### Binary Search
- Divide search space in half each iteration

## Implementation
```java
public int search(int[] nums, int target) {
    int left = 0, right = nums.length - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) return mid;
        if (nums[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}
```

## Complexity
- **Time**: O(log n)
- **Space**: O(1)

## Key Insight
- Use `left + (right - left) / 2` to avoid integer overflow
