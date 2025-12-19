# Valid Palindrome II

## Problem Info
- **Link**: [Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/)
- **Category**: Arrays & Strings
- **Difficulty**: Easy
- **Status**: DONE

## Problem Description
- Given a string `s`, return `true` _if the_`s` _can be palindrome after deleting**at most one** character from it_.
- **Example 1:**
- **Input:** s = "aba"
    **Output:** true
    

**Example 2:**
- **Input:** s = "abca"
    **Output:** true
    **Explanation:** You could delete the character 'c'.
    

**Example 3:**
- **Input:** s = "abc"
    **Output:** false
- **Constraints:**
- * `1 <= s.length <= 105`
  * `s` consists of lowercase English letters.

## Approach
### Data Structure
- Two Pointers, greedy

### Time Complexity
- O(n)

## Things to Remember
- Use a separate method to check palindrome when there is a mismatch
