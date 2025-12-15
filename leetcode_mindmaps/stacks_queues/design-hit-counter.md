# Design Hit Counter

**Problem Link:** [Design Hit Counter](https://leetcode.com/problems/design-hit-counter/)
**Category:** Stacks & Queues

## Implementation
```java
class HitCounter {
    Queue<Integer> queue = new LinkedList<>();
    
    public void hit(int timestamp) {
        queue.offer(timestamp);
    }
    
    public int getHits(int timestamp) {
        while (!queue.isEmpty() && timestamp - queue.peek() >= 300) {
            queue.poll();
        }
        return queue.size();
    }
}
```
