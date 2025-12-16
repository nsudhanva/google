# Design a hit counter

## Problem Info
- **Link**: [Design a hit counter](https://leetcode.com/problems/design-hit-counter/description/)
- **Category**: Stacks & Queues
- **Difficulty**: Medium
- **Status**: DONE

## Approach
### Data Structure
- Queue, Deque

### Time Complexity
- O(n) worst case

## Things to Remember
- I did this using a hashmap with timestamp to count - but not very efficient.
- Assuming timestamps are always increasing, we can use queues.

## Additional Notes
- Queue: Hit: just add to queue. GetHits: check first, if diff>=300, remove it in loop. then return size. Deque: use deque with pairs of timestamp and count. Hit: check last element, if same timestamp, inc count, remove and add new pair, otherwise just add. GetHits: similar to queue. One diff - maintain a total variable.
