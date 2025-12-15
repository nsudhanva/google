# LRU Cache

**Problem Link:** [LRU Cache](https://leetcode.com/problems/lru-cache/)
**Category:** Linked Lists

## Problem Understanding
- Implement LRU Cache with O(1) get/put

## Approach

### HashMap + Doubly Linked List
- Map: key -> node
- DLL: Most recent at head, least at tail

## Implementation
```java
class LRUCache {
    class Node {
        int key, val;
        Node prev, next;
        Node(int k, int v) { key = k; val = v; }
    }
    
    private Map<Integer, Node> cache = new HashMap<>();
    private Node head = new Node(0, 0);
    private Node tail = new Node(0, 0);
    private int capacity;
    
    public LRUCache(int capacity) {
        this.capacity = capacity;
        head.next = tail;
        tail.prev = head;
    }
    
    public int get(int key) {
        if (!cache.containsKey(key)) return -1;
        Node node = cache.get(key);
        remove(node);
        insertAtHead(node);
        return node.val;
    }
    
    public void put(int key, int value) {
        if (cache.containsKey(key)) remove(cache.get(key));
        Node node = new Node(key, value);
        cache.put(key, node);
        insertAtHead(node);
        if (cache.size() > capacity) {
            Node lru = tail.prev;
            remove(lru);
            cache.remove(lru.key);
        }
    }
    
    private void remove(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }
    
    private void insertAtHead(Node node) {
        node.next = head.next;
        node.prev = head;
        head.next.prev = node;
        head.next = node;
    }
}
```

## Complexity
- **Time**: O(1) for both operations
- **Space**: O(capacity)
