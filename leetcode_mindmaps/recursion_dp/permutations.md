# Permutations

**Problem Link:** [Permutations](https://leetcode.com/problems/permutations/)
**Category:** Recursion & DP

## Problem Understanding
- Return all permutations of unique integers

## Approach

### Backtracking
- Track used elements with boolean array

## Implementation
```java
public List<List<Integer>> permute(int[] nums) {
    List<List<Integer>> result = new ArrayList<>();
    backtrack(result, new ArrayList<>(), nums, new boolean[nums.length]);
    return result;
}

private void backtrack(List<List<Integer>> result, List<Integer> path, 
                       int[] nums, boolean[] used) {
    if (path.size() == nums.length) {
        result.add(new ArrayList<>(path));
        return;
    }
    for (int i = 0; i < nums.length; i++) {
        if (used[i]) continue;
        used[i] = true;
        path.add(nums[i]);
        backtrack(result, path, nums, used);
        path.remove(path.size() - 1);
        used[i] = false;
    }
}
```

## Complexity
- **Time**: O(n * n!)
- **Space**: O(n)
