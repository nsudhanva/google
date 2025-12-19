# Palindrome Number

## Problem Info
- **Link**: [Palindrome Number](https://leetcode.com/problems/palindrome-number/description/)
- **Category**: Math/Bitwise
- **Difficulty**: Easy
- **Status**: DONE

## Problem Description
- Given an integer `x`, return `true` _if_`x` _is a_ _**palindrome**_ _, and_`false` _otherwise_.
- **Example 1:**
- **Input:** x = 121
    **Output:** true
    **Explanation:** 121 reads as 121 from left to right and from right to left.
    

**Example 2:**
- **Input:** x = -121
    **Output:** false
    **Explanation:** From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
    

**Example 3:**
- **Input:** x = 10
    **Output:** false
    **Explanation:** Reads 01 from right to left. Therefore it is not a palindrome.
- **Constraints:**
- * `-231 <= x <= 231 - 1`
- **Follow up:** Could you solve it without converting the integer to a string?

## Approach
### Data Structure
- Math

### Time Complexity
- O(logn)

## Things to Remember
- Bruteforce is to convert to string and check.
- Math is to compare half of x to the reversed second part.
- r = r * 10 + (x % 10).
