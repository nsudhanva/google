# Trapping Rain Water

**Problem Link:** [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)
**Category:** Stacks & Queues

## Problem Understanding
- Calculate water trapped between bars

## Approach

### Two Pointers
- Track leftMax and rightMax
- Water at i = min(leftMax, rightMax) - height[i]

## Implementation
```java
public int trap(int[] height) {
    int left = 0, right = height.length - 1;
    int leftMax = 0, rightMax = 0;
    int water = 0;
    
    while (left < right) {
        if (height[left] < height[right]) {
            if (height[left] >= leftMax) {
                leftMax = height[left];
            } else {
                water += leftMax - height[left];
            }
            left++;
        } else {
            if (height[right] >= rightMax) {
                rightMax = height[right];
            } else {
                water += rightMax - height[right];
            }
            right--;
        }
    }
    return water;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
