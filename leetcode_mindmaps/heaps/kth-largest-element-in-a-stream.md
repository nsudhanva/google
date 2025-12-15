# Kth Largest Element in a Stream

**Problem Link:** [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)
**Category:** Heaps

## Implementation
```java
class KthLargest {
    PriorityQueue<Integer> minHeap = new PriorityQueue<>();
    int k;
    
    public KthLargest(int k, int[] nums) {
        this.k = k;
        for (int n : nums) add(n);
    }
    
    public int add(int val) {
        minHeap.offer(val);
        if (minHeap.size() > k) minHeap.poll();
        return minHeap.peek();
    }
}
```

## Complexity
- **Time**: O(log k) per add
- **Space**: O(k)
