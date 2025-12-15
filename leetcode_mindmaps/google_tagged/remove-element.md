# Remove Element

**Problem Link:** [Remove Element](https://leetcode.com/problems/remove-element/)
**Category:** Google tagged

## Problem Understanding
- Remove all occurrences of `val` in-place

## Approach

### Two Pointers
- Writer pointer only advances for valid elements

## Implementation
```java
public int removeElement(int[] nums, int val) {
    int i = 0;
    for (int j = 0; j < nums.length; j++) {
        if (nums[j] != val) {
            nums[i] = nums[j];
            i++;
        }
    }
    return i;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
