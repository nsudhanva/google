# Subarray sum equals k

## Problem Info
- **Link**: [Subarray sum equals k](https://leetcode.com/problems/subarray-sum-equals-k/description/)
- **Category**: Hashmaps & HashSets
- **Difficulty**: Medium
- **Status**: DONE but REVISIT

## Approach
### Data Structure
- HashMap, prefix sum

### Time Complexity
- O(n)

## Things to Remember
- bruteforce O(n3), sum array precomputed O(n2), hashmap O(n).
- Not very intuitive.
- Basic Idea: create a hashmap with prefix sums from 0 to every index and the count of how many times that occurs.
- Also at each interation, look if the target (k - currSum) is already there in map.
- If so, add it to the count, then just add the currSum to the map with count.
