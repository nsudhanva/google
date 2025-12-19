# kth largest element in an array

## Problem Info
- **Link**: [kth largest element in an array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- **Category**: Heaps
- **Difficulty**: Medium
- **Status**: DONE

## Problem Description
- Given an integer array `nums` and an integer `k`, return _the_ `kth` _largest element in the array_.
- Note that it is the `kth` largest element in the sorted order, not the `kth` distinct element.
- Can you solve it without sorting?
- **Example 1:**
- **Input:** nums = [3,2,1,5,6,4], k = 2
    **Output:** 5
    

**Example 2:**
- **Input:** nums = [3,2,3,1,2,4,5,5,6], k = 4
    **Output:** 4
- **Constraints:**
- * `1 <= k <= nums.length <= 105`
  * `-104 <= nums[i] <= 104`

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
