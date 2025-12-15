# Copy List with Random Pointer

**Problem Link:** [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/)
**Category:** Linked Lists

## Implementation
```java
public Node copyRandomList(Node head) {
    if (head == null) return null;
    Map<Node, Node> map = new HashMap<>();
    
    Node curr = head;
    while (curr != null) {
        map.put(curr, new Node(curr.val));
        curr = curr.next;
    }
    
    curr = head;
    while (curr != null) {
        map.get(curr).next = map.get(curr.next);
        map.get(curr).random = map.get(curr.random);
        curr = curr.next;
    }
    return map.get(head);
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(n)
