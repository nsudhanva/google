# Middle of the Linked List

**Problem Link:** [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)

**Category:** Google tagged

## Problem Understanding
- Input: Head of linked list.
- Output: Middle node. (If two, second middle).

## Approach

### Two Pointers (Fast/Slow)
- **Idea**: Fast moves 2 steps, Slow moves 1 step. When Fast hits end, Slow is at middle.
- **Algorithm**:
  - `slow = fast = head`
  - While `fast` and `fast.next`:
    - `slow = slow.next`
    - `fast = fast.next.next`
  - Return `slow`

### Count Length
- **Idea**: Count `n`. Return node at `n // 2`.
- **Complexity**: 1.5 passes.

## Implementation
- **Python**:
  ```python
  slow = fast = head
  while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
  return slow
  ```

## Complexity Analysis
- **Time**: O(n)
- **Space**: O(1)

## Common Pitfalls
- **Loop Condition**: `fast and fast.next` guarantees valid `fast.next.next` isn't accessed on null.

## Key Patterns
- **Fast/Slow Pointers**: Cycle detection, Middle finding.
