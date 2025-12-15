#!/usr/bin/env python3
"""
Generate problem-specific mindmaps for all LeetCode problems.
This creates high-quality, specific content for each problem.
"""

import json
import os
import re
from pathlib import Path

# Problem-specific content database
PROBLEM_CONTENT = {
    # ============ GOOGLE TAGGED ============
    "two-sum": """# Two Sum

**Problem Link:** [Two Sum](https://leetcode.com/problems/two-sum/)
**Category:** Google tagged

## Problem Understanding
- Input: Array `nums`, integer `target`
- Output: Indices of the two numbers that add up to `target`
- Constraints: Exactly one solution, can't use same element twice

## Approach

### Brute Force
- Check every pair `(i, j)` -> O(n²)

### Hash Map (Optimal)
- For each `x`, look for `target - x` in map
- One pass: check then add

## Implementation
```python
seen = {}
for i, num in enumerate(nums):
    diff = target - num
    if diff in seen:
        return [seen[diff], i]
    seen[num] = i
```

## Complexity
- **Time**: O(n)
- **Space**: O(n)

## Key Insight
- Trade space for time with Hash Map
- Check *before* adding to handle duplicates correctly
""",

    "3sum": """# 3Sum

**Problem Link:** [3sum](https://leetcode.com/problems/3sum/)
**Category:** Google tagged

## Problem Understanding
- Find all unique triplets `[a, b, c]` where `a + b + c = 0`
- No duplicate triplets allowed

## Approach

### Sorting + Two Pointers
1. Sort array
2. Fix `nums[i]`, find pairs summing to `-nums[i]`
3. Skip duplicates at all levels

## Implementation
```python
nums.sort()
result = []
for i in range(len(nums) - 2):
    if i > 0 and nums[i] == nums[i-1]: continue
    l, r = i + 1, len(nums) - 1
    while l < r:
        s = nums[i] + nums[l] + nums[r]
        if s < 0: l += 1
        elif s > 0: r -= 1
        else:
            result.append([nums[i], nums[l], nums[r]])
            while l < r and nums[l] == nums[l+1]: l += 1
            while l < r and nums[r] == nums[r-1]: r -= 1
            l, r = l + 1, r - 1
return result
```

## Complexity
- **Time**: O(n²)
- **Space**: O(1) (excluding output)

## Key Insight
- Sorting enables Two Pointers and easy duplicate skipping
""",

    "merge-sorted-array": """# Merge Sorted Array

**Problem Link:** [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)
**Category:** Google tagged

## Problem Understanding
- Merge `nums2` into `nums1` in-place
- `nums1` has extra space at end

## Approach

### Fill from End (Reverse Two Pointers)
- Start from the end to avoid overwriting unprocessed elements
- Compare and place larger element at position `p`

## Implementation
```python
p1, p2 = m - 1, n - 1
for p in range(m + n - 1, -1, -1):
    if p2 < 0: break
    if p1 >= 0 and nums1[p1] > nums2[p2]:
        nums1[p] = nums1[p1]
        p1 -= 1
    else:
        nums1[p] = nums2[p2]
        p2 -= 1
```

## Complexity
- **Time**: O(m + n)
- **Space**: O(1)

## Key Insight
- Fill from end when array has space at end
""",

    "valid-parentheses": """# Valid Parentheses

**Problem Link:** [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
**Category:** Google tagged

## Problem Understanding
- Check if brackets are balanced and properly nested

## Approach

### Stack
- Push opening brackets
- Pop and match for closing brackets

## Implementation
```python
stack = []
mapping = {")": "(", "}": "{", "]": "["}
for char in s:
    if char in mapping:
        if not stack or stack.pop() != mapping[char]:
            return False
    else:
        stack.append(char)
return not stack
```

## Complexity
- **Time**: O(n)
- **Space**: O(n)

## Key Insight
- LIFO property of stack matches nested structure
""",

    "best-time-to-buy-and-sell-stock": """# Best Time to Buy and Sell Stock

**Problem Link:** [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
**Category:** Google tagged

## Problem Understanding
- Find max profit from one buy and one sell
- Must buy before sell

## Approach

### One Pass (Track Minimum)
- Track minimum price seen so far
- At each price, calculate potential profit

## Implementation
```python
min_price = float('inf')
max_profit = 0
for price in prices:
    if price < min_price:
        min_price = price
    elif price - min_price > max_profit:
        max_profit = price - min_price
return max_profit
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)

## Key Insight
- Greedy: always buy at the lowest price seen so far
""",

    "longest-common-prefix": """# Longest Common Prefix

**Problem Link:** [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)
**Category:** Google tagged

## Problem Understanding
- Find longest prefix common to all strings

## Approach

### Horizontal Scanning
- Start with first string as prefix
- Shrink until it matches start of each string

## Implementation
```python
if not strs: return ""
prefix = strs[0]
for s in strs[1:]:
    while not s.startswith(prefix):
        prefix = prefix[:-1]
        if not prefix: return ""
return prefix
```

## Complexity
- **Time**: O(S) where S is sum of all chars
- **Space**: O(1)
""",

    "remove-duplicates-from-sorted-array": """# Remove Duplicates from Sorted Array

**Problem Link:** [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
**Category:** Google tagged

## Problem Understanding
- Remove duplicates in-place, return count of unique elements

## Approach

### Two Pointers (Slow/Fast)
- Slow pointer marks last unique position
- Fast pointer scans for new unique elements

## Implementation
```python
if not nums: return 0
j = 0
for i in range(1, len(nums)):
    if nums[i] != nums[j]:
        j += 1
        nums[j] = nums[i]
return j + 1
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
""",

    "majority-element": """# Majority Element

**Problem Link:** [Majority Element](https://leetcode.com/problems/majority-element/)
**Category:** Google tagged

## Problem Understanding
- Find element appearing more than n/2 times

## Approach

### Boyer-Moore Voting Algorithm
- Cancel out different elements
- Majority survives because count > n/2

## Implementation
```python
candidate, count = None, 0
for num in nums:
    if count == 0:
        candidate = num
    count += (1 if num == candidate else -1)
return candidate
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
""",

    "roman-to-integer": """# Roman to Integer

**Problem Link:** [Roman to Integer](https://leetcode.com/problems/roman-to-integer/)
**Category:** Google tagged

## Problem Understanding
- Convert Roman numeral string to integer
- Handle subtraction cases (IV, IX, XL, XC, CD, CM)

## Approach

### Right-to-Left Pass
- If current < previous, subtract; else add

## Implementation
```python
m = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
total, prev = 0, 0
for c in reversed(s):
    curr = m[c]
    total += curr if curr >= prev else -curr
    prev = curr
return total
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
""",

    "binary-search": """# Binary Search

**Problem Link:** [Binary Search](https://leetcode.com/problems/binary-search/)
**Category:** Google tagged

## Problem Understanding
- Find target in sorted array, return index or -1

## Approach

### Binary Search
- Divide search space in half each iteration

## Implementation
```python
l, r = 0, len(nums) - 1
while l <= r:
    mid = (l + r) // 2
    if nums[mid] == target: return mid
    elif nums[mid] < target: l = mid + 1
    else: r = mid - 1
return -1
```

## Complexity
- **Time**: O(log n)
- **Space**: O(1)

## Key Insight
- Use `l + (r-l)//2` in other languages to avoid overflow
""",

    "move-zeroes": """# Move Zeroes

**Problem Link:** [Move Zeroes](https://leetcode.com/problems/move-zeroes/)
**Category:** Google tagged

## Problem Understanding
- Move all 0s to end, maintain relative order of non-zeros

## Approach

### Two Pointers (Swap)
- `pos` tracks where next non-zero should go
- Swap non-zeros to front

## Implementation
```python
pos = 0
for i in range(len(nums)):
    if nums[i] != 0:
        nums[pos], nums[i] = nums[i], nums[pos]
        pos += 1
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
""",

    "add-two-numbers": """# Add Two Numbers

**Problem Link:** [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)
**Category:** Google tagged

## Problem Understanding
- Two linked lists represent numbers in reverse order
- Return sum as linked list

## Approach

### Elementary Math with Carry
- Add digit by digit, track carry

## Implementation
```python
dummy = ListNode(0)
curr, carry = dummy, 0
while l1 or l2 or carry:
    v1 = l1.val if l1 else 0
    v2 = l2.val if l2 else 0
    val = v1 + v2 + carry
    carry, digit = divmod(val, 10)
    curr.next = ListNode(digit)
    curr = curr.next
    l1 = l1.next if l1 else None
    l2 = l2.next if l2 else None
return dummy.next
```

## Complexity
- **Time**: O(max(m, n))
- **Space**: O(max(m, n))

## Key Insight
- Include `carry` in while condition for final carry
""",

    "climbing-stairs": """# Climbing Stairs

**Problem Link:** [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
**Category:** Google tagged

## Problem Understanding
- Count ways to reach top taking 1 or 2 steps

## Approach

### Fibonacci DP
- `ways(n) = ways(n-1) + ways(n-2)`
- Only need last two values

## Implementation
```python
if n <= 2: return n
prev1, prev2 = 1, 2
for _ in range(3, n + 1):
    prev1, prev2 = prev2, prev1 + prev2
return prev2
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)

## Key Insight
- Classic DP, same as Fibonacci
""",

    "valid-palindrome": """# Valid Palindrome

**Problem Link:** [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
**Category:** Google tagged

## Problem Understanding
- Check if string is palindrome (alphanumeric only, case-insensitive)

## Approach

### Two Pointers
- Compare from both ends, skip non-alphanumeric

## Implementation
```python
l, r = 0, len(s) - 1
while l < r:
    while l < r and not s[l].isalnum(): l += 1
    while l < r and not s[r].isalnum(): r -= 1
    if s[l].lower() != s[r].lower(): return False
    l, r = l + 1, r - 1
return True
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
""",

    "valid-anagram": """# Valid Anagram

**Problem Link:** [Valid Anagram](https://leetcode.com/problems/valid-anagram/)
**Category:** Google tagged

## Problem Understanding
- Check if `t` is anagram of `s` (same chars, same counts)

## Approach

### Frequency Count
- Count chars in both strings, compare

## Implementation
```python
if len(s) != len(t): return False
count = {}
for c in s: count[c] = count.get(c, 0) + 1
for c in t:
    if c not in count or count[c] == 0: return False
    count[c] -= 1
return True
```

## Complexity
- **Time**: O(n)
- **Space**: O(1) (26 letters)
""",

    "plus-one": """# Plus One

**Problem Link:** [Plus One](https://leetcode.com/problems/plus-one/)
**Category:** Google tagged

## Problem Understanding
- Array represents integer, add 1 to it

## Approach

### Reverse Loop with Carry
- Start from end, handle 9s specially

## Implementation
```python
for i in range(len(digits)-1, -1, -1):
    if digits[i] < 9:
        digits[i] += 1
        return digits
    digits[i] = 0
return [1] + digits  # All 9s case
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
""",

    "sqrtx": """# Sqrt(x)

**Problem Link:** [Sqrt(x)](https://leetcode.com/problems/sqrtx/)
**Category:** Google tagged

## Problem Understanding
- Return floor of square root without using `pow`

## Approach

### Binary Search
- Search for `k` where `k*k <= x < (k+1)*(k+1)`

## Implementation
```python
if x < 2: return x
l, r = 2, x // 2
while l <= r:
    mid = (l + r) // 2
    sq = mid * mid
    if sq == x: return mid
    elif sq < x: l = mid + 1
    else: r = mid - 1
return r
```

## Complexity
- **Time**: O(log x)
- **Space**: O(1)
""",

    "happy-number": """# Happy Number

**Problem Link:** [Happy Number](https://leetcode.com/problems/happy-number/)
**Category:** Google tagged

## Problem Understanding
- Repeatedly sum squares of digits
- Return true if reaches 1, false if cycles

## Approach

### Hash Set (Cycle Detection)
- Track seen numbers, detect cycle

## Implementation
```python
def get_next(n):
    total = 0
    while n:
        n, digit = divmod(n, 10)
        total += digit ** 2
    return total

seen = set()
while n != 1 and n not in seen:
    seen.add(n)
    n = get_next(n)
return n == 1
```

## Complexity
- **Time**: O(log n)
- **Space**: O(log n)
""",

    "reverse-linked-list": """# Reverse Linked List

**Problem Link:** [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
**Category:** Google tagged

## Problem Understanding
- Reverse singly linked list

## Approach

### Iterative (Pointer Swap)
- Track prev, curr, next; reverse links

## Implementation
```python
prev = None
curr = head
while curr:
    next_temp = curr.next
    curr.next = prev
    prev = curr
    curr = next_temp
return prev
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
""",

    "contains-duplicate": """# Contains Duplicate

**Problem Link:** [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
**Category:** Google tagged

## Problem Understanding
- Return true if any value appears twice

## Approach

### Hash Set
- Add to set, check if already exists

## Implementation
```python
seen = set()
for n in nums:
    if n in seen: return True
    seen.add(n)
return False
```

## Complexity
- **Time**: O(n)
- **Space**: O(n)
""",

    "length-of-last-word": """# Length of Last Word

**Problem Link:** [Length of Last Word](https://leetcode.com/problems/length-of-last-word/)
**Category:** Google tagged

## Problem Understanding
- Return length of last word (ignore trailing spaces)

## Approach

### Reverse Scan
- Skip trailing spaces, count chars until space

## Implementation
```python
i = len(s) - 1
while i >= 0 and s[i] == ' ': i -= 1
length = 0
while i >= 0 and s[i] != ' ':
    length += 1
    i -= 1
return length
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
""",

    "palindrome-number": """# Palindrome Number

**Problem Link:** [Palindrome Number](https://leetcode.com/problems/palindrome-number/)
**Category:** Google tagged

## Problem Understanding
- Check if integer is palindrome without string conversion

## Approach

### Revert Half Number
- Revert last half, compare with first half

## Implementation
```python
if x < 0 or (x % 10 == 0 and x != 0): return False
rev = 0
while x > rev:
    rev = rev * 10 + x % 10
    x //= 10
return x == rev or x == rev // 10
```

## Complexity
- **Time**: O(log x)
- **Space**: O(1)
""",

    "remove-element": """# Remove Element

**Problem Link:** [Remove Element](https://leetcode.com/problems/remove-element/)
**Category:** Google tagged

## Problem Understanding
- Remove all occurrences of `val` in-place

## Approach

### Two Pointers
- Writer pointer only advances for valid elements

## Implementation
```python
i = 0
for x in nums:
    if x != val:
        nums[i] = x
        i += 1
return i
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
""",

    "find-the-index-of-the-first-occurrence-in-a-string": """# Find the Index of the First Occurrence in a String

**Problem Link:** [Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)
**Category:** Google tagged

## Problem Understanding
- Find first index of `needle` in `haystack`

## Approach

### Sliding Window
- Check each substring of length `len(needle)`

## Implementation
```python
for i in range(len(haystack) - len(needle) + 1):
    if haystack[i:i+len(needle)] == needle:
        return i
return -1
```

## Complexity
- **Time**: O(n * m)
- **Space**: O(1)
""",

    "binary-tree-inorder-traversal": """# Binary Tree Inorder Traversal

**Problem Link:** [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
**Category:** Google tagged

## Problem Understanding
- Return inorder traversal: Left -> Node -> Right

## Approach

### Iterative (Stack)
- Push all lefts, pop one, go right

## Implementation
```python
res, stack = [], []
curr = root
while curr or stack:
    while curr:
        stack.append(curr)
        curr = curr.left
    curr = stack.pop()
    res.append(curr.val)
    curr = curr.right
return res
```

## Complexity
- **Time**: O(n)
- **Space**: O(h)
""",

    "running-sum-of-1d-array": """# Running Sum of 1d Array

**Problem Link:** [Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/)
**Category:** Google tagged

## Problem Understanding
- `result[i] = sum(nums[0]...nums[i])`

## Approach

### Prefix Sum (In-Place)
- Each element becomes sum of itself and previous

## Implementation
```python
for i in range(1, len(nums)):
    nums[i] += nums[i-1]
return nums
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
""",

    "isomorphic-strings": """# Isomorphic Strings

**Problem Link:** [Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/)
**Category:** Google tagged

## Problem Understanding
- Check if chars in `s` can map to `t` (bijective mapping)

## Approach

### Two Hash Maps
- Track `s->t` and `t->s` mappings

## Implementation
```python
m1, m2 = {}, {}
for c1, c2 in zip(s, t):
    if (c1 in m1 and m1[c1] != c2) or (c2 in m2 and m2[c2] != c1):
        return False
    m1[c1], m2[c2] = c2, c1
return True
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
""",

    "container-with-most-water": """# Container With Most Water

**Problem Link:** [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
**Category:** Google tagged

## Problem Understanding
- Find max area: `min(h[i], h[j]) * (j - i)`

## Approach

### Two Pointers
- Start at max width, move shorter line inward

## Implementation
```python
l, r = 0, len(height) - 1
max_area = 0
while l < r:
    max_area = max(max_area, min(height[l], height[r]) * (r - l))
    if height[l] < height[r]: l += 1
    else: r -= 1
return max_area
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)

## Key Insight
- Moving shorter line might find taller; moving taller can only hurt
""",

    "middle-of-the-linked-list": """# Middle of the Linked List

**Problem Link:** [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)
**Category:** Google tagged

## Problem Understanding
- Return middle node (second middle if two)

## Approach

### Fast/Slow Pointers
- Fast moves 2x, when fast ends, slow is at middle

## Implementation
```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
return slow
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
""",

    "two-sum-ii-input-array-is-sorted": """# Two Sum II - Input Array Is Sorted

**Problem Link:** [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
**Category:** Google tagged

## Problem Understanding
- Sorted array, find two indices (1-based) summing to target

## Approach

### Two Pointers
- Start at ends, move based on sum comparison

## Implementation
```python
l, r = 0, len(numbers) - 1
while l < r:
    s = numbers[l] + numbers[r]
    if s == target: return [l+1, r+1]
    if s < target: l += 1
    else: r -= 1
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
""",

    "clone-graph": """# Clone Graph

**Problem Link:** [Clone Graph](https://leetcode.com/problems/clone-graph/)
**Category:** Google tagged

## Problem Understanding
- Deep copy a graph with adjacency list

## Approach

### DFS with Hash Map
- Map old node -> cloned node
- Recursively clone neighbors

## Implementation
```python
def cloneGraph(node):
    if not node: return None
    cloned = {}
    def dfs(n):
        if n in cloned: return cloned[n]
        copy = Node(n.val)
        cloned[n] = copy
        for neighbor in n.neighbors:
            copy.neighbors.append(dfs(neighbor))
        return copy
    return dfs(node)
```

## Complexity
- **Time**: O(V + E)
- **Space**: O(V)
""",

    "course-schedule": """# Course Schedule

**Problem Link:** [Course Schedule](https://leetcode.com/problems/course-schedule/)
**Category:** Google tagged

## Problem Understanding
- Can finish all courses? (Detect cycle in DAG)

## Approach

### Topological Sort (Kahn's BFS)
- Remove nodes with 0 in-degree iteratively
- If all removed, no cycle

## Implementation
```python
from collections import deque, defaultdict
graph = defaultdict(list)
indegree = [0] * numCourses
for a, b in prerequisites:
    graph[b].append(a)
    indegree[a] += 1
queue = deque([i for i in range(numCourses) if indegree[i] == 0])
count = 0
while queue:
    node = queue.popleft()
    count += 1
    for neighbor in graph[node]:
        indegree[neighbor] -= 1
        if indegree[neighbor] == 0:
            queue.append(neighbor)
return count == numCourses
```

## Complexity
- **Time**: O(V + E)
- **Space**: O(V + E)
""",

    "evaluate-division": """# Evaluate Division

**Problem Link:** [Evaluate Division](https://leetcode.com/problems/evaluate-division/)
**Category:** Google tagged

## Problem Understanding
- Given equations `a/b = k`, evaluate queries

## Approach

### Graph (DFS/BFS)
- Build graph: `a -> b` with weight `k`, `b -> a` with weight `1/k`
- For query `x/y`, find path `x -> y` and multiply weights

## Implementation
```python
from collections import defaultdict
graph = defaultdict(dict)
for (a, b), v in zip(equations, values):
    graph[a][b] = v
    graph[b][a] = 1 / v

def dfs(src, dst, visited):
    if src not in graph or dst not in graph: return -1.0
    if src == dst: return 1.0
    visited.add(src)
    for neighbor, weight in graph[src].items():
        if neighbor not in visited:
            result = dfs(neighbor, dst, visited)
            if result != -1.0:
                return weight * result
    return -1.0

return [dfs(c, d, set()) for c, d in queries]
```

## Complexity
- **Time**: O(Q * (V + E))
- **Space**: O(V + E)
""",

    # ============ LINKED LISTS ============
    "palindrome-linked-list": """# Palindrome Linked List

**Problem Link:** [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)
**Category:** Linked Lists

## Problem Understanding
- Check if linked list is palindrome

## Approach

### Reverse Second Half
1. Find middle (fast/slow)
2. Reverse second half
3. Compare halves

## Implementation
```python
# Find middle
slow = fast = head
while fast and fast.next:
    slow, fast = slow.next, fast.next.next

# Reverse second half
prev = None
while slow:
    slow.next, prev, slow = prev, slow, slow.next

# Compare
left, right = head, prev
while right:
    if left.val != right.val: return False
    left, right = left.next, right.next
return True
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
""",

    "lru-cache": """# LRU Cache

**Problem Link:** [LRU Cache](https://leetcode.com/problems/lru-cache/)
**Category:** Linked Lists

## Problem Understanding
- Implement LRU Cache with O(1) get/put

## Approach

### Hash Map + Doubly Linked List
- Map: key -> node
- DLL: Most recent at head, least at tail

## Implementation
```python
class Node:
    def __init__(self, k, v):
        self.key, self.val = k, v
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    def _remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def _insert(self, node):
        node.next, node.prev = self.head.next, self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key in self.cache:
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self._insert(node)
        if len(self.cache) > self.cap:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
```

## Complexity
- **Time**: O(1) for both operations
- **Space**: O(capacity)
""",

    "remove-nth-node-from-end-of-list": """# Remove Nth Node From End of List

**Problem Link:** [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
**Category:** Linked Lists

## Problem Understanding
- Remove nth node from end in one pass

## Approach

### Two Pointers (Gap of N)
- Move fast n steps ahead
- Move both until fast reaches end
- Slow is at prev of target

## Implementation
```python
dummy = ListNode(0, head)
slow = fast = dummy
for _ in range(n): fast = fast.next
while fast.next:
    slow, fast = slow.next, fast.next
slow.next = slow.next.next
return dummy.next
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
""",

    "copy-list-with-random-pointer": """# Copy List with Random Pointer

**Problem Link:** [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/)
**Category:** Linked Lists

## Problem Understanding
- Deep copy list where each node has `next` and `random` pointers

## Approach

### Hash Map
- Map old node -> new node
- Two passes: create nodes, then set pointers

## Implementation
```python
if not head: return None
old_to_new = {}
curr = head
while curr:
    old_to_new[curr] = Node(curr.val)
    curr = curr.next
curr = head
while curr:
    old_to_new[curr].next = old_to_new.get(curr.next)
    old_to_new[curr].random = old_to_new.get(curr.random)
    curr = curr.next
return old_to_new[head]
```

## Complexity
- **Time**: O(n)
- **Space**: O(n)
""",

    # ============ HEAPS ============
    "kth-largest-element-in-an-array": """# Kth Largest Element in an Array

**Problem Link:** [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
**Category:** Heaps

## Problem Understanding
- Find kth largest element

## Approach

### Min Heap of Size K
- Keep k largest elements
- Top of min heap = kth largest

## Implementation
```python
import heapq
heap = []
for n in nums:
    heapq.heappush(heap, n)
    if len(heap) > k:
        heapq.heappop(heap)
return heap[0]
```

## Complexity
- **Time**: O(n log k)
- **Space**: O(k)
""",

    "top-k-frequent-elements": """# Top K Frequent Elements

**Problem Link:** [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
**Category:** Heaps

## Problem Understanding
- Return k most frequent elements

## Approach

### Bucket Sort
- Count frequencies
- Bucket by frequency
- Collect from highest buckets

## Implementation
```python
from collections import Counter
count = Counter(nums)
buckets = [[] for _ in range(len(nums) + 1)]
for num, freq in count.items():
    buckets[freq].append(num)
result = []
for i in range(len(buckets) - 1, -1, -1):
    for num in buckets[i]:
        result.append(num)
        if len(result) == k:
            return result
```

## Complexity
- **Time**: O(n)
- **Space**: O(n)
""",

    "find-median-from-data-stream": """# Find Median from Data Stream

**Problem Link:** [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)
**Category:** Heaps

## Problem Understanding
- Add numbers, query median efficiently

## Approach

### Two Heaps
- Max heap for lower half
- Min heap for upper half
- Balance sizes (differ by at most 1)

## Implementation
```python
import heapq
class MedianFinder:
    def __init__(self):
        self.lo = []  # max heap (negated)
        self.hi = []  # min heap

    def addNum(self, num):
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self):
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        return (-self.lo[0] + self.hi[0]) / 2
```

## Complexity
- **addNum**: O(log n)
- **findMedian**: O(1)
- **Space**: O(n)
""",

    "meeting-rooms-ii": """# Meeting Rooms II

**Problem Link:** [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)
**Category:** Heaps

## Problem Understanding
- Find minimum meeting rooms needed

## Approach

### Min Heap (End Times)
- Sort by start time
- Heap tracks earliest ending meeting
- If new start >= heap top, reuse room (pop); else need new room

## Implementation
```python
import heapq
if not intervals: return 0
intervals.sort(key=lambda x: x[0])
heap = [intervals[0][1]]
for i in range(1, len(intervals)):
    if intervals[i][0] >= heap[0]:
        heapq.heappop(heap)
    heapq.heappush(heap, intervals[i][1])
return len(heap)
```

## Complexity
- **Time**: O(n log n)
- **Space**: O(n)
""",

    # ============ STACKS & QUEUES ============
    "min-stack": """# Min Stack

**Problem Link:** [Min Stack](https://leetcode.com/problems/min-stack/)
**Category:** Stacks & Queues

## Problem Understanding
- Stack with O(1) push, pop, top, and getMin

## Approach

### Two Stacks
- One for values, one for minimums

## Implementation
```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]
```

## Complexity
- **Time**: O(1) all operations
- **Space**: O(n)
""",

    "daily-temperatures": """# Daily Temperatures

**Problem Link:** [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)
**Category:** Stacks & Queues

## Problem Understanding
- For each day, find days until warmer temperature

## Approach

### Monotonic Stack (Decreasing)
- Stack stores indices of unresolved temperatures
- When warmer found, calculate distance for all colder ones

## Implementation
```python
result = [0] * len(temperatures)
stack = []
for i, t in enumerate(temperatures):
    while stack and temperatures[stack[-1]] < t:
        j = stack.pop()
        result[j] = i - j
    stack.append(i)
return result
```

## Complexity
- **Time**: O(n)
- **Space**: O(n)
""",

    "trapping-rain-water": """# Trapping Rain Water

**Problem Link:** [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)
**Category:** Stacks & Queues

## Problem Understanding
- Calculate water trapped between bars

## Approach

### Two Pointers
- Track left_max and right_max
- Water at i = min(left_max, right_max) - height[i]

## Implementation
```python
l, r = 0, len(height) - 1
left_max = right_max = 0
water = 0
while l < r:
    if height[l] < height[r]:
        if height[l] >= left_max:
            left_max = height[l]
        else:
            water += left_max - height[l]
        l += 1
    else:
        if height[r] >= right_max:
            right_max = height[r]
        else:
            water += right_max - height[r]
        r -= 1
return water
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
""",

    "evaluate-reverse-polish-notation": """# Evaluate Reverse Polish Notation

**Problem Link:** [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)
**Category:** Stacks & Queues

## Problem Understanding
- Evaluate postfix expression

## Approach

### Stack
- Push operands, pop two for operators

## Implementation
```python
stack = []
for token in tokens:
    if token in "+-*/":
        b, a = stack.pop(), stack.pop()
        if token == '+': stack.append(a + b)
        elif token == '-': stack.append(a - b)
        elif token == '*': stack.append(a * b)
        else: stack.append(int(a / b))  # truncate toward zero
    else:
        stack.append(int(token))
return stack[0]
```

## Complexity
- **Time**: O(n)
- **Space**: O(n)
""",

    # ============ RECURSION & DP ============
    "coin-change": """# Coin Change

**Problem Link:** [Coin Change](https://leetcode.com/problems/coin-change/)
**Category:** Recursion & DP

## Problem Understanding
- Find minimum coins to make amount

## Approach

### Bottom-Up DP
- `dp[i]` = min coins for amount `i`
- `dp[i] = min(dp[i], dp[i - coin] + 1)`

## Implementation
```python
dp = [float('inf')] * (amount + 1)
dp[0] = 0
for coin in coins:
    for x in range(coin, amount + 1):
        dp[x] = min(dp[x], dp[x - coin] + 1)
return dp[amount] if dp[amount] != float('inf') else -1
```

## Complexity
- **Time**: O(amount * len(coins))
- **Space**: O(amount)
""",

    "longest-increasing-subsequence": """# Longest Increasing Subsequence

**Problem Link:** [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
**Category:** Recursion & DP

## Problem Understanding
- Find length of longest strictly increasing subsequence

## Approach

### Binary Search + DP
- Maintain array of smallest tail for each length

## Implementation
```python
from bisect import bisect_left
tails = []
for num in nums:
    pos = bisect_left(tails, num)
    if pos == len(tails):
        tails.append(num)
    else:
        tails[pos] = num
return len(tails)
```

## Complexity
- **Time**: O(n log n)
- **Space**: O(n)
""",

    "word-break": """# Word Break

**Problem Link:** [Word Break](https://leetcode.com/problems/word-break/)
**Category:** Recursion & DP

## Problem Understanding
- Can string be segmented into dictionary words?

## Approach

### DP
- `dp[i]` = can s[0:i] be segmented?
- `dp[i] = dp[j] and s[j:i] in wordDict`

## Implementation
```python
word_set = set(wordDict)
dp = [False] * (len(s) + 1)
dp[0] = True
for i in range(1, len(s) + 1):
    for j in range(i):
        if dp[j] and s[j:i] in word_set:
            dp[i] = True
            break
return dp[len(s)]
```

## Complexity
- **Time**: O(n² * m) where m is max word length
- **Space**: O(n)
""",

    "generate-parentheses": """# Generate Parentheses

**Problem Link:** [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
**Category:** Recursion & DP

## Problem Understanding
- Generate all valid combinations of n pairs of parentheses

## Approach

### Backtracking
- Track open and close counts
- Add '(' if open < n, ')' if close < open

## Implementation
```python
result = []
def backtrack(curr, open_count, close_count):
    if len(curr) == 2 * n:
        result.append(curr)
        return
    if open_count < n:
        backtrack(curr + '(', open_count + 1, close_count)
    if close_count < open_count:
        backtrack(curr + ')', open_count, close_count + 1)
backtrack('', 0, 0)
return result
```

## Complexity
- **Time**: O(4^n / sqrt(n)) - Catalan number
- **Space**: O(n)
""",

    "permutations": """# Permutations

**Problem Link:** [Permutations](https://leetcode.com/problems/permutations/)
**Category:** Recursion & DP

## Problem Understanding
- Return all permutations of unique integers

## Approach

### Backtracking
- Track used elements with set or swap technique

## Implementation
```python
result = []
def backtrack(path, remaining):
    if not remaining:
        result.append(path[:])
        return
    for i in range(len(remaining)):
        path.append(remaining[i])
        backtrack(path, remaining[:i] + remaining[i+1:])
        path.pop()
backtrack([], nums)
return result
```

## Complexity
- **Time**: O(n * n!)
- **Space**: O(n)
""",

    # ============ HASHMAPS ============
    "group-anagrams": """# Group Anagrams

**Problem Link:** [Group Anagrams](https://leetcode.com/problems/group-anagrams/)
**Category:** Hashmaps

## Problem Understanding
- Group strings that are anagrams

## Approach

### Sorted String as Key
- Anagrams have same sorted form

## Implementation
```python
from collections import defaultdict
groups = defaultdict(list)
for s in strs:
    key = ''.join(sorted(s))
    groups[key].append(s)
return list(groups.values())
```

## Complexity
- **Time**: O(n * k log k) where k is max string length
- **Space**: O(n * k)
""",

    "subarray-sum-equals-k": """# Subarray Sum Equals K

**Problem Link:** [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)
**Category:** Hashmaps

## Problem Understanding
- Count subarrays with sum = k

## Approach

### Prefix Sum + Hash Map
- If `prefix[j] - prefix[i] = k`, subarray i+1 to j sums to k

## Implementation
```python
count = 0
prefix_sum = 0
prefix_counts = {0: 1}
for num in nums:
    prefix_sum += num
    count += prefix_counts.get(prefix_sum - k, 0)
    prefix_counts[prefix_sum] = prefix_counts.get(prefix_sum, 0) + 1
return count
```

## Complexity
- **Time**: O(n)
- **Space**: O(n)
""",

    # ============ ARRAYS & STRINGS ============
    "meeting-rooms": """# Meeting Rooms

**Problem Link:** [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/)
**Category:** Arrays & Strings

## Problem Understanding
- Can a person attend all meetings? (No overlap)

## Approach

### Sort and Compare Adjacent
- Sort by start time
- Check if any end > next start

## Implementation
```python
intervals.sort(key=lambda x: x[0])
for i in range(len(intervals) - 1):
    if intervals[i][1] > intervals[i+1][0]:
        return False
return True
```

## Complexity
- **Time**: O(n log n)
- **Space**: O(1)
""",
}


def get_problem_slug(url):
    """Extract the problem slug from LeetCode URL."""
    match = re.search(r'/problems/([\w-]+)/?', url)
    return match.group(1) if match else None


def create_category_dir(sheet_name):
    """Create a sanitized directory name from sheet name."""
    sanitized = re.sub(r'[^\w\s-]', '', sheet_name.lower())
    sanitized = re.sub(r'[\s-]+', '_', sanitized)
    return sanitized


def main():
    """Generate all problem-specific mindmaps."""
    # Load the extracted problems
    with open('leetcode_problems.json', 'r') as f:
        problems = json.load(f)

    print(f"Generating specific mindmaps for {len(PROBLEM_CONTENT)} problems...")

    base_dir = Path('leetcode_mindmaps')
    base_dir.mkdir(exist_ok=True)

    updated = 0
    for problem in problems:
        slug = get_problem_slug(problem['url'])
        if not slug:
            continue

        if slug in PROBLEM_CONTENT:
            sheet_name = problem['context']['sheet']
            category_dir = create_category_dir(sheet_name)
            full_dir = base_dir / category_dir
            full_dir.mkdir(exist_ok=True)

            filepath = full_dir / f"{slug}.md"
            with open(filepath, 'w') as f:
                f.write(PROBLEM_CONTENT[slug])
            updated += 1
            print(f"  Updated: {filepath}")

    print(f"\n✓ Updated {updated} mindmaps with specific content!")


if __name__ == '__main__':
    main()
