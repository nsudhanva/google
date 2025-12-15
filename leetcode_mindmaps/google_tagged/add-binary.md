# Add Binary

**Problem Link:** [Add Binary](https://leetcode.com/problems/add-binary/)
**Category:** Google tagged

## Problem Understanding
- Add two binary strings, return sum as binary string

## Approach
### Simulation with Carry
- Process from right to left, track carry

## Implementation
```java
public String addBinary(String a, String b) {
    StringBuilder sb = new StringBuilder();
    int i = a.length() - 1, j = b.length() - 1, carry = 0;
    
    while (i >= 0 || j >= 0 || carry != 0) {
        int sum = carry;
        if (i >= 0) sum += a.charAt(i--) - '0';
        if (j >= 0) sum += b.charAt(j--) - '0';
        sb.append(sum % 2);
        carry = sum / 2;
    }
    return sb.reverse().toString();
}
```

## Complexity
- **Time**: O(max(m, n))
- **Space**: O(max(m, n))
