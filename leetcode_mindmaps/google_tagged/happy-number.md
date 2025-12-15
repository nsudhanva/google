# Happy Number

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
