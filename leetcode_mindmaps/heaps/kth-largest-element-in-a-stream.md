# kth largest element in a stream

## Problem Info
- **Link**: [kth largest element in a stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/description/)
- **Category**: Heaps
- **Difficulty**: Easy
- **Status**: DONE

## Approach
### Data Structure
- min heap

### Time Complexity
- O(n logk)

## Things to Remember
- Use a min heap of size k. then the kth largest will always be at the root

## Additional Notes
- minheap - new PriorityQueue<>();     maxheap - new PriorityQueue<>(Collections.reverseOrder());
