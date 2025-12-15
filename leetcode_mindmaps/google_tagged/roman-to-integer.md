# Roman to Integer

**Problem Link:** [Roman to Integer](https://leetcode.com/problems/roman-to-integer/)
**Category:** Google tagged

## Problem Understanding
- Convert Roman numeral string to integer
- Handle subtraction cases (IV, IX, XL, XC, CD, CM)

## Approach

### Right-to-Left Pass
- If current < previous, subtract; else add

## Implementation
```java
public int romanToInt(String s) {
    Map<Character, Integer> map = Map.of(
        'I', 1, 'V', 5, 'X', 10, 'L', 50,
        'C', 100, 'D', 500, 'M', 1000
    );
    
    int total = 0, prev = 0;
    for (int i = s.length() - 1; i >= 0; i--) {
        int curr = map.get(s.charAt(i));
        total += (curr < prev) ? -curr : curr;
        prev = curr;
    }
    return total;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
