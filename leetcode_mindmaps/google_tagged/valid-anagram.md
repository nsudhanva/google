# Valid Anagram

**Problem Link:** [Valid Anagram](https://leetcode.com/problems/valid-anagram/)
**Category:** Google tagged

## Problem Understanding
- Check if `t` is anagram of `s` (same chars, same counts)

## Approach

### Frequency Count
- Count chars in both strings, compare

## Implementation
```java
public boolean isAnagram(String s, String t) {
    if (s.length() != t.length()) return false;
    
    int[] count = new int[26];
    for (int i = 0; i < s.length(); i++) {
        count[s.charAt(i) - 'a']++;
        count[t.charAt(i) - 'a']--;
    }
    
    for (int c : count) {
        if (c != 0) return false;
    }
    return true;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(1) (26 letters)
