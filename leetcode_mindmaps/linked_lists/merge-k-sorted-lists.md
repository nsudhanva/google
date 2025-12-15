# Merge K Sorted Lists

**Problem Link:** [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
**Category:** Heaps / Linked Lists

## Approach
### Min Heap

## Implementation
```java
public ListNode mergeKLists(ListNode[] lists) {
    PriorityQueue<ListNode> pq = new PriorityQueue<>((a, b) -> a.val - b.val);
    
    for (ListNode node : lists) {
        if (node != null) pq.offer(node);
    }
    
    ListNode dummy = new ListNode(0);
    ListNode curr = dummy;
    
    while (!pq.isEmpty()) {
        ListNode node = pq.poll();
        curr.next = node;
        curr = curr.next;
        if (node.next != null) pq.offer(node.next);
    }
    return dummy.next;
}
```

## Complexity
- **Time**: O(N log k)
- **Space**: O(k)
