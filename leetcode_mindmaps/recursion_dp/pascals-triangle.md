# Pascals triangle

## Problem Info
- **Link**: [Pascals triangle](https://leetcode.com/problems/pascals-triangle/description/)
- **Category**: Recursion & DP
- **Difficulty**: Easy
- **Status**: DONE

## Approach
### Data Structure
- DP, Iterative

### Time Complexity
- O(n2)

## Things to Remember
- Iterative DP: Idea is to use prev row to calculate the current row.
- So you go through each row twice - once when building it and once when building next row, hence O(n2).

## Additional Notes
- currRow.add(prevRow.get(j - 1) + prevRow.get(j));
