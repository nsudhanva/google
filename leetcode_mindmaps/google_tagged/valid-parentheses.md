# Valid Parentheses

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
