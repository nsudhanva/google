# Implement Stack using queue

## Problem Info
- **Link**: [Implement Stack using queue](https://leetcode.com/problems/implement-stack-using-queues/description/)
- **Category**: Stacks & Queues
- **Difficulty**: Easy
- **Status**: DONE

## Approach
### Data Structure
- Queue

### Time Complexity
- Either push or pop is O(n)

## Things to Remember
- Use 2 queues.
- Push - O(1) - just add to end and maintain top.
- Pop - O(n) - remove and add to a temp queue till except last element which should be poppped.
