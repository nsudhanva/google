# Pascals triangle

## Problem Info
- **Link**: [Pascals triangle](https://leetcode.com/problems/pascals-triangle/description/)
- **Category**: Recursion & DP
- **Difficulty**: Easy
- **Status**: DONE

## Problem Description
- Given an integer `numRows`, return the first numRows of **Pascal 's triangle**.
- In **Pascal 's triangle**, each number is the sum of the two numbers directly above it as shown:
- ![](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)
- **Example 1:**
- **Input:** numRows = 5
    **Output:** [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    

**Example 2:**
- **Input:** numRows = 1
    **Output:** [[1]]
- **Constraints:**
- * `1 <= numRows <= 30`

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
