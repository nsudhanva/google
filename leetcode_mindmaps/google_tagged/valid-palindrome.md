# Valid Palindrome

**Problem Link:** [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
**Category:** Google tagged

## Problem Understanding
- Check if string is palindrome (alphanumeric only, case-insensitive)

## Approach

### Two Pointers
- Compare from both ends, skip non-alphanumeric

## Implementation
```java
public boolean isPalindrome(String s) {
    int left = 0, right = s.length() - 1;
    
    while (left < right) {
        while (left < right && !Character.isLetterOrDigit(s.charAt(left))) left++;
        while (left < right && !Character.isLetterOrDigit(s.charAt(right))) right--;
        
        if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
