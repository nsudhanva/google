# Daily Temperatures

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
