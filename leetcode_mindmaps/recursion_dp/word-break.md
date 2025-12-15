# Word Break

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
