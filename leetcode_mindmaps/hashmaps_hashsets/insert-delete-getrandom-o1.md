# Insert Delete GetRandom O(1)

## Problem Info
- **Link**: [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/description/)
- **Category**: Hashmaps & HashSets
- **Difficulty**: Medium
- **Status**: DONE

## Approach
### Data Structure
- Hashmap, array

### Time Complexity
- O(1)

## Things to Remember
- Insert: insert into list, insert into map with index as value.
- Delete: swap the last element into that index, update map for that, then delete last element from list and corresponding map element.
- GetRandom: use Java Random() on the list index to retrieve.
