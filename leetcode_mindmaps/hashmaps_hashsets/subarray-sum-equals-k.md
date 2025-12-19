# Subarray sum equals k

## Problem Info
- **Link**: [Subarray sum equals k](https://leetcode.com/problems/subarray-sum-equals-k/description/)
- **Category**: Hashmaps & HashSets
- **Difficulty**: Medium
- **Status**: DONE but REVISIT

## Problem Description
- Given an array of integers `nums` and an integer `k`, return _the total number of subarrays whose sum equals to_ `k`.
- A subarray is a contiguous **non-empty** sequence of elements within an array.
- **Example 1:**
- **Input:** nums = [1,1,1], k = 2
    **Output:** 2
    

**Example 2:**
- **Input:** nums = [1,2,3], k = 3
    **Output:** 2
- **Constraints:**
- * `1 <= nums.length <= 2 * 104`
  * `-1000 <= nums[i] <= 1000`
  * `-107 <= k <= 107`

## Approach
### Data Structure
- HashMap, prefix sum

### Time Complexity
- O(n)

## Things to Remember
- bruteforce O(n3), sum array precomputed O(n2), hashmap O(n).
- Not very intuitive.
- Basic Idea: create a hashmap with prefix sums from 0 to every index and the count of how many times that occurs.
- Also at each interation, look if the target (k - currSum) is already there in map.
- If so, add it to the count, then just add the currSum to the map with count.
