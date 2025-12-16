# Snapshot array

## Problem Info
- **Link**: [Snapshot array](https://leetcode.com/problems/snapshot-array/description/)
- **Category**: Hashmaps & HashSets
- **Difficulty**: Medium
- **Status**: DONE

## Approach
### Data Structure
- Treemap

### Time Complexity
- O(nlogn+k)

## Things to Remember
- Bruteforce of storing every snapshot uses too much memory.
- Optimal: On set, store the value with snapID every time.
- On get, do a binary search to get the closest smaller snapid and value.
- Easily done with Treemaps in Java.
