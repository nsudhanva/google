# 3Sum

**Problem Link:** [3sum](https://leetcode.com/problems/3sum/)
**Category:** Google tagged

## Problem Understanding
- Find all unique triplets `[a, b, c]` where `a + b + c = 0`
- No duplicate triplets allowed

## Approach

### Sorting + Two Pointers
1. Sort array
2. Fix `nums[i]`, find pairs summing to `-nums[i]`
3. Skip duplicates at all levels

## Implementation
```java
public List<List<Integer>> threeSum(int[] nums) {
    Arrays.sort(nums);
    List<List<Integer>> result = new ArrayList<>();
    
    for (int i = 0; i < nums.length - 2; i++) {
        if (i > 0 && nums[i] == nums[i - 1]) continue;
        
        int left = i + 1, right = nums.length - 1;
        while (left < right) {
            int sum = nums[i] + nums[left] + nums[right];
            if (sum < 0) {
                left++;
            } else if (sum > 0) {
                right--;
            } else {
                result.add(Arrays.asList(nums[i], nums[left], nums[right]));
                while (left < right && nums[left] == nums[left + 1]) left++;
                while (left < right && nums[right] == nums[right - 1]) right--;
                left++;
                right--;
            }
        }
    }
    return result;
}
```

## Complexity
- **Time**: O(n²)
- **Space**: O(1) (excluding output)

## Key Insight
- Sorting enables Two Pointers and easy duplicate skipping
