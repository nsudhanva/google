# Group Anagrams

**Problem Link:** [Group Anagrams](https://leetcode.com/problems/group-anagrams/)
**Category:** Hashmaps

## Problem Understanding
- Group strings that are anagrams

## Approach

### Sorted String as Key
- Anagrams have same sorted form

## Implementation
```java
public List<List<String>> groupAnagrams(String[] strs) {
    Map<String, List<String>> map = new HashMap<>();
    
    for (String s : strs) {
        char[] chars = s.toCharArray();
        Arrays.sort(chars);
        String key = new String(chars);
        
        map.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
    }
    return new ArrayList<>(map.values());
}
```

## Complexity
- **Time**: O(n * k log k) where k is max string length
- **Space**: O(n * k)
