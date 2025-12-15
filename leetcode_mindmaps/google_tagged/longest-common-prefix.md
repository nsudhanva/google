# Longest Common Prefix

**Problem Link:** [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)
**Category:** Google tagged

## Problem Understanding
- Find longest prefix common to all strings

## Approach

### Horizontal Scanning
- Start with first string as prefix
- Shrink until it matches start of each string

## Implementation
```java
public String longestCommonPrefix(String[] strs) {
    if (strs == null || strs.length == 0) return "";
    
    String prefix = strs[0];
    for (int i = 1; i < strs.length; i++) {
        while (strs[i].indexOf(prefix) != 0) {
            prefix = prefix.substring(0, prefix.length() - 1);
            if (prefix.isEmpty()) return "";
        }
    }
    return prefix;
}
```

## Complexity
- **Time**: O(S) where S is sum of all chars
- **Space**: O(1)
