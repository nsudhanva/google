# Min Stack

**Problem Link:** [Min Stack](https://leetcode.com/problems/min-stack/)
**Category:** Stacks & Queues

## Problem Understanding
- Stack with O(1) push, pop, top, and getMin

## Approach

### Two Stacks
- One for values, one for minimums

## Implementation
```java
class MinStack {
    private Stack<Integer> stack = new Stack<>();
    private Stack<Integer> minStack = new Stack<>();
    
    public void push(int val) {
        stack.push(val);
        if (minStack.isEmpty() || val <= minStack.peek()) {
            minStack.push(val);
        }
    }
    
    public void pop() {
        if (stack.pop().equals(minStack.peek())) {
            minStack.pop();
        }
    }
    
    public int top() { return stack.peek(); }
    public int getMin() { return minStack.peek(); }
}
```

## Complexity
- **Time**: O(1) all operations
- **Space**: O(n)
