# Binary Tree Inorder Traversal

**Problem Link:** [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)

**Category:** Google tagged

## Problem Understanding
- Input: Root of binary tree
- Output: List of values (Left -> Node -> Right)

## Approach

### Recursive
- **Idea**: `dfs(node.left) -> visit(node) -> dfs(node.right)`
- **Complexity**: O(n), Space O(h).

### Iterative (Stack)
- **Idea**: Simulate recursion stack.
- **Algorithm**:
  - `curr = root`, `stack = []`
  - While `curr` or `stack`:
    - While `curr`: push `curr`, `curr = curr.left`
    - `curr = stack.pop()`
    - Visit `curr.val`
    - `curr = curr.right`

### Morris Traversal (Space Optimal)
- **Idea**: Use threaded binary tree (links to successor).
- **Complexity**: O(n) Time, O(1) Space.

## Implementation (Recursive)
- **Python**:
  ```python
  def inorder(root):
      return inorder(root.left) + [root.val] + inorder(root.right) if root else []
  ```

## Implementation (Iterative)
- **Python**:
  ```python
  res, stack = [], []
  curr = root
  while curr or stack:
      while curr:
          stack.append(curr)
          curr = curr.left
      curr = stack.pop()
      res.append(curr.val)
      curr = curr.right
  return res
  ```

## Complexity Analysis
- **Time**: O(n)
- **Space**: O(h)

## Common Pitfalls
- **Stack Logic**: Push all lefts, then pop one, then move right.

## Key Patterns
- **DFS**: Standard traversal.
