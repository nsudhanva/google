# Flatten a Multilevel Doubly Linked List

**Problem Link:** [Flatten a Multilevel Doubly Linked List](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/)
**Category:** Linked Lists

## Implementation
```java
public Node flatten(Node head) {
    if (head == null) return null;
    Node curr = head;
    while (curr != null) {
        if (curr.child != null) {
            Node next = curr.next;
            Node child = flatten(curr.child);
            curr.next = child;
            child.prev = curr;
            curr.child = null;
            while (curr.next != null) curr = curr.next;
            if (next != null) {
                curr.next = next;
                next.prev = curr;
            }
        }
        curr = curr.next;
    }
    return head;
}
```
