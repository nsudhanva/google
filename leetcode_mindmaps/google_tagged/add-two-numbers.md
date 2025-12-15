# Add Two Numbers

**Problem Link:** [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)
**Category:** Google tagged

## Problem Understanding
- Two linked lists represent numbers in reverse order
- Return sum as linked list

## Approach

### Elementary Math with Carry
- Add digit by digit, track carry

## Implementation
```java
public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    ListNode dummy = new ListNode(0);
    ListNode curr = dummy;
    int carry = 0;
    
    while (l1 != null || l2 != null || carry != 0) {
        int v1 = (l1 != null) ? l1.val : 0;
        int v2 = (l2 != null) ? l2.val : 0;
        int sum = v1 + v2 + carry;
        
        carry = sum / 10;
        curr.next = new ListNode(sum % 10);
        curr = curr.next;
        
        if (l1 != null) l1 = l1.next;
        if (l2 != null) l2 = l2.next;
    }
    return dummy.next;
}
```

## Complexity
- **Time**: O(max(m, n))
- **Space**: O(max(m, n))

## Key Insight
- Include `carry != 0` in while condition for final carry
