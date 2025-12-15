# Android Unlock Patterns

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
