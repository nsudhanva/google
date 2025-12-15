# Subarray Sum Equals K

**Problem Link:** [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)
**Category:** Hashmaps

## Problem Understanding
- Count subarrays with sum = k

## Approach

### Prefix Sum + HashMap
- If `prefix[j] - prefix[i] = k`, subarray i+1 to j sums to k

## Implementation
```java
public int subarraySum(int[] nums, int k) {
    int count = 0, prefixSum = 0;
    Map<Integer, Integer> prefixCounts = new HashMap<>();
    prefixCounts.put(0, 1);
    
    for (int num : nums) {
        prefixSum += num;
        count += prefixCounts.getOrDefault(prefixSum - k, 0);
        prefixCounts.put(prefixSum, prefixCounts.getOrDefault(prefixSum, 0) + 1);
    }
    return count;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(n)
