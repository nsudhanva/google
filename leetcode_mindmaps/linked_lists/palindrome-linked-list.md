# Palindrome linked list

## Problem Info
- **Link**: [Palindrome linked list](https://leetcode.com/problems/palindrome-linked-list/description/)
- **Category**: Linked Lists
- **Difficulty**: Easy
- **Status**: DONE

## Problem Description
- Given the `head` of a singly linked list, return `true` _if it is a_ _palindrome_ _or_`false` _otherwise_.
- **Example 1:**
- ![](https://assets.leetcode.com/uploads/2021/03/03/pal1linked-list.jpg)
    
    
    **Input:** head = [1,2,2,1]
    **Output:** true
    

**Example 2:**
- ![](https://assets.leetcode.com/uploads/2021/03/03/pal2linked-list.jpg)
    
    
    **Input:** head = [1,2]
    **Output:** false
- **Constraints:**
- * The number of nodes in the list is in the range `[1, 105]`.
  * `0 <= Node.val <= 9`
- **Follow up:** Could you do it in `O(n)` time and `O(1)` space?

## Approach
### Data Structure
- Linked list

### Time Complexity
- O(n)

## Things to Remember
- I did it with slow and fast pointers and a stack.
- Can also be done in-place by reversing the second half and traversing.
