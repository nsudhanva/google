# Plus One

**Problem Link:** [Plus One](https://leetcode.com/problems/plus-one/)
**Category:** Google tagged

## Problem Understanding
- Array represents integer, add 1 to it

## Approach

### Reverse Loop with Carry
- Start from end, handle 9s specially

## Implementation
```java
public int[] plusOne(int[] digits) {
    for (int i = digits.length - 1; i >= 0; i--) {
        if (digits[i] < 9) {
            digits[i]++;
            return digits;
        }
        digits[i] = 0;
    }
    
    // All 9s case
    int[] result = new int[digits.length + 1];
    result[0] = 1;
    return result;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
