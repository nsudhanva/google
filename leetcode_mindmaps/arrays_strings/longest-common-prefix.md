# Longest Common Prefix

## Problem Info
- **Link**: [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)
- **Category**: Arrays & Strings
- **Difficulty**: Easy
- **Status**: DONE

## Problem Description
- Write a function to find the longest common prefix string amongst an array of strings.
- If there is no common prefix, return an empty string `""`.
- **Example 1:**
- **Input:** strs = ["flower","flow","flight"]
    **Output:** "fl"
    

**Example 2:**
- **Input:** strs = ["dog","racecar","car"]
    **Output:** ""
    **Explanation:** There is no common prefix among the input strings.
- **Constraints:**
- * `1 <= strs.length <= 200`
  * `0 <= strs[i].length <= 200`
  * `strs[i]` consists of only lowercase English letters if it is non-empty.

## Approach
### Data Structure
- String / Binary Search

### Time Complexity
- O(S)

## Things to Remember
- Assign first string to lcp.
- then loop through other strings.
- if the str already starts with lcp, continue.
- otherwise find the common substring between str and lcp and make that the new lcp.
- Note: this can also be solved using Binary Search.
