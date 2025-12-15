# Container With Most Water

**Problem Link:** [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
**Category:** Google tagged

## Problem Understanding
- Find max area: `min(h[i], h[j]) * (j - i)`

## Approach

### Two Pointers
- Start at max width, move shorter line inward

## Implementation
```java
public int maxArea(int[] height) {
    int left = 0, right = height.length - 1;
    int maxArea = 0;
    
    while (left < right) {
        int area = Math.min(height[left], height[right]) * (right - left);
        maxArea = Math.max(maxArea, area);
        
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }
    return maxArea;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)

## Key Insight
- Moving shorter line might find taller; moving taller can only hurt
