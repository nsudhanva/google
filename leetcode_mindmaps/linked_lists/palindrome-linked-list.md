# Palindrome Linked List

**Problem Link:** [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)
**Category:** Linked Lists

## Problem Understanding
- Check if linked list is palindrome

## Approach

### Reverse Second Half
1. Find middle (fast/slow)
2. Reverse second half
3. Compare halves

## Implementation
```java
public boolean isPalindrome(ListNode head) {
    // Find middle
    ListNode slow = head, fast = head;
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
    }
    
    // Reverse second half
    ListNode prev = null;
    while (slow != null) {
        ListNode next = slow.next;
        slow.next = prev;
        prev = slow;
        slow = next;
    }
    
    // Compare
    ListNode left = head, right = prev;
    while (right != null) {
        if (left.val != right.val) return false;
        left = left.next;
        right = right.next;
    }
    return true;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
