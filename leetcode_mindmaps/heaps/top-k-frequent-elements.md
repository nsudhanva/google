# Top k frequent elements

## Problem Info
- **Link**: [Top k frequent elements](https://leetcode.com/problems/top-k-frequent-elements/)
- **Category**: Heaps
- **Difficulty**: Medium
- **Status**: DONE

## Approach
### Data Structure
- max heap

### Time Complexity
- O(n + nlogk)

## Things to Remember
- Brute force I came up with - count map, inverse map, convert to 2d array, sort based on count, return top k keys...
- Better: use a max heap - count map, inverse, insert count into prio queue, get top k.

## Additional Notes
- **imp note** prio queues HAVE to be traversed in a while loop with q.poll() or q.peek()
