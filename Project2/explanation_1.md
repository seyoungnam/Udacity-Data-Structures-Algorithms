## Problem 1 : Least Recently Used Cache

### Reasoning for choosing data sturctures and/or algorithms

The main data structures applied in this problem are hashmap (dictionary in Python) and double linked list. Given that both `get()` and `set()` operation requires `insert` and `remove` operations and each operation should be performed in a constant time, hashmap is very useful to check if the node containing the target value exists in the cache. Double linked list also plays a significant role in doing `insert` and `remove` operations in a constant time.

### Time Complexity

- `get()`: O(1) - Hashmap assures to locate the node in a constant time, and the time complexity for `remove` and `insert` operations is O(1) in a double linked list.
- `set()`: O(1) - Hashmap assures to locate the node in a constant time, and the time complexity for `remove` and `insert` operations is O(1) in a double linked list.

### Space Complexity

Space complexity for LRU_Cache class is O(n) where n represents the size of the cache.
