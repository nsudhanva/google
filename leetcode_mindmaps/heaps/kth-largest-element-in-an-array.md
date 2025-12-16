# kth largest element in an array

## Problem Info
- **Link**: [kth largest element in an array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- **Category**: Heaps
- **Difficulty**: Medium
- **Status**: DONE

## Approach
### Data Structure
- min heap

### Time Complexity
- O(nlogk) / O(n)

## Things to Remember
- Similar to #1.
- Can be done with max heap and poll till we hit k.
- Or use a min heap and only insert if < size k (so min heap of size k).

## Additional Notes
- Another soln: quick select: similar to quick sort - choose a pivot element (rightmost). Go through the array, if nums[i] is less than pivot, then swap with p otherwise keep as is. after the loop, swap pivot with p element. Then do it recursively till k == p. Average time O(n) but worst time O(n2)
