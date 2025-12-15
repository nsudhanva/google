# Find the Index of the First Occurrence in a String

**Problem Link:** [Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)
**Category:** Google tagged

## Problem Understanding
- Find first index of `needle` in `haystack`

## Approach

### Sliding Window
- Check each substring of length `needle.length()`

## Implementation
```java
public int strStr(String haystack, String needle) {
    if (needle.isEmpty()) return 0;
    
    for (int i = 0; i <= haystack.length() - needle.length(); i++) {
        if (haystack.substring(i, i + needle.length()).equals(needle)) {
            return i;
        }
    }
    return -1;
}
```

## Complexity
- **Time**: O(n * m)
- **Space**: O(1)
