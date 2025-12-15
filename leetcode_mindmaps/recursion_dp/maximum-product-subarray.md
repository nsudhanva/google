# Maximum Product Subarray

**Problem Link:** [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)
**Category:** Recursion & DP

## Problem Understanding
- Find contiguous subarray with largest product

## Approach
### Track Min and Max
- Negative * Negative can become max

## Implementation
```java
public int maxProduct(int[] nums) {
    int maxProd = nums[0], minProd = nums[0], result = nums[0];
    
    for (int i = 1; i < nums.length; i++) {
        if (nums[i] < 0) {
            int temp = maxProd;
            maxProd = minProd;
            minProd = temp;
        }
        maxProd = Math.max(nums[i], maxProd * nums[i]);
        minProd = Math.min(nums[i], minProd * nums[i]);
        result = Math.max(result, maxProd);
    }
    return result;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
