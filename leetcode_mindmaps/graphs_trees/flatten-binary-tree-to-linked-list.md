# Flatten Binary Tree to Linked List

**Problem Link:** [Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)
**Category:** Graphs & Trees

## Implementation
```java
public void flatten(TreeNode root) {
    TreeNode curr = root;
    while (curr != null) {
        if (curr.left != null) {
            TreeNode rightmost = curr.left;
            while (rightmost.right != null) rightmost = rightmost.right;
            rightmost.right = curr.right;
            curr.right = curr.left;
            curr.left = null;
        }
        curr = curr.right;
    }
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
