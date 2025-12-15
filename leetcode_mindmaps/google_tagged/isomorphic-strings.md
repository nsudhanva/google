# Isomorphic Strings

**Problem Link:** [Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/)

**Category:** Google tagged

## Problem Understanding
- Input: `s`, `t`
- Output: `true` if chars in `s` can be replaced to get `t`.
- Rule: Map char to char. No two map to same. Order preserved.

## Approach

### Two Hash Maps
- **Idea**: Track `s->t` and `t->s` mapping.
- **Algorithm**:
  - `mapST = {}, mapTS = {}`
  - Loop `c1, c2` in `zip(s, t)`:
    - If `c1` in `mapST` and `mapST[c1] != c2`: return `False`
    - If `c2` in `mapTS` and `mapTS[c2] != c1`: return `False`
    - `mapST[c1] = c2`, `mapTS[c2] = c1`
  - Return `True`

### Single Map + Set
- **Idea**: Map `s->t`, and track used values in `set`.
- **Complexity**: Same.

## Implementation
- **Python**:
  ```python
  m1, m2 = {}, {}
  for c1, c2 in zip(s, t):
      if (c1 in m1 and m1[c1] != c2) or (c2 in m2 and m2[c2] != c1):
          return False
      m1[c1] = c2
      m2[c2] = c1
  return True
  ```

## Complexity Analysis
- **Time**: O(n)
- **Space**: O(1) (ASCII size)

## Common Pitfalls
- **One-way Mapping**: `ab` -> `aa`. `a->a`, `b->a`. Valid? No, two chars map to same. Need bijection.
