# Edit Distance

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
