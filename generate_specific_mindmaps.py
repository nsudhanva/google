#!/usr/bin/env python3
"""
Generate problem-specific mindmaps for all LeetCode problems.
This creates high-quality, specific content with Java implementations.
"""

import json
import os
import re
from pathlib import Path

# Problem-specific content database with JAVA implementations
PROBLEM_CONTENT = {
    # ============ GOOGLE TAGGED ============
    "two-sum": """# Two Sum

**Problem Link:** [Two Sum](https://leetcode.com/problems/two-sum/)
**Category:** Google tagged

## Problem Understanding
- Input: Array `nums`, integer `target`
- Output: Indices of two numbers that add up to `target`
- Constraints: Exactly one solution, can't use same element twice

## Approach

### Brute Force
- Check every pair `(i, j)` -> O(n²)

### Hash Map (Optimal)
- For each `x`, look for `target - x` in map
- One pass: check then add

## Implementation
```java
public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
        int complement = target - nums[i];
        if (map.containsKey(complement)) {
            return new int[] { map.get(complement), i };
        }
        map.put(nums[i], i);
    }
    return new int[] {};
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(n)

## Key Insight
- Trade space for time with HashMap
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
```java
public List<List<Integer>> threeSum(int[] nums) {
    Arrays.sort(nums);
    List<List<Integer>> result = new ArrayList<>();
    
    for (int i = 0; i < nums.length - 2; i++) {
        if (i > 0 && nums[i] == nums[i - 1]) continue;
        
        int left = i + 1, right = nums.length - 1;
        while (left < right) {
            int sum = nums[i] + nums[left] + nums[right];
            if (sum < 0) {
                left++;
            } else if (sum > 0) {
                right--;
            } else {
                result.add(Arrays.asList(nums[i], nums[left], nums[right]));
                while (left < right && nums[left] == nums[left + 1]) left++;
                while (left < right && nums[right] == nums[right - 1]) right--;
                left++;
                right--;
            }
        }
    }
    return result;
}
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
```java
public void merge(int[] nums1, int m, int[] nums2, int n) {
    int p1 = m - 1, p2 = n - 1, p = m + n - 1;
    
    while (p2 >= 0) {
        if (p1 >= 0 && nums1[p1] > nums2[p2]) {
            nums1[p--] = nums1[p1--];
        } else {
            nums1[p--] = nums2[p2--];
        }
    }
}
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
```java
public boolean isValid(String s) {
    Stack<Character> stack = new Stack<>();
    Map<Character, Character> map = Map.of(')', '(', '}', '{', ']', '[');
    
    for (char c : s.toCharArray()) {
        if (map.containsKey(c)) {
            if (stack.isEmpty() || stack.pop() != map.get(c)) {
                return false;
            }
        } else {
            stack.push(c);
        }
    }
    return stack.isEmpty();
}
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
```java
public int maxProfit(int[] prices) {
    int minPrice = Integer.MAX_VALUE;
    int maxProfit = 0;
    
    for (int price : prices) {
        if (price < minPrice) {
            minPrice = price;
        } else if (price - minPrice > maxProfit) {
            maxProfit = price - minPrice;
        }
    }
    return maxProfit;
}
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
```java
public String longestCommonPrefix(String[] strs) {
    if (strs == null || strs.length == 0) return "";
    
    String prefix = strs[0];
    for (int i = 1; i < strs.length; i++) {
        while (strs[i].indexOf(prefix) != 0) {
            prefix = prefix.substring(0, prefix.length() - 1);
            if (prefix.isEmpty()) return "";
        }
    }
    return prefix;
}
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
```java
public int removeDuplicates(int[] nums) {
    if (nums.length == 0) return 0;
    
    int j = 0;
    for (int i = 1; i < nums.length; i++) {
        if (nums[i] != nums[j]) {
            j++;
            nums[j] = nums[i];
        }
    }
    return j + 1;
}
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
```java
public int majorityElement(int[] nums) {
    int candidate = 0, count = 0;
    
    for (int num : nums) {
        if (count == 0) {
            candidate = num;
        }
        count += (num == candidate) ? 1 : -1;
    }
    return candidate;
}
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
```java
public int romanToInt(String s) {
    Map<Character, Integer> map = Map.of(
        'I', 1, 'V', 5, 'X', 10, 'L', 50,
        'C', 100, 'D', 500, 'M', 1000
    );
    
    int total = 0, prev = 0;
    for (int i = s.length() - 1; i >= 0; i--) {
        int curr = map.get(s.charAt(i));
        total += (curr < prev) ? -curr : curr;
        prev = curr;
    }
    return total;
}
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
```java
public int search(int[] nums, int target) {
    int left = 0, right = nums.length - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) return mid;
        if (nums[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}
```

## Complexity
- **Time**: O(log n)
- **Space**: O(1)

## Key Insight
- Use `left + (right - left) / 2` to avoid integer overflow
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
```java
public void moveZeroes(int[] nums) {
    int pos = 0;
    for (int i = 0; i < nums.length; i++) {
        if (nums[i] != 0) {
            int temp = nums[pos];
            nums[pos] = nums[i];
            nums[i] = temp;
            pos++;
        }
    }
}
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
```java
public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    ListNode dummy = new ListNode(0);
    ListNode curr = dummy;
    int carry = 0;
    
    while (l1 != null || l2 != null || carry != 0) {
        int v1 = (l1 != null) ? l1.val : 0;
        int v2 = (l2 != null) ? l2.val : 0;
        int sum = v1 + v2 + carry;
        
        carry = sum / 10;
        curr.next = new ListNode(sum % 10);
        curr = curr.next;
        
        if (l1 != null) l1 = l1.next;
        if (l2 != null) l2 = l2.next;
    }
    return dummy.next;
}
```

## Complexity
- **Time**: O(max(m, n))
- **Space**: O(max(m, n))

## Key Insight
- Include `carry != 0` in while condition for final carry
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
```java
public int climbStairs(int n) {
    if (n <= 2) return n;
    
    int prev1 = 1, prev2 = 2;
    for (int i = 3; i <= n; i++) {
        int curr = prev1 + prev2;
        prev1 = prev2;
        prev2 = curr;
    }
    return prev2;
}
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
```java
public boolean isPalindrome(String s) {
    int left = 0, right = s.length() - 1;
    
    while (left < right) {
        while (left < right && !Character.isLetterOrDigit(s.charAt(left))) left++;
        while (left < right && !Character.isLetterOrDigit(s.charAt(right))) right--;
        
        if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}
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
```java
public boolean isAnagram(String s, String t) {
    if (s.length() != t.length()) return false;
    
    int[] count = new int[26];
    for (int i = 0; i < s.length(); i++) {
        count[s.charAt(i) - 'a']++;
        count[t.charAt(i) - 'a']--;
    }
    
    for (int c : count) {
        if (c != 0) return false;
    }
    return true;
}
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
```java
public int[] plusOne(int[] digits) {
    for (int i = digits.length - 1; i >= 0; i--) {
        if (digits[i] < 9) {
            digits[i]++;
            return digits;
        }
        digits[i] = 0;
    }
    
    // All 9s case
    int[] result = new int[digits.length + 1];
    result[0] = 1;
    return result;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
""",
    "sqrtx": """# Sqrt(x)

**Problem Link:** [Sqrt(x)](https://leetcode.com/problems/sqrtx/)
**Category:** Google tagged

## Problem Understanding
- Return floor of square root without using `Math.sqrt`

## Approach

### Binary Search
- Search for `k` where `k*k <= x < (k+1)*(k+1)`

## Implementation
```java
public int mySqrt(int x) {
    if (x < 2) return x;
    
    long left = 2, right = x / 2;
    while (left <= right) {
        long mid = left + (right - left) / 2;
        long sq = mid * mid;
        
        if (sq == x) return (int) mid;
        if (sq < x) left = mid + 1;
        else right = mid - 1;
    }
    return (int) right;
}
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

### HashSet (Cycle Detection)
- Track seen numbers, detect cycle

## Implementation
```java
public boolean isHappy(int n) {
    Set<Integer> seen = new HashSet<>();
    
    while (n != 1 && !seen.contains(n)) {
        seen.add(n);
        n = getNext(n);
    }
    return n == 1;
}

private int getNext(int n) {
    int sum = 0;
    while (n > 0) {
        int digit = n % 10;
        sum += digit * digit;
        n /= 10;
    }
    return sum;
}
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
```java
public ListNode reverseList(ListNode head) {
    ListNode prev = null;
    ListNode curr = head;
    
    while (curr != null) {
        ListNode nextTemp = curr.next;
        curr.next = prev;
        prev = curr;
        curr = nextTemp;
    }
    return prev;
}
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

### HashSet
- Add to set, check if already exists

## Implementation
```java
public boolean containsDuplicate(int[] nums) {
    Set<Integer> seen = new HashSet<>();
    for (int num : nums) {
        if (seen.contains(num)) return true;
        seen.add(num);
    }
    return false;
}
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
```java
public int lengthOfLastWord(String s) {
    int i = s.length() - 1;
    
    while (i >= 0 && s.charAt(i) == ' ') i--;
    
    int length = 0;
    while (i >= 0 && s.charAt(i) != ' ') {
        length++;
        i--;
    }
    return length;
}
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
```java
public boolean isPalindrome(int x) {
    if (x < 0 || (x % 10 == 0 && x != 0)) return false;
    
    int reversed = 0;
    while (x > reversed) {
        reversed = reversed * 10 + x % 10;
        x /= 10;
    }
    return x == reversed || x == reversed / 10;
}
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
```java
public int removeElement(int[] nums, int val) {
    int i = 0;
    for (int j = 0; j < nums.length; j++) {
        if (nums[j] != val) {
            nums[i] = nums[j];
            i++;
        }
    }
    return i;
}
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
- Check each substring of length `needle.length()`

## Implementation
```java
public int strStr(String haystack, String needle) {
    if (needle.isEmpty()) return 0;
    
    for (int i = 0; i <= haystack.length() - needle.length(); i++) {
        if (haystack.substring(i, i + needle.length()).equals(needle)) {
            return i;
        }
    }
    return -1;
}
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
```java
public List<Integer> inorderTraversal(TreeNode root) {
    List<Integer> result = new ArrayList<>();
    Stack<TreeNode> stack = new Stack<>();
    TreeNode curr = root;
    
    while (curr != null || !stack.isEmpty()) {
        while (curr != null) {
            stack.push(curr);
            curr = curr.left;
        }
        curr = stack.pop();
        result.add(curr.val);
        curr = curr.right;
    }
    return result;
}
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
```java
public int[] runningSum(int[] nums) {
    for (int i = 1; i < nums.length; i++) {
        nums[i] += nums[i - 1];
    }
    return nums;
}
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

### Two HashMaps
- Track `s->t` and `t->s` mappings

## Implementation
```java
public boolean isIsomorphic(String s, String t) {
    Map<Character, Character> mapST = new HashMap<>();
    Map<Character, Character> mapTS = new HashMap<>();
    
    for (int i = 0; i < s.length(); i++) {
        char c1 = s.charAt(i), c2 = t.charAt(i);
        
        if (mapST.containsKey(c1) && mapST.get(c1) != c2) return false;
        if (mapTS.containsKey(c2) && mapTS.get(c2) != c1) return false;
        
        mapST.put(c1, c2);
        mapTS.put(c2, c1);
    }
    return true;
}
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
```java
public int maxArea(int[] height) {
    int left = 0, right = height.length - 1;
    int maxArea = 0;
    
    while (left < right) {
        int area = Math.min(height[left], height[right]) * (right - left);
        maxArea = Math.max(maxArea, area);
        
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }
    return maxArea;
}
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
```java
public ListNode middleNode(ListNode head) {
    ListNode slow = head, fast = head;
    
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
    }
    return slow;
}
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
```java
public int[] twoSum(int[] numbers, int target) {
    int left = 0, right = numbers.length - 1;
    
    while (left < right) {
        int sum = numbers[left] + numbers[right];
        if (sum == target) {
            return new int[] { left + 1, right + 1 };
        } else if (sum < target) {
            left++;
        } else {
            right--;
        }
    }
    return new int[] {};
}
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

### DFS with HashMap
- Map old node -> cloned node
- Recursively clone neighbors

## Implementation
```java
private Map<Node, Node> visited = new HashMap<>();

public Node cloneGraph(Node node) {
    if (node == null) return null;
    
    if (visited.containsKey(node)) {
        return visited.get(node);
    }
    
    Node clone = new Node(node.val);
    visited.put(node, clone);
    
    for (Node neighbor : node.neighbors) {
        clone.neighbors.add(cloneGraph(neighbor));
    }
    return clone;
}
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
```java
public boolean canFinish(int numCourses, int[][] prerequisites) {
    int[] indegree = new int[numCourses];
    List<List<Integer>> adj = new ArrayList<>();
    
    for (int i = 0; i < numCourses; i++) adj.add(new ArrayList<>());
    
    for (int[] prereq : prerequisites) {
        adj.get(prereq[1]).add(prereq[0]);
        indegree[prereq[0]]++;
    }
    
    Queue<Integer> queue = new LinkedList<>();
    for (int i = 0; i < numCourses; i++) {
        if (indegree[i] == 0) queue.offer(i);
    }
    
    int count = 0;
    while (!queue.isEmpty()) {
        int course = queue.poll();
        count++;
        for (int next : adj.get(course)) {
            if (--indegree[next] == 0) queue.offer(next);
        }
    }
    return count == numCourses;
}
```

## Complexity
- **Time**: O(V + E)
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
```java
public boolean isPalindrome(ListNode head) {
    // Find middle
    ListNode slow = head, fast = head;
    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
    }
    
    // Reverse second half
    ListNode prev = null;
    while (slow != null) {
        ListNode next = slow.next;
        slow.next = prev;
        prev = slow;
        slow = next;
    }
    
    // Compare
    ListNode left = head, right = prev;
    while (right != null) {
        if (left.val != right.val) return false;
        left = left.next;
        right = right.next;
    }
    return true;
}
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

### HashMap + Doubly Linked List
- Map: key -> node
- DLL: Most recent at head, least at tail

## Implementation
```java
class LRUCache {
    class Node {
        int key, val;
        Node prev, next;
        Node(int k, int v) { key = k; val = v; }
    }
    
    private Map<Integer, Node> cache = new HashMap<>();
    private Node head = new Node(0, 0);
    private Node tail = new Node(0, 0);
    private int capacity;
    
    public LRUCache(int capacity) {
        this.capacity = capacity;
        head.next = tail;
        tail.prev = head;
    }
    
    public int get(int key) {
        if (!cache.containsKey(key)) return -1;
        Node node = cache.get(key);
        remove(node);
        insertAtHead(node);
        return node.val;
    }
    
    public void put(int key, int value) {
        if (cache.containsKey(key)) remove(cache.get(key));
        Node node = new Node(key, value);
        cache.put(key, node);
        insertAtHead(node);
        if (cache.size() > capacity) {
            Node lru = tail.prev;
            remove(lru);
            cache.remove(lru.key);
        }
    }
    
    private void remove(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }
    
    private void insertAtHead(Node node) {
        node.next = head.next;
        node.prev = head;
        head.next.prev = node;
        head.next = node;
    }
}
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
```java
public ListNode removeNthFromEnd(ListNode head, int n) {
    ListNode dummy = new ListNode(0);
    dummy.next = head;
    ListNode slow = dummy, fast = dummy;
    
    for (int i = 0; i <= n; i++) fast = fast.next;
    
    while (fast != null) {
        slow = slow.next;
        fast = fast.next;
    }
    
    slow.next = slow.next.next;
    return dummy.next;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
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
```java
public int findKthLargest(int[] nums, int k) {
    PriorityQueue<Integer> minHeap = new PriorityQueue<>();
    
    for (int num : nums) {
        minHeap.offer(num);
        if (minHeap.size() > k) {
            minHeap.poll();
        }
    }
    return minHeap.peek();
}
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
```java
public int[] topKFrequent(int[] nums, int k) {
    Map<Integer, Integer> count = new HashMap<>();
    for (int num : nums) {
        count.put(num, count.getOrDefault(num, 0) + 1);
    }
    
    List<Integer>[] buckets = new List[nums.length + 1];
    for (int key : count.keySet()) {
        int freq = count.get(key);
        if (buckets[freq] == null) buckets[freq] = new ArrayList<>();
        buckets[freq].add(key);
    }
    
    int[] result = new int[k];
    int idx = 0;
    for (int i = buckets.length - 1; i >= 0 && idx < k; i--) {
        if (buckets[i] != null) {
            for (int num : buckets[i]) {
                result[idx++] = num;
                if (idx == k) break;
            }
        }
    }
    return result;
}
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
```java
class MedianFinder {
    private PriorityQueue<Integer> lo = new PriorityQueue<>(Collections.reverseOrder());
    private PriorityQueue<Integer> hi = new PriorityQueue<>();
    
    public void addNum(int num) {
        lo.offer(num);
        hi.offer(lo.poll());
        if (hi.size() > lo.size()) {
            lo.offer(hi.poll());
        }
    }
    
    public double findMedian() {
        if (lo.size() > hi.size()) {
            return lo.peek();
        }
        return (lo.peek() + hi.peek()) / 2.0;
    }
}
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
```java
class MinStack {
    private Stack<Integer> stack = new Stack<>();
    private Stack<Integer> minStack = new Stack<>();
    
    public void push(int val) {
        stack.push(val);
        if (minStack.isEmpty() || val <= minStack.peek()) {
            minStack.push(val);
        }
    }
    
    public void pop() {
        if (stack.pop().equals(minStack.peek())) {
            minStack.pop();
        }
    }
    
    public int top() { return stack.peek(); }
    public int getMin() { return minStack.peek(); }
}
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
```java
public int[] dailyTemperatures(int[] temperatures) {
    int[] result = new int[temperatures.length];
    Stack<Integer> stack = new Stack<>();
    
    for (int i = 0; i < temperatures.length; i++) {
        while (!stack.isEmpty() && temperatures[stack.peek()] < temperatures[i]) {
            int j = stack.pop();
            result[j] = i - j;
        }
        stack.push(i);
    }
    return result;
}
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
- Track leftMax and rightMax
- Water at i = min(leftMax, rightMax) - height[i]

## Implementation
```java
public int trap(int[] height) {
    int left = 0, right = height.length - 1;
    int leftMax = 0, rightMax = 0;
    int water = 0;
    
    while (left < right) {
        if (height[left] < height[right]) {
            if (height[left] >= leftMax) {
                leftMax = height[left];
            } else {
                water += leftMax - height[left];
            }
            left++;
        } else {
            if (height[right] >= rightMax) {
                rightMax = height[right];
            } else {
                water += rightMax - height[right];
            }
            right--;
        }
    }
    return water;
}
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
```java
public int evalRPN(String[] tokens) {
    Stack<Integer> stack = new Stack<>();
    
    for (String token : tokens) {
        if ("+-*/".contains(token)) {
            int b = stack.pop(), a = stack.pop();
            switch (token) {
                case "+": stack.push(a + b); break;
                case "-": stack.push(a - b); break;
                case "*": stack.push(a * b); break;
                case "/": stack.push(a / b); break;
            }
        } else {
            stack.push(Integer.parseInt(token));
        }
    }
    return stack.pop();
}
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
```java
public int coinChange(int[] coins, int amount) {
    int[] dp = new int[amount + 1];
    Arrays.fill(dp, amount + 1);
    dp[0] = 0;
    
    for (int coin : coins) {
        for (int x = coin; x <= amount; x++) {
            dp[x] = Math.min(dp[x], dp[x - coin] + 1);
        }
    }
    return dp[amount] > amount ? -1 : dp[amount];
}
```

## Complexity
- **Time**: O(amount * coins.length)
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
```java
public int lengthOfLIS(int[] nums) {
    List<Integer> tails = new ArrayList<>();
    
    for (int num : nums) {
        int pos = Collections.binarySearch(tails, num);
        if (pos < 0) pos = -(pos + 1);
        
        if (pos == tails.size()) {
            tails.add(num);
        } else {
            tails.set(pos, num);
        }
    }
    return tails.size();
}
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
- `dp[i] = dp[j] && s[j:i] in wordDict`

## Implementation
```java
public boolean wordBreak(String s, List<String> wordDict) {
    Set<String> wordSet = new HashSet<>(wordDict);
    boolean[] dp = new boolean[s.length() + 1];
    dp[0] = true;
    
    for (int i = 1; i <= s.length(); i++) {
        for (int j = 0; j < i; j++) {
            if (dp[j] && wordSet.contains(s.substring(j, i))) {
                dp[i] = true;
                break;
            }
        }
    }
    return dp[s.length()];
}
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
```java
public List<String> generateParenthesis(int n) {
    List<String> result = new ArrayList<>();
    backtrack(result, "", 0, 0, n);
    return result;
}

private void backtrack(List<String> result, String curr, int open, int close, int n) {
    if (curr.length() == 2 * n) {
        result.add(curr);
        return;
    }
    if (open < n) backtrack(result, curr + "(", open + 1, close, n);
    if (close < open) backtrack(result, curr + ")", open, close + 1, n);
}
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
- Track used elements with boolean array

## Implementation
```java
public List<List<Integer>> permute(int[] nums) {
    List<List<Integer>> result = new ArrayList<>();
    backtrack(result, new ArrayList<>(), nums, new boolean[nums.length]);
    return result;
}

private void backtrack(List<List<Integer>> result, List<Integer> path, 
                       int[] nums, boolean[] used) {
    if (path.size() == nums.length) {
        result.add(new ArrayList<>(path));
        return;
    }
    for (int i = 0; i < nums.length; i++) {
        if (used[i]) continue;
        used[i] = true;
        path.add(nums[i]);
        backtrack(result, path, nums, used);
        path.remove(path.size() - 1);
        used[i] = false;
    }
}
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
```java
public List<List<String>> groupAnagrams(String[] strs) {
    Map<String, List<String>> map = new HashMap<>();
    
    for (String s : strs) {
        char[] chars = s.toCharArray();
        Arrays.sort(chars);
        String key = new String(chars);
        
        map.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
    }
    return new ArrayList<>(map.values());
}
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

### Prefix Sum + HashMap
- If `prefix[j] - prefix[i] = k`, subarray i+1 to j sums to k

## Implementation
```java
public int subarraySum(int[] nums, int k) {
    int count = 0, prefixSum = 0;
    Map<Integer, Integer> prefixCounts = new HashMap<>();
    prefixCounts.put(0, 1);
    
    for (int num : nums) {
        prefixSum += num;
        count += prefixCounts.getOrDefault(prefixSum - k, 0);
        prefixCounts.put(prefixSum, prefixCounts.getOrDefault(prefixSum, 0) + 1);
    }
    return count;
}
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
""",
}


def get_problem_slug(url):
    """Extract the problem slug from LeetCode URL."""
    match = re.search(r"/problems/([\w-]+)/?", url)
    return match.group(1) if match else None


def create_category_dir(sheet_name):
    """Create a sanitized directory name from sheet name."""
    sanitized = re.sub(r"[^\w\s-]", "", sheet_name.lower())
    sanitized = re.sub(r"[\s-]+", "_", sanitized)
    return sanitized


def main():
    """Generate all problem-specific mindmaps."""
    # Load the extracted problems
    with open("leetcode_problems.json", "r") as f:
        problems = json.load(f)

    print(
        f"Generating specific mindmaps for {len(PROBLEM_CONTENT)} problems with Java implementations..."
    )

    base_dir = Path("leetcode_mindmaps")
    base_dir.mkdir(exist_ok=True)

    updated = 0
    for problem in problems:
        slug = get_problem_slug(problem["url"])
        if not slug:
            continue

        if slug in PROBLEM_CONTENT:
            sheet_name = problem["context"]["sheet"]
            category_dir = create_category_dir(sheet_name)
            full_dir = base_dir / category_dir
            full_dir.mkdir(exist_ok=True)

            filepath = full_dir / f"{slug}.md"
            with open(filepath, "w") as f:
                f.write(PROBLEM_CONTENT[slug])
            updated += 1
            print(f"  Updated: {filepath}")

    print(f"\n✓ Updated {updated} mindmaps with specific Java content!")


if __name__ == "__main__":
    main()
