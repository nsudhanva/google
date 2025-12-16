# Copy List with Random Pointer

## Problem Info
- **Link**: [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/description/)
- **Category**: Linked Lists
- **Difficulty**: Medium
- **Status**: DONE

## Approach
### Data Structure
- Linked List, Hashmap

### Time Complexity
- O(n)

## Things to Remember
- I used a hashmap to store old and new nodes.
- Copied as a normal list while adding to the map and traversing again and assigning random pointers by looking at the map.

## Additional Notes
- This can also be done recursively with a hashmap - check if map contains, then return. otherwise create a new node, save it in the map, then call func recursively on next and random while assigning them. With constant space: traverse the list while creating copy and storing each copy as next of old node. Then go through again and assign randoms to the new ones. Then decouple the two lists and return
