# Valid Palindrome

## Problem Info
- **Link**: [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
- **Category**: Arrays & Strings
- **Difficulty**: Easy
- **Status**: DONE

## Problem Description
- A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
- Given a string `s`, return `true` _if it is a**palindrome** , or _`false` _otherwise_.
- **Example 1:**
- **Input:** s = "A man, a plan, a canal: Panama"
    **Output:** true
    **Explanation:** "amanaplanacanalpanama" is a palindrome.
    

**Example 2:**
- **Input:** s = "race a car"
    **Output:** false
    **Explanation:** "raceacar" is not a palindrome.
    

**Example 3:**
- **Input:** s = " "
    **Output:** true
    **Explanation:** s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.
- **Constraints:**
- * `1 <= s.length <= 2 * 105`
  * `s` consists only of printable ASCII characters.

## Approach
### Data Structure
- Two pointers

### Time Complexity
- O(n)

## Things to Remember
- pointers at start and end, check for alphanumeric along the way.
- Another way is to build the reverse and compare.
