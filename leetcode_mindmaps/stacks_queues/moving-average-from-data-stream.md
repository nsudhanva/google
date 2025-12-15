# Moving Average from Data Stream

**Problem Link:** [Moving Average from Data Stream](https://leetcode.com/problems/moving-average-from-data-stream/)
**Category:** Stacks & Queues

## Implementation
```java
class MovingAverage {
    Queue<Integer> queue = new LinkedList<>();
    int size, sum = 0;
    
    public MovingAverage(int size) { this.size = size; }
    
    public double next(int val) {
        if (queue.size() == size) sum -= queue.poll();
        queue.offer(val);
        sum += val;
        return (double) sum / queue.size();
    }
}
```

## Complexity
- **Time**: O(1)
- **Space**: O(size)
