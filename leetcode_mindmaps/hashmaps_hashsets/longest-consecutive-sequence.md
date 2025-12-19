# Longest Consecutive sequence

## Problem Info
- **Link**: [Longest Consecutive sequence](https://leetcode.com/problems/longest-consecutive-sequence/description/)
- **Category**: Hashmaps & HashSets
- **Difficulty**: Medium
- **Status**: DONE but REVISIT

## Problem Description
- Given an unsorted array of integers `nums`, return _the length of the longest consecutive elements sequence._
- You must write an algorithm that runs in `O(n)` time.
- **Example 1:**
- **Input:** nums = [100,4,200,1,3,2]
    **Output:** 4
    **Explanation:** The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
    

**Example 2:**
- **Input:** nums = [0,3,7,2,5,8,4,6,0,1]
    **Output:** 9
    

**Example 3:**
- **Input:** nums = [1,0,1,2]
    **Output:** 3
- **Constraints:**
- * `0 <= nums.length <= 105`
  * `-109 <= nums[i] <= 109`

## Approach
### Data Structure
- BFS Solution was more intuitive

### Time Complexity
- O(n)

## Things to Remember
- Bruteforce - sort and check every consecutive while maintaining max.
- BFS - visualize as graph, create adj by adding list of prev and next numbers if exists, then maintain visted, for each key and not visited, add to q, while q not empty, remove, and for each nei not visited, add to q while inc size.
