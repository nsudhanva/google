# Reverse Linked List

**Problem Link:** [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
**Category:** Google tagged

## Problem Understanding
- Reverse singly linked list

## Approach

### Iterative (Pointer Swap)
- Track prev, curr, next; reverse links

## Implementation
```java
public ListNode reverseList(ListNode head) {
    ListNode prev = null;
    ListNode curr = head;
    
    while (curr != null) {
        ListNode nextTemp = curr.next;
        curr.next = prev;
        prev = curr;
        curr = nextTemp;
    }
    return prev;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
