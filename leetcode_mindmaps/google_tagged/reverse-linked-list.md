# Reverse Linked List

**Problem Link:** [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

**Category:** Google tagged

## Problem Understanding
- Input: Head of singly linked list.
- Output: New head of reversed list.
- Example: `1->2->3->4->5` -> `5->4->3->2->1`.

## Approach

### Iterative (Optimal)
- **Idea**: Change pointers one by one as we traverse.
- **Algorithm**:
  - `prev = None`, `curr = head`
  - While `curr`:
    - `temp = curr.next` (Save next)
    - `curr.next = prev` (Reverse link)
    - `prev = curr` (Move prev)
    - `curr = temp` (Move curr)
  - Return `prev` (New head)

### Recursive
- **Idea**: Reverse rest of list, then make current node point to null.
- **Algorithm**:
  - Base: If `!head` or `!head.next`: return `head`
  - `p = reverse(head.next)`
  - `head.next.next = head` (Make next point back to me)
  - `head.next = None` (Break forward link)
  - Return `p`

## Implementation
- **Python**:
  ```python
  prev = None
  curr = head
  while curr:
      temp = curr.next
      curr.next = prev
      prev = curr
      curr = temp
  return prev
  ```

## Complexity Analysis
- **Time**: O(n)
- **Space**: O(1) Iterative, O(n) Recursive (Stack).

## Common Pitfalls
- **Lost Reference**: Overwriting `curr.next` before saving `curr.next`.
- **Return Value**: Returning `head` (which is now tail) instead of `prev`.

## Key Patterns
- **Pointer Manipulation**: Standard linked list skill.
