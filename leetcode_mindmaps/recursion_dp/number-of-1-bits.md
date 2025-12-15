# Number of 1 Bits

**Problem Link:** [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)
**Category:** Recursion & DP

## Implementation
```java
public int hammingWeight(int n) {
    int count = 0;
    while (n != 0) {
        count += (n & 1);
        n >>>= 1;
    }
    return count;
}
```

## Complexity
- **Time**: O(32) = O(1)
- **Space**: O(1)
