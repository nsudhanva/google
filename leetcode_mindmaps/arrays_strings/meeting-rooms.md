# Meeting Rooms

**Problem Link:** [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/)
**Category:** Arrays & Strings

## Problem Understanding
- Can a person attend all meetings? (No overlap)

## Approach

### Sort and Compare Adjacent
- Sort by start time
- Check if any end > next start

## Implementation
```java
public boolean canAttendMeetings(int[][] intervals) {
    Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
    
    for (int i = 0; i < intervals.length - 1; i++) {
        if (intervals[i][1] > intervals[i + 1][0]) {
            return false;
        }
    }
    return true;
}
```

## Complexity
- **Time**: O(n log n)
- **Space**: O(1)
