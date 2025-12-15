# Palindrome Number

**Problem Link:** [Palindrome Number](https://leetcode.com/problems/palindrome-number/)
**Category:** Google tagged

## Problem Understanding
- Check if integer is palindrome without string conversion

## Approach

### Revert Half Number
- Revert last half, compare with first half

## Implementation
```java
public boolean isPalindrome(int x) {
    if (x < 0 || (x % 10 == 0 && x != 0)) return false;
    
    int reversed = 0;
    while (x > reversed) {
        reversed = reversed * 10 + x % 10;
        x /= 10;
    }
    return x == reversed || x == reversed / 10;
}
```

## Complexity
- **Time**: O(log x)
- **Space**: O(1)
