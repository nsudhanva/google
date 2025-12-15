# Majority Element

**Problem Link:** [Majority Element](https://leetcode.com/problems/majority-element/)
**Category:** Google tagged

## Problem Understanding
- Find element appearing more than n/2 times

## Approach

### Boyer-Moore Voting Algorithm
- Cancel out different elements
- Majority survives because count > n/2

## Implementation
```java
public int majorityElement(int[] nums) {
    int candidate = 0, count = 0;
    
    for (int num : nums) {
        if (count == 0) {
            candidate = num;
        }
        count += (num == candidate) ? 1 : -1;
    }
    return candidate;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
