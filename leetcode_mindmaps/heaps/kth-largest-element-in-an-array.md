# Kth Largest Element in an Array

**Problem Link:** [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)

**Category:** Heaps

## Problem Understanding
- Input: Array `nums`, integer `k`.
- Output: `k`th largest element.
- Example: `[3,2,1,5,6,4]`, k=2 -> 5.

## Approach

### Sorting (Naive)
- **Idea**: Sort descending, take index `k-1`.
- **Complexity**: O(N log N).

### Min Heap (Optimal for Streaming)
- **Idea**: Keep a heap of size `k` tracking the largest elements seen so far. The top will be the `k`th largest (smallest of the top k).
- **Algorithm**:
  - Init Min Heap.
  - For `num` in `nums`:
    - `heappush(num)`
    - If `size > k`: `heappop()`
  - Return `heap[0]`
- **Complexity**: O(N log k). Better than sorting if k < N.

### Quickselect (Hoare's Selection)
- **Idea**: Partition array like Quicksort.
- **Algorithm**:
  - Choose pivot.
  - Partition: `< pivot`, `> pivot`.
  - Recurse into side containing target index `n-k`.
- **Complexity**: O(N) Average, O(N^2) Worst.

## Implementation (Min Heap)
- **Python**:
  ```python
  import heapq
  heap = []
  for n in nums:
      heapq.heappush(heap, n)
      if len(heap) > k:
          heapq.heappop(heap)
  return heap[0]
  ```

## Complexity Analysis
- **Time**: O(N log k)
- **Space**: O(k)

## Common Pitfalls
- **Min vs Max Heap**: To find k-th *largest*, use *Min* Heap of size k (keeps largest elements, pops smallest of them). To find k-th *smallest*, use *Max* Heap of size k.

## Key Patterns
- **Top K Pattern**: Use Heap.
