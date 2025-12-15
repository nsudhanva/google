# Merge Sorted Array

**Problem Link:** [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)
**Category:** Google tagged

## Problem Understanding
- Merge `nums2` into `nums1` in-place
- `nums1` has extra space at end

## Approach

### Fill from End (Reverse Two Pointers)
- Start from the end to avoid overwriting unprocessed elements
- Compare and place larger element at position `p`

## Implementation
```java
public void merge(int[] nums1, int m, int[] nums2, int n) {
    int p1 = m - 1, p2 = n - 1, p = m + n - 1;
    
    while (p2 >= 0) {
        if (p1 >= 0 && nums1[p1] > nums2[p2]) {
            nums1[p--] = nums1[p1--];
        } else {
            nums1[p--] = nums2[p2--];
        }
    }
}
```

## Complexity
- **Time**: O(m + n)
- **Space**: O(1)

## Key Insight
- Fill from end when array has space at end
