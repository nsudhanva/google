# Reverse Polish Notation

## Problem Info
- **Link**: [Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/description/)
- **Category**: Stacks & Queues
- **Difficulty**: Medium
- **Status**: DONE

## Approach
### Data Structure
- Stack

### Time Complexity
- O(n)

## Things to Remember
- Keep pushing till you reach an operator, push the result back

## Additional Notes
- Brute force is to do string manipulation - keep traversing till you find an operator, then take prev 2 numbers and evaluate. O(n2)
