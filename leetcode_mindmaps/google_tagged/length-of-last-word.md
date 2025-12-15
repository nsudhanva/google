# Length of Last Word

**Problem Link:** [Length of Last Word](https://leetcode.com/problems/length-of-last-word/)
**Category:** Google tagged

## Problem Understanding
- Return length of last word (ignore trailing spaces)

## Approach

### Reverse Scan
- Skip trailing spaces, count chars until space

## Implementation
```java
public int lengthOfLastWord(String s) {
    int i = s.length() - 1;
    
    while (i >= 0 && s.charAt(i) == ' ') i--;
    
    int length = 0;
    while (i >= 0 && s.charAt(i) != ' ') {
        length++;
        i--;
    }
    return length;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
