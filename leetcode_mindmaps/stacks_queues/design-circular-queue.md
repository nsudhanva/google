# Design Circular Queue

**Problem Link:** [Design Circular Queue](https://leetcode.com/problems/design-circular-queue/)
**Category:** Stacks & Queues

## Implementation
```java
class MyCircularQueue {
    int[] data;
    int head = 0, tail = -1, size = 0;
    
    public MyCircularQueue(int k) { data = new int[k]; }
    
    public boolean enQueue(int value) {
        if (isFull()) return false;
        tail = (tail + 1) % data.length;
        data[tail] = value;
        size++;
        return true;
    }
    
    public boolean deQueue() {
        if (isEmpty()) return false;
        head = (head + 1) % data.length;
        size--;
        return true;
    }
    
    public int Front() { return isEmpty() ? -1 : data[head]; }
    public int Rear() { return isEmpty() ? -1 : data[tail]; }
    public boolean isEmpty() { return size == 0; }
    public boolean isFull() { return size == data.length; }
}
```
