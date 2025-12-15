# Snapshot Array

**Problem Link:** [Snapshot Array](https://leetcode.com/problems/snapshot-array/)
**Category:** Hashmaps

## Implementation
```java
class SnapshotArray {
    List<TreeMap<Integer, Integer>> arr;
    int snapId = 0;
    
    public SnapshotArray(int length) {
        arr = new ArrayList<>();
        for (int i = 0; i < length; i++) {
            TreeMap<Integer, Integer> map = new TreeMap<>();
            map.put(0, 0);
            arr.add(map);
        }
    }
    
    public void set(int index, int val) {
        arr.get(index).put(snapId, val);
    }
    
    public int snap() { return snapId++; }
    
    public int get(int index, int snap_id) {
        return arr.get(index).floorEntry(snap_id).getValue();
    }
}
```
