# Contains Duplicate

**Problem Link:** [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
**Category:** Google tagged

## Problem Understanding
- Return true if any value appears twice

## Approach

### HashSet
- Add to set, check if already exists

## Implementation
```java
public boolean containsDuplicate(int[] nums) {
    Set<Integer> seen = new HashSet<>();
    for (int num : nums) {
        if (seen.contains(num)) return true;
        seen.add(num);
    }
    return false;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(n)
