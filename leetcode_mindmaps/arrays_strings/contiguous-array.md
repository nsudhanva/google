# Contiguous Array

## Problem Info
- **Link**: [Contiguous Array](https://leetcode.com/problems/contiguous-array/description/)
- **Category**: Arrays & Strings
- **Difficulty**: Medium
- **Status**: DONE

## Problem Description
- Given a binary array `nums`, return _the maximum length of a contiguous subarray with an equal number of_`0` _and_`1`.
- **Example 1:**
- **Input:** nums = [0,1]
    **Output:** 2
    **Explanation:** [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
    

**Example 2:**
- **Input:** nums = [0,1,0]
    **Output:** 2
    **Explanation:** [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
    

**Example 3:**
- **Input:** nums = [0,1,1,1,1,1,0,0,0]
    **Output:** 6
    **Explanation:** [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.
- **Constraints:**
- * `1 <= nums.length <= 105`
  * `nums[i]` is either `0` or `1`.

## Approach
### Data Structure
- Prefix sum, Hashmap

### Time Complexity
- O(n)

## Things to Remember
- Create a sums array by adding 1 if you find 1 and sub 1 if you find a 0.
- Then this sums array will have same sum when it has found contiguous 0s and 1s.
- Use a hashmap to store first occurrence of each sum to find maxLen.
