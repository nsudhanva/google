# Index of first occurrence in a string

## Problem Info
- **Link**: [Index of first occurrence in a string](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/)
- **Category**: Hashmaps & HashSets
- **Difficulty**: Easy
- **Status**: DONE but REVISIT

## Problem Description
- Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.
- **Example 1:**
- **Input:** haystack = "sadbutsad", needle = "sad"
    **Output:** 0
    **Explanation:** "sad" occurs at index 0 and 6.
    The first occurrence is at index 0, so we return 0.
    

**Example 2:**
- **Input:** haystack = "leetcode", needle = "leeto"
    **Output:** -1
    **Explanation:** "leeto" did not occur in "leetcode", so we return -1.
- **Constraints:**
- * `1 <= haystack.length, needle.length <= 104`
  * `haystack` and `needle` consist of only lowercase English characters.

## Approach
### Data Structure
- Hashing

### Time Complexity
- O(nm)

## Things to Remember
- I used substring method - but that is brute force.
- Other way is hasing each character, checking the hash of each substring and only if it matches, compare chars.
- but that also in worst case is the same complexity.
- There is another way with O(n) but very complex - revisit.
