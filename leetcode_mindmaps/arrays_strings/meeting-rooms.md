# Meeting rooms

## Problem Info
- **Link**: [Meeting rooms](https://leetcode.com/problems/meeting-rooms/)
- **Category**: Arrays & Strings
- **Difficulty**: Easy
- **Status**: DONE

## Approach
### Data Structure
- Arrays, sorting

### Time Complexity
- O(nlogn)

## Things to Remember
- Sort based on start times and then check for overlapping meetings

## Additional Notes
- Arrays.sort(intervals, (a,b) -> Integer.compare(a[0], b[0])); ---- sorting based on start times
