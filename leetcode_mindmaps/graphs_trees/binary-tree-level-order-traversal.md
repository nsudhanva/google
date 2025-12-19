# Level Order Traversal

## Problem Info
- **Link**: [Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- **Category**: Graphs & Trees
- **Difficulty**: Medium
- **Status**: DONE

## Problem Description
- Given the `root` of a binary tree, return _the level order traversal of its nodes ' values_. (i.e., from left to right, level by level).
- **Example 1:**
- ![](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)
    
    
    **Input:** root = [3,9,20,null,null,15,7]
    **Output:** [[3],[9,20],[15,7]]
    

**Example 2:**
- **Input:** root = [1]
    **Output:** [[1]]
    

**Example 3:**
- **Input:** root = []
    **Output:** []
- **Constraints:**
- * The number of nodes in the tree is in the range `[0, 2000]`.
  * `-1000 <= Node.val <= 1000`

## Approach
### Data Structure
- Tree, BFS

### Time Complexity
- O(n)

## Things to Remember
- Same as above. 2 while loops. the inner one is for each level
