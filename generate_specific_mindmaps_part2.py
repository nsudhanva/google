#!/usr/bin/env python3
"""
Generate remaining problem-specific mindmaps - Part 2
"""

import json
import re
from pathlib import Path

PROBLEM_CONTENT_2 = {
    "add-binary": """# Add Binary

**Problem Link:** [Add Binary](https://leetcode.com/problems/add-binary/)
**Category:** Google tagged

## Problem Understanding
- Add two binary strings, return sum as binary string

## Approach
### Simulation with Carry
- Process from right to left, track carry

## Implementation
```java
public String addBinary(String a, String b) {
    StringBuilder sb = new StringBuilder();
    int i = a.length() - 1, j = b.length() - 1, carry = 0;
    
    while (i >= 0 || j >= 0 || carry != 0) {
        int sum = carry;
        if (i >= 0) sum += a.charAt(i--) - '0';
        if (j >= 0) sum += b.charAt(j--) - '0';
        sb.append(sum % 2);
        carry = sum / 2;
    }
    return sb.reverse().toString();
}
```

## Complexity
- **Time**: O(max(m, n))
- **Space**: O(max(m, n))
""",
    "binary-tree-level-order-traversal": """# Binary Tree Level Order Traversal

**Problem Link:** [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
**Category:** Google tagged

## Problem Understanding
- Return nodes level by level (BFS order)

## Approach
### BFS with Queue
- Process level by level using queue size

## Implementation
```java
public List<List<Integer>> levelOrder(TreeNode root) {
    List<List<Integer>> result = new ArrayList<>();
    if (root == null) return result;
    
    Queue<TreeNode> queue = new LinkedList<>();
    queue.offer(root);
    
    while (!queue.isEmpty()) {
        int size = queue.size();
        List<Integer> level = new ArrayList<>();
        for (int i = 0; i < size; i++) {
            TreeNode node = queue.poll();
            level.add(node.val);
            if (node.left != null) queue.offer(node.left);
            if (node.right != null) queue.offer(node.right);
        }
        result.add(level);
    }
    return result;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(n)
""",
    "binary-tree-preorder-traversal": """# Binary Tree Preorder Traversal

**Problem Link:** [Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)
**Category:** Google tagged

## Problem Understanding
- Return preorder: Node -> Left -> Right

## Implementation
```java
public List<Integer> preorderTraversal(TreeNode root) {
    List<Integer> result = new ArrayList<>();
    Stack<TreeNode> stack = new Stack<>();
    if (root != null) stack.push(root);
    
    while (!stack.isEmpty()) {
        TreeNode node = stack.pop();
        result.add(node.val);
        if (node.right != null) stack.push(node.right);
        if (node.left != null) stack.push(node.left);
    }
    return result;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(h)
""",
    "binary-tree-postorder-traversal": """# Binary Tree Postorder Traversal

**Problem Link:** [Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)
**Category:** Google tagged

## Problem Understanding
- Return postorder: Left -> Right -> Node

## Implementation
```java
public List<Integer> postorderTraversal(TreeNode root) {
    LinkedList<Integer> result = new LinkedList<>();
    Stack<TreeNode> stack = new Stack<>();
    if (root != null) stack.push(root);
    
    while (!stack.isEmpty()) {
        TreeNode node = stack.pop();
        result.addFirst(node.val);  // Add to front
        if (node.left != null) stack.push(node.left);
        if (node.right != null) stack.push(node.right);
    }
    return result;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(h)
""",
    "minimum-depth-of-binary-tree": """# Minimum Depth of Binary Tree

**Problem Link:** [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)
**Category:** Google tagged

## Problem Understanding
- Find minimum depth (root to nearest leaf)

## Approach
### BFS (Optimal for min depth)
- Stop at first leaf found

## Implementation
```java
public int minDepth(TreeNode root) {
    if (root == null) return 0;
    Queue<TreeNode> queue = new LinkedList<>();
    queue.offer(root);
    int depth = 1;
    
    while (!queue.isEmpty()) {
        int size = queue.size();
        for (int i = 0; i < size; i++) {
            TreeNode node = queue.poll();
            if (node.left == null && node.right == null) return depth;
            if (node.left != null) queue.offer(node.left);
            if (node.right != null) queue.offer(node.right);
        }
        depth++;
    }
    return depth;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(n)
""",
    "course-schedule-ii": """# Course Schedule II

**Problem Link:** [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)
**Category:** Google tagged

## Problem Understanding
- Return course order (topological sort)

## Implementation
```java
public int[] findOrder(int numCourses, int[][] prerequisites) {
    int[] indegree = new int[numCourses];
    List<List<Integer>> adj = new ArrayList<>();
    for (int i = 0; i < numCourses; i++) adj.add(new ArrayList<>());
    
    for (int[] p : prerequisites) {
        adj.get(p[1]).add(p[0]);
        indegree[p[0]]++;
    }
    
    Queue<Integer> queue = new LinkedList<>();
    for (int i = 0; i < numCourses; i++) {
        if (indegree[i] == 0) queue.offer(i);
    }
    
    int[] result = new int[numCourses];
    int idx = 0;
    while (!queue.isEmpty()) {
        int course = queue.poll();
        result[idx++] = course;
        for (int next : adj.get(course)) {
            if (--indegree[next] == 0) queue.offer(next);
        }
    }
    return idx == numCourses ? result : new int[0];
}
```

## Complexity
- **Time**: O(V + E)
- **Space**: O(V + E)
""",
    "graph-valid-tree": """# Graph Valid Tree

**Problem Link:** [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/)
**Category:** Google tagged

## Problem Understanding
- Check if edges form a valid tree (connected, no cycles)

## Approach
- Valid tree: n nodes, n-1 edges, all connected

## Implementation
```java
public boolean validTree(int n, int[][] edges) {
    if (edges.length != n - 1) return false;
    
    List<List<Integer>> adj = new ArrayList<>();
    for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
    for (int[] e : edges) {
        adj.get(e[0]).add(e[1]);
        adj.get(e[1]).add(e[0]);
    }
    
    Set<Integer> visited = new HashSet<>();
    Queue<Integer> queue = new LinkedList<>();
    queue.offer(0);
    visited.add(0);
    
    while (!queue.isEmpty()) {
        int node = queue.poll();
        for (int neighbor : adj.get(node)) {
            if (!visited.contains(neighbor)) {
                visited.add(neighbor);
                queue.offer(neighbor);
            }
        }
    }
    return visited.size() == n;
}
```

## Complexity
- **Time**: O(V + E)
- **Space**: O(V + E)
""",
    "evaluate-division": """# Evaluate Division

**Problem Link:** [Evaluate Division](https://leetcode.com/problems/evaluate-division/)
**Category:** Google tagged

## Problem Understanding
- Given a/b = k, evaluate queries like a/c

## Approach
### Graph DFS
- Build weighted graph, find path

## Implementation
```java
public double[] calcEquation(List<List<String>> equations, double[] values, 
                             List<List<String>> queries) {
    Map<String, Map<String, Double>> graph = new HashMap<>();
    
    for (int i = 0; i < equations.size(); i++) {
        String a = equations.get(i).get(0), b = equations.get(i).get(1);
        graph.computeIfAbsent(a, k -> new HashMap<>()).put(b, values[i]);
        graph.computeIfAbsent(b, k -> new HashMap<>()).put(a, 1.0 / values[i]);
    }
    
    double[] result = new double[queries.size()];
    for (int i = 0; i < queries.size(); i++) {
        result[i] = dfs(queries.get(i).get(0), queries.get(i).get(1), 
                        graph, new HashSet<>());
    }
    return result;
}

private double dfs(String src, String dst, Map<String, Map<String, Double>> graph, 
                   Set<String> visited) {
    if (!graph.containsKey(src)) return -1.0;
    if (src.equals(dst)) return 1.0;
    visited.add(src);
    for (Map.Entry<String, Double> e : graph.get(src).entrySet()) {
        if (!visited.contains(e.getKey())) {
            double result = dfs(e.getKey(), dst, graph, visited);
            if (result != -1.0) return e.getValue() * result;
        }
    }
    return -1.0;
}
```

## Complexity
- **Time**: O(Q * (V + E))
- **Space**: O(V + E)
""",
    "word-search": """# Word Search

**Problem Link:** [Word Search](https://leetcode.com/problems/word-search/)
**Category:** Recursion & DP

## Problem Understanding
- Find if word exists in grid via adjacent cells

## Approach
### Backtracking
- DFS from each cell, mark visited

## Implementation
```java
public boolean exist(char[][] board, String word) {
    for (int i = 0; i < board.length; i++) {
        for (int j = 0; j < board[0].length; j++) {
            if (dfs(board, word, i, j, 0)) return true;
        }
    }
    return false;
}

private boolean dfs(char[][] board, String word, int i, int j, int k) {
    if (k == word.length()) return true;
    if (i < 0 || i >= board.length || j < 0 || j >= board[0].length) return false;
    if (board[i][j] != word.charAt(k)) return false;
    
    char temp = board[i][j];
    board[i][j] = '#';
    boolean found = dfs(board, word, i+1, j, k+1) || dfs(board, word, i-1, j, k+1) ||
                    dfs(board, word, i, j+1, k+1) || dfs(board, word, i, j-1, k+1);
    board[i][j] = temp;
    return found;
}
```

## Complexity
- **Time**: O(m * n * 4^L)
- **Space**: O(L)
""",
    "word-search-ii": """# Word Search II

**Problem Link:** [Word Search II](https://leetcode.com/problems/word-search-ii/)
**Category:** Recursion & DP

## Problem Understanding
- Find all words from list in grid

## Approach
### Trie + Backtracking
- Build Trie, DFS with pruning

## Implementation
```java
class TrieNode {
    TrieNode[] children = new TrieNode[26];
    String word = null;
}

public List<String> findWords(char[][] board, String[] words) {
    TrieNode root = buildTrie(words);
    List<String> result = new ArrayList<>();
    
    for (int i = 0; i < board.length; i++) {
        for (int j = 0; j < board[0].length; j++) {
            dfs(board, i, j, root, result);
        }
    }
    return result;
}

private void dfs(char[][] board, int i, int j, TrieNode node, List<String> result) {
    if (i < 0 || i >= board.length || j < 0 || j >= board[0].length) return;
    char c = board[i][j];
    if (c == '#' || node.children[c - 'a'] == null) return;
    
    node = node.children[c - 'a'];
    if (node.word != null) {
        result.add(node.word);
        node.word = null;  // Avoid duplicates
    }
    
    board[i][j] = '#';
    dfs(board, i+1, j, node, result);
    dfs(board, i-1, j, node, result);
    dfs(board, i, j+1, node, result);
    dfs(board, i, j-1, node, result);
    board[i][j] = c;
}
```

## Complexity
- **Time**: O(m * n * 4^L)
- **Space**: O(sum of word lengths)
""",
    "edit-distance": """# Edit Distance

**Problem Link:** [Edit Distance](https://leetcode.com/problems/edit-distance/)
**Category:** Recursion & DP

## Problem Understanding
- Min operations to convert word1 to word2 (insert, delete, replace)

## Approach
### 2D DP
- dp[i][j] = min ops for word1[0..i] to word2[0..j]

## Implementation
```java
public int minDistance(String word1, String word2) {
    int m = word1.length(), n = word2.length();
    int[][] dp = new int[m + 1][n + 1];
    
    for (int i = 0; i <= m; i++) dp[i][0] = i;
    for (int j = 0; j <= n; j++) dp[0][j] = j;
    
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (word1.charAt(i-1) == word2.charAt(j-1)) {
                dp[i][j] = dp[i-1][j-1];
            } else {
                dp[i][j] = 1 + Math.min(dp[i-1][j-1], 
                               Math.min(dp[i-1][j], dp[i][j-1]));
            }
        }
    }
    return dp[m][n];
}
```

## Complexity
- **Time**: O(m * n)
- **Space**: O(m * n)
""",
    "maximum-product-subarray": """# Maximum Product Subarray

**Problem Link:** [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)
**Category:** Recursion & DP

## Problem Understanding
- Find contiguous subarray with largest product

## Approach
### Track Min and Max
- Negative * Negative can become max

## Implementation
```java
public int maxProduct(int[] nums) {
    int maxProd = nums[0], minProd = nums[0], result = nums[0];
    
    for (int i = 1; i < nums.length; i++) {
        if (nums[i] < 0) {
            int temp = maxProd;
            maxProd = minProd;
            minProd = temp;
        }
        maxProd = Math.max(nums[i], maxProd * nums[i]);
        minProd = Math.min(nums[i], minProd * nums[i]);
        result = Math.max(result, maxProd);
    }
    return result;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
""",
    "partition-equal-subset-sum": """# Partition Equal Subset Sum

**Problem Link:** [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)
**Category:** Recursion & DP

## Problem Understanding
- Can array be partitioned into two equal sum subsets?

## Approach
### 0/1 Knapsack DP
- Target = totalSum / 2

## Implementation
```java
public boolean canPartition(int[] nums) {
    int sum = 0;
    for (int n : nums) sum += n;
    if (sum % 2 != 0) return false;
    
    int target = sum / 2;
    boolean[] dp = new boolean[target + 1];
    dp[0] = true;
    
    for (int num : nums) {
        for (int j = target; j >= num; j--) {
            dp[j] = dp[j] || dp[j - num];
        }
    }
    return dp[target];
}
```

## Complexity
- **Time**: O(n * sum)
- **Space**: O(sum)
""",
    "fibonacci-number": """# Fibonacci Number

**Problem Link:** [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)
**Category:** Recursion & DP

## Implementation
```java
public int fib(int n) {
    if (n <= 1) return n;
    int a = 0, b = 1;
    for (int i = 2; i <= n; i++) {
        int temp = a + b;
        a = b;
        b = temp;
    }
    return b;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
""",
    "min-cost-climbing-stairs": """# Min Cost Climbing Stairs

**Problem Link:** [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/)
**Category:** Recursion & DP

## Implementation
```java
public int minCostClimbingStairs(int[] cost) {
    int n = cost.length;
    int[] dp = new int[n + 1];
    
    for (int i = 2; i <= n; i++) {
        dp[i] = Math.min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2]);
    }
    return dp[n];
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(n)
""",
    "pascals-triangle": """# Pascal's Triangle

**Problem Link:** [Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/)
**Category:** Recursion & DP

## Implementation
```java
public List<List<Integer>> generate(int numRows) {
    List<List<Integer>> result = new ArrayList<>();
    
    for (int i = 0; i < numRows; i++) {
        List<Integer> row = new ArrayList<>();
        for (int j = 0; j <= i; j++) {
            if (j == 0 || j == i) row.add(1);
            else row.add(result.get(i-1).get(j-1) + result.get(i-1).get(j));
        }
        result.add(row);
    }
    return result;
}
```

## Complexity
- **Time**: O(n²)
- **Space**: O(n²)
""",
    "counting-bits": """# Counting Bits

**Problem Link:** [Counting Bits](https://leetcode.com/problems/counting-bits/)
**Category:** Recursion & DP

## Approach
### DP: dp[i] = dp[i >> 1] + (i & 1)

## Implementation
```java
public int[] countBits(int n) {
    int[] dp = new int[n + 1];
    for (int i = 1; i <= n; i++) {
        dp[i] = dp[i >> 1] + (i & 1);
    }
    return dp;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(n)
""",
    "sudoku-solver": """# Sudoku Solver

**Problem Link:** [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)
**Category:** Recursion & DP

## Approach
### Backtracking

## Implementation
```java
public void solveSudoku(char[][] board) {
    solve(board);
}

private boolean solve(char[][] board) {
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            if (board[i][j] == '.') {
                for (char c = '1'; c <= '9'; c++) {
                    if (isValid(board, i, j, c)) {
                        board[i][j] = c;
                        if (solve(board)) return true;
                        board[i][j] = '.';
                    }
                }
                return false;
            }
        }
    }
    return true;
}

private boolean isValid(char[][] board, int row, int col, char c) {
    for (int i = 0; i < 9; i++) {
        if (board[row][i] == c) return false;
        if (board[i][col] == c) return false;
        if (board[3*(row/3) + i/3][3*(col/3) + i%3] == c) return false;
    }
    return true;
}
```

## Complexity
- **Time**: O(9^(empty cells))
- **Space**: O(81)
""",
    "merge-k-sorted-lists": """# Merge K Sorted Lists

**Problem Link:** [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
**Category:** Heaps / Linked Lists

## Approach
### Min Heap

## Implementation
```java
public ListNode mergeKLists(ListNode[] lists) {
    PriorityQueue<ListNode> pq = new PriorityQueue<>((a, b) -> a.val - b.val);
    
    for (ListNode node : lists) {
        if (node != null) pq.offer(node);
    }
    
    ListNode dummy = new ListNode(0);
    ListNode curr = dummy;
    
    while (!pq.isEmpty()) {
        ListNode node = pq.poll();
        curr.next = node;
        curr = curr.next;
        if (node.next != null) pq.offer(node.next);
    }
    return dummy.next;
}
```

## Complexity
- **Time**: O(N log k)
- **Space**: O(k)
""",
    "copy-list-with-random-pointer": """# Copy List with Random Pointer

**Problem Link:** [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/)
**Category:** Linked Lists

## Implementation
```java
public Node copyRandomList(Node head) {
    if (head == null) return null;
    Map<Node, Node> map = new HashMap<>();
    
    Node curr = head;
    while (curr != null) {
        map.put(curr, new Node(curr.val));
        curr = curr.next;
    }
    
    curr = head;
    while (curr != null) {
        map.get(curr).next = map.get(curr.next);
        map.get(curr).random = map.get(curr.random);
        curr = curr.next;
    }
    return map.get(head);
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(n)
""",
    "reverse-nodes-in-k-group": """# Reverse Nodes in K-Group

**Problem Link:** [Reverse Nodes in K-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)
**Category:** Linked Lists

## Implementation
```java
public ListNode reverseKGroup(ListNode head, int k) {
    ListNode curr = head;
    int count = 0;
    while (curr != null && count < k) {
        curr = curr.next;
        count++;
    }
    if (count == k) {
        curr = reverseKGroup(curr, k);
        while (count-- > 0) {
            ListNode next = head.next;
            head.next = curr;
            curr = head;
            head = next;
        }
        head = curr;
    }
    return head;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(n/k)
""",
    "flatten-a-multilevel-doubly-linked-list": """# Flatten a Multilevel Doubly Linked List

**Problem Link:** [Flatten a Multilevel Doubly Linked List](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/)
**Category:** Linked Lists

## Implementation
```java
public Node flatten(Node head) {
    if (head == null) return null;
    Node curr = head;
    while (curr != null) {
        if (curr.child != null) {
            Node next = curr.next;
            Node child = flatten(curr.child);
            curr.next = child;
            child.prev = curr;
            curr.child = null;
            while (curr.next != null) curr = curr.next;
            if (next != null) {
                curr.next = next;
                next.prev = curr;
            }
        }
        curr = curr.next;
    }
    return head;
}
```
""",
    "kth-largest-element-in-a-stream": """# Kth Largest Element in a Stream

**Problem Link:** [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)
**Category:** Heaps

## Implementation
```java
class KthLargest {
    PriorityQueue<Integer> minHeap = new PriorityQueue<>();
    int k;
    
    public KthLargest(int k, int[] nums) {
        this.k = k;
        for (int n : nums) add(n);
    }
    
    public int add(int val) {
        minHeap.offer(val);
        if (minHeap.size() > k) minHeap.poll();
        return minHeap.peek();
    }
}
```

## Complexity
- **Time**: O(log k) per add
- **Space**: O(k)
""",
    "basic-calculator-ii": """# Basic Calculator II

**Problem Link:** [Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/)
**Category:** Stacks & Queues

## Implementation
```java
public int calculate(String s) {
    Stack<Integer> stack = new Stack<>();
    int num = 0;
    char sign = '+';
    
    for (int i = 0; i < s.length(); i++) {
        char c = s.charAt(i);
        if (Character.isDigit(c)) {
            num = num * 10 + (c - '0');
        }
        if ((!Character.isDigit(c) && c != ' ') || i == s.length() - 1) {
            if (sign == '+') stack.push(num);
            else if (sign == '-') stack.push(-num);
            else if (sign == '*') stack.push(stack.pop() * num);
            else if (sign == '/') stack.push(stack.pop() / num);
            sign = c;
            num = 0;
        }
    }
    int result = 0;
    for (int n : stack) result += n;
    return result;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(n)
""",
    "implement-queue-using-stacks": """# Implement Queue using Stacks

**Problem Link:** [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)
**Category:** Stacks & Queues

## Implementation
```java
class MyQueue {
    Stack<Integer> in = new Stack<>();
    Stack<Integer> out = new Stack<>();
    
    public void push(int x) { in.push(x); }
    
    public int pop() {
        peek();
        return out.pop();
    }
    
    public int peek() {
        if (out.isEmpty()) {
            while (!in.isEmpty()) out.push(in.pop());
        }
        return out.peek();
    }
    
    public boolean empty() { return in.isEmpty() && out.isEmpty(); }
}
```

## Complexity
- **Amortized**: O(1) per operation
""",
    "implement-stack-using-queues": """# Implement Stack using Queues

**Problem Link:** [Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)
**Category:** Stacks & Queues

## Implementation
```java
class MyStack {
    Queue<Integer> queue = new LinkedList<>();
    
    public void push(int x) {
        queue.offer(x);
        int size = queue.size();
        while (size-- > 1) queue.offer(queue.poll());
    }
    
    public int pop() { return queue.poll(); }
    public int top() { return queue.peek(); }
    public boolean empty() { return queue.isEmpty(); }
}
```
""",
    "next-greater-element-i": """# Next Greater Element I

**Problem Link:** [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/)
**Category:** Stacks & Queues

## Implementation
```java
public int[] nextGreaterElement(int[] nums1, int[] nums2) {
    Map<Integer, Integer> map = new HashMap<>();
    Stack<Integer> stack = new Stack<>();
    
    for (int num : nums2) {
        while (!stack.isEmpty() && stack.peek() < num) {
            map.put(stack.pop(), num);
        }
        stack.push(num);
    }
    
    int[] result = new int[nums1.length];
    for (int i = 0; i < nums1.length; i++) {
        result[i] = map.getOrDefault(nums1[i], -1);
    }
    return result;
}
```

## Complexity
- **Time**: O(n + m)
- **Space**: O(n)
""",
    "design-circular-queue": """# Design Circular Queue

**Problem Link:** [Design Circular Queue](https://leetcode.com/problems/design-circular-queue/)
**Category:** Stacks & Queues

## Implementation
```java
class MyCircularQueue {
    int[] data;
    int head = 0, tail = -1, size = 0;
    
    public MyCircularQueue(int k) { data = new int[k]; }
    
    public boolean enQueue(int value) {
        if (isFull()) return false;
        tail = (tail + 1) % data.length;
        data[tail] = value;
        size++;
        return true;
    }
    
    public boolean deQueue() {
        if (isEmpty()) return false;
        head = (head + 1) % data.length;
        size--;
        return true;
    }
    
    public int Front() { return isEmpty() ? -1 : data[head]; }
    public int Rear() { return isEmpty() ? -1 : data[tail]; }
    public boolean isEmpty() { return size == 0; }
    public boolean isFull() { return size == data.length; }
}
```
""",
    "moving-average-from-data-stream": """# Moving Average from Data Stream

**Problem Link:** [Moving Average from Data Stream](https://leetcode.com/problems/moving-average-from-data-stream/)
**Category:** Stacks & Queues

## Implementation
```java
class MovingAverage {
    Queue<Integer> queue = new LinkedList<>();
    int size, sum = 0;
    
    public MovingAverage(int size) { this.size = size; }
    
    public double next(int val) {
        if (queue.size() == size) sum -= queue.poll();
        queue.offer(val);
        sum += val;
        return (double) sum / queue.size();
    }
}
```

## Complexity
- **Time**: O(1)
- **Space**: O(size)
""",
    "design-hit-counter": """# Design Hit Counter

**Problem Link:** [Design Hit Counter](https://leetcode.com/problems/design-hit-counter/)
**Category:** Stacks & Queues

## Implementation
```java
class HitCounter {
    Queue<Integer> queue = new LinkedList<>();
    
    public void hit(int timestamp) {
        queue.offer(timestamp);
    }
    
    public int getHits(int timestamp) {
        while (!queue.isEmpty() && timestamp - queue.peek() >= 300) {
            queue.poll();
        }
        return queue.size();
    }
}
```
""",
    "longest-consecutive-sequence": """# Longest Consecutive Sequence

**Problem Link:** [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)
**Category:** Hashmaps

## Implementation
```java
public int longestConsecutive(int[] nums) {
    Set<Integer> set = new HashSet<>();
    for (int n : nums) set.add(n);
    
    int longest = 0;
    for (int n : set) {
        if (!set.contains(n - 1)) {  // Start of sequence
            int curr = n, len = 1;
            while (set.contains(curr + 1)) {
                curr++;
                len++;
            }
            longest = Math.max(longest, len);
        }
    }
    return longest;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(n)
""",
    "insert-delete-getrandom-o1": """# Insert Delete GetRandom O(1)

**Problem Link:** [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/)
**Category:** Hashmaps

## Implementation
```java
class RandomizedSet {
    List<Integer> list = new ArrayList<>();
    Map<Integer, Integer> map = new HashMap<>();
    Random rand = new Random();
    
    public boolean insert(int val) {
        if (map.containsKey(val)) return false;
        map.put(val, list.size());
        list.add(val);
        return true;
    }
    
    public boolean remove(int val) {
        if (!map.containsKey(val)) return false;
        int idx = map.get(val);
        int last = list.get(list.size() - 1);
        list.set(idx, last);
        map.put(last, idx);
        list.remove(list.size() - 1);
        map.remove(val);
        return true;
    }
    
    public int getRandom() {
        return list.get(rand.nextInt(list.size()));
    }
}
```

## Complexity
- **Time**: O(1) all operations
- **Space**: O(n)
""",
    "design-hashmap": """# Design HashMap

**Problem Link:** [Design HashMap](https://leetcode.com/problems/design-hashmap/)
**Category:** Hashmaps

## Implementation
```java
class MyHashMap {
    int[] data = new int[1000001];
    
    public MyHashMap() { Arrays.fill(data, -1); }
    public void put(int key, int value) { data[key] = value; }
    public int get(int key) { return data[key]; }
    public void remove(int key) { data[key] = -1; }
}
```
""",
    "snapshot-array": """# Snapshot Array

**Problem Link:** [Snapshot Array](https://leetcode.com/problems/snapshot-array/)
**Category:** Hashmaps

## Implementation
```java
class SnapshotArray {
    List<TreeMap<Integer, Integer>> arr;
    int snapId = 0;
    
    public SnapshotArray(int length) {
        arr = new ArrayList<>();
        for (int i = 0; i < length; i++) {
            TreeMap<Integer, Integer> map = new TreeMap<>();
            map.put(0, 0);
            arr.add(map);
        }
    }
    
    public void set(int index, int val) {
        arr.get(index).put(snapId, val);
    }
    
    public int snap() { return snapId++; }
    
    public int get(int index, int snap_id) {
        return arr.get(index).floorEntry(snap_id).getValue();
    }
}
```
""",
    "convert-binary-search-tree-to-sorted-doubly-linked-list": """# Convert Binary Search Tree to Sorted Doubly Linked List

**Problem Link:** [Convert Binary Search Tree to Sorted Doubly Linked List](https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/)
**Category:** Graphs & Trees

## Implementation
```java
Node first = null, last = null;

public Node treeToDoublyList(Node root) {
    if (root == null) return null;
    inorder(root);
    last.right = first;
    first.left = last;
    return first;
}

private void inorder(Node node) {
    if (node == null) return;
    inorder(node.left);
    if (last != null) {
        last.right = node;
        node.left = last;
    } else {
        first = node;
    }
    last = node;
    inorder(node.right);
}
```
""",
    "flatten-binary-tree-to-linked-list": """# Flatten Binary Tree to Linked List

**Problem Link:** [Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)
**Category:** Graphs & Trees

## Implementation
```java
public void flatten(TreeNode root) {
    TreeNode curr = root;
    while (curr != null) {
        if (curr.left != null) {
            TreeNode rightmost = curr.left;
            while (rightmost.right != null) rightmost = rightmost.right;
            rightmost.right = curr.right;
            curr.right = curr.left;
            curr.left = null;
        }
        curr = curr.right;
    }
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
""",
    "number-of-connected-components-in-an-undirected-graph": """# Number of Connected Components in an Undirected Graph

**Problem Link:** [Number of Connected Components](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)
**Category:** Google tagged

## Implementation
```java
public int countComponents(int n, int[][] edges) {
    int[] parent = new int[n];
    for (int i = 0; i < n; i++) parent[i] = i;
    
    int count = n;
    for (int[] e : edges) {
        int p1 = find(parent, e[0]), p2 = find(parent, e[1]);
        if (p1 != p2) {
            parent[p1] = p2;
            count--;
        }
    }
    return count;
}

private int find(int[] parent, int i) {
    while (parent[i] != i) {
        parent[i] = parent[parent[i]];
        i = parent[i];
    }
    return i;
}
```

## Complexity
- **Time**: O(E * α(N))
- **Space**: O(N)
""",
    "minimum-height-trees": """# Minimum Height Trees

**Problem Link:** [Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees/)
**Category:** Google tagged

## Approach
### Topological Sort (Trim Leaves)
- Remove leaves layer by layer until 1-2 nodes remain

## Implementation
```java
public List<Integer> findMinHeightTrees(int n, int[][] edges) {
    if (n == 1) return Arrays.asList(0);
    
    List<Set<Integer>> adj = new ArrayList<>();
    for (int i = 0; i < n; i++) adj.add(new HashSet<>());
    for (int[] e : edges) {
        adj.get(e[0]).add(e[1]);
        adj.get(e[1]).add(e[0]);
    }
    
    List<Integer> leaves = new ArrayList<>();
    for (int i = 0; i < n; i++) {
        if (adj.get(i).size() == 1) leaves.add(i);
    }
    
    int remaining = n;
    while (remaining > 2) {
        remaining -= leaves.size();
        List<Integer> newLeaves = new ArrayList<>();
        for (int leaf : leaves) {
            int neighbor = adj.get(leaf).iterator().next();
            adj.get(neighbor).remove(leaf);
            if (adj.get(neighbor).size() == 1) newLeaves.add(neighbor);
        }
        leaves = newLeaves;
    }
    return leaves;
}
```
""",
    "valid-palindrome-ii": """# Valid Palindrome II

**Problem Link:** [Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/)
**Category:** Google tagged

## Implementation
```java
public boolean validPalindrome(String s) {
    int l = 0, r = s.length() - 1;
    while (l < r) {
        if (s.charAt(l) != s.charAt(r)) {
            return isPalin(s, l+1, r) || isPalin(s, l, r-1);
        }
        l++; r--;
    }
    return true;
}

private boolean isPalin(String s, int l, int r) {
    while (l < r) {
        if (s.charAt(l++) != s.charAt(r--)) return false;
    }
    return true;
}
```
""",
    "find-the-celebrity": """# Find the Celebrity

**Problem Link:** [Find the Celebrity](https://leetcode.com/problems/find-the-celebrity/)
**Category:** Google tagged

## Approach
- Celebrity: everyone knows them, they know no one

## Implementation
```java
public int findCelebrity(int n) {
    int candidate = 0;
    for (int i = 1; i < n; i++) {
        if (knows(candidate, i)) candidate = i;
    }
    for (int i = 0; i < n; i++) {
        if (i != candidate) {
            if (knows(candidate, i) || !knows(i, candidate)) return -1;
        }
    }
    return candidate;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
""",
    "number-of-1-bits": """# Number of 1 Bits

**Problem Link:** [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)
**Category:** Recursion & DP

## Implementation
```java
public int hammingWeight(int n) {
    int count = 0;
    while (n != 0) {
        count += (n & 1);
        n >>>= 1;
    }
    return count;
}
```

## Complexity
- **Time**: O(32) = O(1)
- **Space**: O(1)
""",
    "binary-tree-paths": """# Binary Tree Paths

**Problem Link:** [Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/)
**Category:** Recursion & DP

## Implementation
```java
public List<String> binaryTreePaths(TreeNode root) {
    List<String> result = new ArrayList<>();
    if (root != null) dfs(root, "", result);
    return result;
}

private void dfs(TreeNode node, String path, List<String> result) {
    if (node.left == null && node.right == null) {
        result.add(path + node.val);
        return;
    }
    if (node.left != null) dfs(node.left, path + node.val + "->", result);
    if (node.right != null) dfs(node.right, path + node.val + "->", result);
}
```
""",
    "letter-case-permutation": """# Letter Case Permutation

**Problem Link:** [Letter Case Permutation](https://leetcode.com/problems/letter-case-permutation/)
**Category:** Recursion & DP

## Implementation
```java
public List<String> letterCasePermutation(String s) {
    List<String> result = new ArrayList<>();
    backtrack(s.toCharArray(), 0, result);
    return result;
}

private void backtrack(char[] chars, int idx, List<String> result) {
    if (idx == chars.length) {
        result.add(new String(chars));
        return;
    }
    backtrack(chars, idx + 1, result);
    if (Character.isLetter(chars[idx])) {
        chars[idx] ^= 32;  // Toggle case
        backtrack(chars, idx + 1, result);
        chars[idx] ^= 32;
    }
}
```
""",
    "sum-of-all-subset-xor-totals": """# Sum of All Subset XOR Totals

**Problem Link:** [Sum of All Subset XOR Totals](https://leetcode.com/problems/sum-of-all-subset-xor-totals/)
**Category:** Recursion & DP

## Implementation
```java
public int subsetXORSum(int[] nums) {
    return helper(nums, 0, 0);
}

private int helper(int[] nums, int idx, int curr) {
    if (idx == nums.length) return curr;
    return helper(nums, idx + 1, curr ^ nums[idx]) + helper(nums, idx + 1, curr);
}
```
""",
    "strobogrammatic-number-ii": """# Strobogrammatic Number II

**Problem Link:** [Strobogrammatic Number II](https://leetcode.com/problems/strobogrammatic-number-ii/)
**Category:** Recursion & DP

## Implementation
```java
public List<String> findStrobogrammatic(int n) {
    return helper(n, n);
}

private List<String> helper(int n, int m) {
    if (n == 0) return new ArrayList<>(Arrays.asList(""));
    if (n == 1) return new ArrayList<>(Arrays.asList("0", "1", "8"));
    
    List<String> middles = helper(n - 2, m);
    List<String> result = new ArrayList<>();
    
    for (String middle : middles) {
        if (n != m) result.add("0" + middle + "0");
        result.add("1" + middle + "1");
        result.add("6" + middle + "9");
        result.add("8" + middle + "8");
        result.add("9" + middle + "6");
    }
    return result;
}
```
""",
    "android-unlock-patterns": """# Android Unlock Patterns

**Problem Link:** [Android Unlock Patterns](https://leetcode.com/problems/android-unlock-patterns/)
**Category:** Recursion & DP

## Implementation
```java
public int numberOfPatterns(int m, int n) {
    int[][] skip = new int[10][10];
    skip[1][3] = skip[3][1] = 2;
    skip[1][7] = skip[7][1] = 4;
    skip[3][9] = skip[9][3] = 6;
    skip[7][9] = skip[9][7] = 8;
    skip[1][9] = skip[9][1] = skip[3][7] = skip[7][3] = 5;
    skip[2][8] = skip[8][2] = skip[4][6] = skip[6][4] = 5;
    
    boolean[] visited = new boolean[10];
    int result = 0;
    for (int i = m; i <= n; i++) {
        result += dfs(1, i - 1, skip, visited) * 4;
        result += dfs(2, i - 1, skip, visited) * 4;
        result += dfs(5, i - 1, skip, visited);
    }
    return result;
}

private int dfs(int curr, int remain, int[][] skip, boolean[] visited) {
    if (remain == 0) return 1;
    visited[curr] = true;
    int count = 0;
    for (int next = 1; next <= 9; next++) {
        if (!visited[next] && (skip[curr][next] == 0 || visited[skip[curr][next]])) {
            count += dfs(next, remain - 1, skip, visited);
        }
    }
    visited[curr] = false;
    return count;
}
```
""",
    "construct-quad-tree": """# Construct Quad Tree

**Problem Link:** [Construct Quad Tree](https://leetcode.com/problems/construct-quad-tree/)
**Category:** Recursion & DP

## Implementation
```java
public Node construct(int[][] grid) {
    return build(grid, 0, 0, grid.length);
}

private Node build(int[][] grid, int r, int c, int len) {
    if (len == 1) return new Node(grid[r][c] == 1, true);
    
    int half = len / 2;
    Node tl = build(grid, r, c, half);
    Node tr = build(grid, r, c + half, half);
    Node bl = build(grid, r + half, c, half);
    Node br = build(grid, r + half, c + half, half);
    
    if (tl.isLeaf && tr.isLeaf && bl.isLeaf && br.isLeaf &&
        tl.val == tr.val && tr.val == bl.val && bl.val == br.val) {
        return new Node(tl.val, true);
    }
    return new Node(false, false, tl, tr, bl, br);
}
```
""",
    "binary-watch": """# Binary Watch

**Problem Link:** [Binary Watch](https://leetcode.com/problems/binary-watch/)
**Category:** Recursion & DP

## Implementation
```java
public List<String> readBinaryWatch(int turnedOn) {
    List<String> result = new ArrayList<>();
    for (int h = 0; h < 12; h++) {
        for (int m = 0; m < 60; m++) {
            if (Integer.bitCount(h) + Integer.bitCount(m) == turnedOn) {
                result.add(String.format("%d:%02d", h, m));
            }
        }
    }
    return result;
}
```
""",
    "calculate-money-in-leetcode-bank": """# Calculate Money in Leetcode Bank

**Problem Link:** [Calculate Money in Leetcode Bank](https://leetcode.com/problems/calculate-money-in-leetcode-bank/)
**Category:** Google tagged

## Implementation
```java
public int totalMoney(int n) {
    int weeks = n / 7, days = n % 7;
    int weekSum = 28 * weeks + 7 * (weeks * (weeks - 1)) / 2;
    int remSum = days * (weeks + 1) + days * (days - 1) / 2;
    return weekSum + remSum;
}
```

## Complexity
- **Time**: O(1)
- **Space**: O(1)
""",
}


def get_problem_slug(url):
    match = re.search(r"/problems/([\w-]+)/?", url)
    return match.group(1) if match else None


def create_category_dir(sheet_name):
    sanitized = re.sub(r"[^\w\s-]", "", sheet_name.lower())
    sanitized = re.sub(r"[\s-]+", "_", sanitized)
    return sanitized


def main():
    with open("leetcode_problems.json", "r") as f:
        problems = json.load(f)

    print(f"Generating remaining {len(PROBLEM_CONTENT_2)} mindmaps with Java...")

    base_dir = Path("leetcode_mindmaps")
    base_dir.mkdir(exist_ok=True)

    updated = 0
    for problem in problems:
        slug = get_problem_slug(problem["url"])
        if not slug:
            continue

        if slug in PROBLEM_CONTENT_2:
            sheet_name = problem["context"]["sheet"]
            category_dir = create_category_dir(sheet_name)
            full_dir = base_dir / category_dir
            full_dir.mkdir(exist_ok=True)

            filepath = full_dir / f"{slug}.md"
            with open(filepath, "w") as f:
                f.write(PROBLEM_CONTENT_2[slug])
            updated += 1
            print(f"  Updated: {filepath}")

    print(f"\n✓ Updated {updated} additional mindmaps!")


if __name__ == "__main__":
    main()
