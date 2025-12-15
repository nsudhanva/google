# Best Time to Buy and Sell Stock

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
