# Find Median from Data Stream

**Problem Link:** [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)
**Category:** Heaps

## Problem Understanding
- Add numbers, query median efficiently

## Approach

### Two Heaps
- Max heap for lower half
- Min heap for upper half
- Balance sizes (differ by at most 1)

## Implementation
```java
class MedianFinder {
    private PriorityQueue<Integer> lo = new PriorityQueue<>(Collections.reverseOrder());
    private PriorityQueue<Integer> hi = new PriorityQueue<>();
    
    public void addNum(int num) {
        lo.offer(num);
        hi.offer(lo.poll());
        if (hi.size() > lo.size()) {
            lo.offer(hi.poll());
        }
    }
    
    public double findMedian() {
        if (lo.size() > hi.size()) {
            return lo.peek();
        }
        return (lo.peek() + hi.peek()) / 2.0;
    }
}
```

## Complexity
- **addNum**: O(log n)
- **findMedian**: O(1)
- **Space**: O(n)
