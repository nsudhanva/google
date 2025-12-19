# Remove nth node from list

## Problem Info
- **Link**: [Remove nth node from list](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/)
- **Category**: Linked Lists
- **Difficulty**: Medium
- **Status**: DONE

## Problem Description
- Given the `head` of a linked list, remove the `nth` node from the end of the list and return its head.
- **Example 1:**
- ![](https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg)
    
    
    **Input:** head = [1,2,3,4,5], n = 2
    **Output:** [1,2,3,5]
    

**Example 2:**
- **Input:** head = [1], n = 1
    **Output:** []
    

**Example 3:**
- **Input:** head = [1,2], n = 1
    **Output:** [1]
- **Constraints:**
- * The number of nodes in the list is `sz`.
  * `1 <= sz <= 30`
  * `0 <= Node.val <= 100`
  * `1 <= n <= sz`
- **Follow up:** Could you do this in one pass?

## Approach
### Data Structure
- Linked List

### Time Complexity
- O(L)

## Things to Remember
- Need a dummy node at the start in case head is to be removed.
- I solved it by finding the length and then traversing till there again to remove.

## Additional Notes
- One pass algo: have a dummy node, maintain two pointers. Move the first pointer to the n+1th node so that the gap b/w the two pointers is n nodes. Then till first pointer becomes null, advance both of them together. At that point, second ptr will be at (L-n)th node. remove that node
