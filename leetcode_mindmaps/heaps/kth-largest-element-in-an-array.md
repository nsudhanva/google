# Kth Largest Element in an Array

**Problem Link:** [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
**Category:** Heaps

## Problem Understanding
- Find kth largest element

## Approach

### Min Heap of Size K
- Keep k largest elements
- Top of min heap = kth largest

## Implementation
```java
public int findKthLargest(int[] nums, int k) {
    PriorityQueue<Integer> minHeap = new PriorityQueue<>();
    
    for (int num : nums) {
        minHeap.offer(num);
        if (minHeap.size() > k) {
            minHeap.poll();
        }
    }
    return minHeap.peek();
}
```

## Complexity
- **Time**: O(n log k)
- **Space**: O(k)
