# Convert Binary Search Tree to Sorted Doubly Linked List

**Problem Link:** [Convert Binary Search Tree to Sorted Doubly Linked List](https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/)
**Category:** Graphs & Trees

## Implementation
```java
Node first = null, last = null;

public Node treeToDoublyList(Node root) {
    if (root == null) return null;
    inorder(root);
    last.right = first;
    first.left = last;
    return first;
}

private void inorder(Node node) {
    if (node == null) return;
    inorder(node.left);
    if (last != null) {
        last.right = node;
        node.left = last;
    } else {
        first = node;
    }
    last = node;
    inorder(node.right);
}
```
