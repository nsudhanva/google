# Move Zeroes

**Problem Link:** [Move Zeroes](https://leetcode.com/problems/move-zeroes/)
**Category:** Google tagged

## Problem Understanding
- Move all 0s to end, maintain relative order of non-zeros

## Approach

### Two Pointers (Swap)
- `pos` tracks where next non-zero should go
- Swap non-zeros to front

## Implementation
```java
public void moveZeroes(int[] nums) {
    int pos = 0;
    for (int i = 0; i < nums.length; i++) {
        if (nums[i] != 0) {
            int temp = nums[pos];
            nums[pos] = nums[i];
            nums[i] = temp;
            pos++;
        }
    }
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
