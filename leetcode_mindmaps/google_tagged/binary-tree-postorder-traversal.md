# Binary Tree Postorder Traversal

**Problem Link:** [Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)
**Category:** Google tagged

## Problem Understanding
- Return postorder: Left -> Right -> Node

## Implementation
```java
public List<Integer> postorderTraversal(TreeNode root) {
    LinkedList<Integer> result = new LinkedList<>();
    Stack<TreeNode> stack = new Stack<>();
    if (root != null) stack.push(root);
    
    while (!stack.isEmpty()) {
        TreeNode node = stack.pop();
        result.addFirst(node.val);  // Add to front
        if (node.left != null) stack.push(node.left);
        if (node.right != null) stack.push(node.right);
    }
    return result;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(h)
