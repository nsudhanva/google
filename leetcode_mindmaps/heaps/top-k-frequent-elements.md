# Top K Frequent Elements

**Problem Link:** [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
**Category:** Heaps

## Problem Understanding
- Return k most frequent elements

## Approach

### Bucket Sort
- Count frequencies
- Bucket by frequency
- Collect from highest buckets

## Implementation
```java
public int[] topKFrequent(int[] nums, int k) {
    Map<Integer, Integer> count = new HashMap<>();
    for (int num : nums) {
        count.put(num, count.getOrDefault(num, 0) + 1);
    }
    
    List<Integer>[] buckets = new List[nums.length + 1];
    for (int key : count.keySet()) {
        int freq = count.get(key);
        if (buckets[freq] == null) buckets[freq] = new ArrayList<>();
        buckets[freq].add(key);
    }
    
    int[] result = new int[k];
    int idx = 0;
    for (int i = buckets.length - 1; i >= 0 && idx < k; i--) {
        if (buckets[i] != null) {
            for (int num : buckets[i]) {
                result[idx++] = num;
                if (idx == k) break;
            }
        }
    }
    return result;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(n)
