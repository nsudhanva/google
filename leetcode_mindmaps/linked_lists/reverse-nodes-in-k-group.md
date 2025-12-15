# Reverse Nodes in K-Group

**Problem Link:** [Reverse Nodes in K-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)
**Category:** Linked Lists

## Implementation
```java
public ListNode reverseKGroup(ListNode head, int k) {
    ListNode curr = head;
    int count = 0;
    while (curr != null && count < k) {
        curr = curr.next;
        count++;
    }
    if (count == k) {
        curr = reverseKGroup(curr, k);
        while (count-- > 0) {
            ListNode next = head.next;
            head.next = curr;
            curr = head;
            head = next;
        }
        head = curr;
    }
    return head;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(n/k)
