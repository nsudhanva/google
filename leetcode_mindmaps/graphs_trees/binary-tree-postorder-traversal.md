# Post order

## Problem Info
- **Link**: [Post order](https://leetcode.com/problems/binary-tree-postorder-traversal/)
- **Category**: Graphs & Trees
- **Difficulty**: Easy
- **Status**: DONE

## Problem Description
- Given the `root` of a binary tree, return _the postorder traversal of its nodes ' values_.
- **Example 1:**
- **Input:** root = [1,null,2,3]
- **Output:** [3,2,1]
- **Explanation:**
- ![](https://assets.leetcode.com/uploads/2024/08/29/screenshot-2024-08-29-202743.png)
- **Example 2:**
- **Input:** root = [1,2,3,4,5,null,8,null,null,6,7,9]
- **Output:** [4,6,7,5,2,9,8,3,1]
- **Explanation:**
- ![](https://assets.leetcode.com/uploads/2024/08/29/tree_2.png)
- **Example 3:**
- **Input:** root = []
- **Output:** []
- **Example 4:**
- **Input:** root = [1]
- **Output:** [1]
- **Constraints:**
- * The number of the nodes in the tree is in the range `[0, 100]`.
  * `-100 <= Node.val <= 100`
- **Follow up:** Recursive solution is trivial, could you do it iteratively?

## Approach
### Data Structure
- Tree, DFS

### Time Complexity
- O(n)

## Things to Remember
- Little more complex - one while loop. maintain prev node and make right null when visited
