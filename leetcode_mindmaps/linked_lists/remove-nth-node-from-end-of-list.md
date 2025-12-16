# Remove nth node from list

## Problem Info
- **Link**: [Remove nth node from list](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/)
- **Category**: Linked Lists
- **Difficulty**: Medium
- **Status**: DONE

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
