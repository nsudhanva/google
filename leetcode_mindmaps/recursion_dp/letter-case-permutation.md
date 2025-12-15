# Letter Case Permutation

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
