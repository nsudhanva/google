# Minimum Depth of Binary Tree

**Problem Link:** [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)
**Category:** Google tagged

## Problem Understanding
- Find minimum depth (root to nearest leaf)

## Approach
### BFS (Optimal for min depth)
- Stop at first leaf found

## Implementation
```java
public int minDepth(TreeNode root) {
    if (root == null) return 0;
    Queue<TreeNode> queue = new LinkedList<>();
    queue.offer(root);
    int depth = 1;
    
    while (!queue.isEmpty()) {
        int size = queue.size();
        for (int i = 0; i < size; i++) {
            TreeNode node = queue.poll();
            if (node.left == null && node.right == null) return depth;
            if (node.left != null) queue.offer(node.left);
            if (node.right != null) queue.offer(node.right);
        }
        depth++;
    }
    return depth;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(n)
