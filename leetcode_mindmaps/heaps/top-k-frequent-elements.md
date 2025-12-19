# Top k frequent elements

## Problem Info
- **Link**: [Top k frequent elements](https://leetcode.com/problems/top-k-frequent-elements/)
- **Category**: Heaps
- **Difficulty**: Medium
- **Status**: DONE

## Problem Description
- Given an integer array `nums` and an integer `k`, return _the_ `k` _most frequent elements_. You may return the answer in **any order**.
- **Example 1:**
- **Input:** nums = [1,1,1,2,2,3], k = 2
- **Output:** [1,2]
- **Example 2:**
- **Input:** nums = [1], k = 1
- **Output:** [1]
- **Example 3:**
- **Input:** nums = [1,2,1,2,1,2,3,1,3,2], k = 2
- **Output:** [1,2]
- **Constraints:**
- * `1 <= nums.length <= 105`
  * `-104 <= nums[i] <= 104`
  * `k` is in the range `[1, the number of unique elements in the array]`.
  * It is **guaranteed** that the answer is **unique**.
- **Follow up:** Your algorithm's time complexity must be better than `O(n log n)`, where n is the array's size.

## Approach
### Data Structure
- max heap

### Time Complexity
- O(n + nlogk)

## Things to Remember
- Brute force I came up with - count map, inverse map, convert to 2d array, sort based on count, return top k keys...
- Better: use a max heap - count map, inverse, insert count into prio queue, get top k.

## Additional Notes
- **imp note** prio queues HAVE to be traversed in a while loop with q.poll() or q.peek()
