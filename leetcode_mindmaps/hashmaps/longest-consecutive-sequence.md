# Longest Consecutive Sequence

**Problem Link:** [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)
**Category:** Hashmaps

## Implementation
```java
public int longestConsecutive(int[] nums) {
    Set<Integer> set = new HashSet<>();
    for (int n : nums) set.add(n);
    
    int longest = 0;
    for (int n : set) {
        if (!set.contains(n - 1)) {  // Start of sequence
            int curr = n, len = 1;
            while (set.contains(curr + 1)) {
                curr++;
                len++;
            }
            longest = Math.max(longest, len);
        }
    }
    return longest;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(n)
