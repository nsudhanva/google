# Meeting Rooms II

**Problem Link:** [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)
**Category:** Heaps

## Problem Understanding
- Find minimum meeting rooms needed

## Approach

### Min Heap (End Times)
- Sort by start time
- Heap tracks earliest ending meeting
- If new start >= heap top, reuse room (poll); else need new room

## Implementation
```java
public int minMeetingRooms(int[][] intervals) {
    if (intervals.length == 0) return 0;
    
    Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
    PriorityQueue<Integer> heap = new PriorityQueue<>();
    heap.offer(intervals[0][1]);
    
    for (int i = 1; i < intervals.length; i++) {
        if (intervals[i][0] >= heap.peek()) {
            heap.poll();
        }
        heap.offer(intervals[i][1]);
    }
    return heap.size();
}
```

## Complexity
- **Time**: O(n log n)
- **Space**: O(n)
