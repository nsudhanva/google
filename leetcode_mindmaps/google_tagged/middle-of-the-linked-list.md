# Middle of the Linked List

**Problem Link:** [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)
**Category:** Google tagged

## Problem Understanding
- Return middle node (second middle if two)

## Approach

### Fast/Slow Pointers
- Fast moves 2x, when fast ends, slow is at middle

## Implementation
```java
public ListNode middleNode(ListNode head) {
    ListNode slow = head, fast = head;
    
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
    }
    return slow;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
