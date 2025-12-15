# Implement Queue using Stacks

**Problem Link:** [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)
**Category:** Stacks & Queues

## Implementation
```java
class MyQueue {
    Stack<Integer> in = new Stack<>();
    Stack<Integer> out = new Stack<>();
    
    public void push(int x) { in.push(x); }
    
    public int pop() {
        peek();
        return out.pop();
    }
    
    public int peek() {
        if (out.isEmpty()) {
            while (!in.isEmpty()) out.push(in.pop());
        }
        return out.peek();
    }
    
    public boolean empty() { return in.isEmpty() && out.isEmpty(); }
}
```

## Complexity
- **Amortized**: O(1) per operation
