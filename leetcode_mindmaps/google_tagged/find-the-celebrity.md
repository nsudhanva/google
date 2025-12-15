# Find the Celebrity

**Problem Link:** [Find the Celebrity](https://leetcode.com/problems/find-the-celebrity/)
**Category:** Google tagged

## Approach
- Celebrity: everyone knows them, they know no one

## Implementation
```java
public int findCelebrity(int n) {
    int candidate = 0;
    for (int i = 1; i < n; i++) {
        if (knows(candidate, i)) candidate = i;
    }
    for (int i = 0; i < n; i++) {
        if (i != candidate) {
            if (knows(candidate, i) || !knows(i, candidate)) return -1;
        }
    }
    return candidate;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
