# Longest Increasing Subsequence

**Problem Link:** [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
**Category:** Recursion & DP

## Problem Understanding
- Find length of longest strictly increasing subsequence

## Approach

### Binary Search + DP
- Maintain array of smallest tail for each length

## Implementation
```java
public int lengthOfLIS(int[] nums) {
    List<Integer> tails = new ArrayList<>();
    
    for (int num : nums) {
        int pos = Collections.binarySearch(tails, num);
        if (pos < 0) pos = -(pos + 1);
        
        if (pos == tails.size()) {
            tails.add(num);
        } else {
            tails.set(pos, num);
        }
    }
    return tails.size();
}
```

## Complexity
- **Time**: O(n log n)
- **Space**: O(n)
