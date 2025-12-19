# Isomorphic Strings

## Problem Info
- **Link**: [Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/description/)
- **Category**: Hashmaps & HashSets
- **Difficulty**: Easy
- **Status**: DONE

## Problem Description
- Given two strings `s` and `t`, _determine if they are isomorphic_.
- Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.
- All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
- **Example 1:**
- **Input:** s = "egg", t = "add"
- **Output:** true
- **Explanation:**
- The strings `s` and `t` can be made identical by:
- * Mapping `'e'` to `'a'`.
  * Mapping `'g'` to `'d'`.



**Example 2:**
- **Input:** s = "foo", t = "bar"
- **Output:** false
- **Explanation:**
- The strings `s` and `t` can not be made identical as `'o'` needs to be mapped to both `'a'` and `'r'`.
- **Example 3:**
- **Input:** s = "paper", t = "title"
- **Output:** true
- **Constraints:**
- * `1 <= s.length <= 5 * 104`
  * `t.length == s.length`
  * `s` and `t` consist of any valid ascii character.

## Approach
### Data Structure
- Hashset

### Time Complexity
- O(n)

## Things to Remember
- One soln - hashmap and set.
- second sol - transform both strings and compare.
- transofmration - create a string with index of first occurrence.
