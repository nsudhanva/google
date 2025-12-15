# Implement Stack using Queues

**Problem Link:** [Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)
**Category:** Stacks & Queues

## Implementation
```java
class MyStack {
    Queue<Integer> queue = new LinkedList<>();
    
    public void push(int x) {
        queue.offer(x);
        int size = queue.size();
        while (size-- > 1) queue.offer(queue.poll());
    }
    
    public int pop() { return queue.poll(); }
    public int top() { return queue.peek(); }
    public boolean empty() { return queue.isEmpty(); }
}
```
