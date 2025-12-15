# Isomorphic Strings

**Problem Link:** [Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/)
**Category:** Google tagged

## Problem Understanding
- Check if chars in `s` can map to `t` (bijective mapping)

## Approach

### Two HashMaps
- Track `s->t` and `t->s` mappings

## Implementation
```java
public boolean isIsomorphic(String s, String t) {
    Map<Character, Character> mapST = new HashMap<>();
    Map<Character, Character> mapTS = new HashMap<>();
    
    for (int i = 0; i < s.length(); i++) {
        char c1 = s.charAt(i), c2 = t.charAt(i);
        
        if (mapST.containsKey(c1) && mapST.get(c1) != c2) return false;
        if (mapTS.containsKey(c2) && mapTS.get(c2) != c1) return false;
        
        mapST.put(c1, c2);
        mapTS.put(c2, c1);
    }
    return true;
}
```

## Complexity
- **Time**: O(n)
- **Space**: O(1)
