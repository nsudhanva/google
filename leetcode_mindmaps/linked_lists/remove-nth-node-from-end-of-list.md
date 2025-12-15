# Remove Nth Node From End of List

**Problem Link:** [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
**Category:** Linked Lists

## Problem Understanding
- Remove nth node from end in one pass

## Approach

### Two Pointers (Gap of N)
- Move fast n steps ahead
- Move both until fast reaches end
- Slow is at prev of target

## Implementation
```java
public ListNode removeNthFromEnd(ListNode head, int n) {
    ListNode dummy = new ListNode(0);
    dummy.next = head;
    ListNode slow = dummy, fast = dummy;
    
    for (int i = 0; i <= n; i++) fast = fast.next;
    
    while (fast != null) {
        slow = slow.next;
        fast = fast.next;
    }
    
    slow.next = slow.next.next;
    return dummy.next;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
