# Sqrt(x)

**Problem Link:** [Sqrt(x)](https://leetcode.com/problems/sqrtx/)
**Category:** Google tagged

## Problem Understanding
- Return floor of square root without using `Math.sqrt`

## Approach

### Binary Search
- Search for `k` where `k*k <= x < (k+1)*(k+1)`

## Implementation
```java
public int mySqrt(int x) {
    if (x < 2) return x;
    
    long left = 2, right = x / 2;
    while (left <= right) {
        long mid = left + (right - left) / 2;
        long sq = mid * mid;
        
        if (sq == x) return (int) mid;
        if (sq < x) left = mid + 1;
        else right = mid - 1;
    }
    return (int) right;
}
```

## Complexity
- **Time**: O(log x)
- **Space**: O(1)
