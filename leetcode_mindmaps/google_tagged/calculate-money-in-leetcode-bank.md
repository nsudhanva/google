# Calculate Money in Leetcode Bank

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
