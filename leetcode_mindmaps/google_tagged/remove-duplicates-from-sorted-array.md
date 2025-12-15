# Remove Duplicates from Sorted Array

**Problem Link:** [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
**Category:** Google tagged

## Problem Understanding
- Remove duplicates in-place, return count of unique elements

## Approach

### Two Pointers (Slow/Fast)
- Slow pointer marks last unique position
- Fast pointer scans for new unique elements

## Implementation
```java
public int removeDuplicates(int[] nums) {
    if (nums.length == 0) return 0;
    
    int j = 0;
    for (int i = 1; i < nums.length; i++) {
        if (nums[i] != nums[j]) {
            j++;
            nums[j] = nums[i];
        }
    }
    return j + 1;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
