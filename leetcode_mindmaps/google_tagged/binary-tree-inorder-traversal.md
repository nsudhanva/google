# Binary Tree Inorder Traversal

**Problem Link:** [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
**Category:** Google tagged

## Problem Understanding
- Return inorder traversal: Left -> Node -> Right

## Approach

### Iterative (Stack)
- Push all lefts, pop one, go right

## Implementation
```java
public List<Integer> inorderTraversal(TreeNode root) {
    List<Integer> result = new ArrayList<>();
    Stack<TreeNode> stack = new Stack<>();
    TreeNode curr = root;
    
    while (curr != null || !stack.isEmpty()) {
        while (curr != null) {
            stack.push(curr);
            curr = curr.left;
        }
        curr = stack.pop();
        result.add(curr.val);
        curr = curr.right;
    }
    return result;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(h)
