## Problem 7 : HTTPRouter using a Trie

### Reasoning for choosing data structures and/or algorithms

The `RouteTrie` class possesses the root attribute that contains the hierarchical structure of possible HTTP paths and their handlers. A `Trie` structure is optimal to represent the hierarchical structure because it allows us to do very quick lookups of a particular data, the handler in this case.

In terms of time complexity, `Hashmap` of O(1) is faster than `Trie` of O(m), where m represents the number of the subpaths in the entire HTTP path. As for space complexity, however, `Trie` takes only O(n) while `Hashmap` takes O(n*m) (n represents the number of existing HTTP paths).

### Time Complexity

* `RouteTrie` class:
    * `insert()`: O(n) - n represents the number of the subpaths in a given HTTP path. For example, n equals three for `/home/about/me`. To insert handler under `me` node in `Trie` structure, we have to visit `home`, `about`, and `me`.
    * `find()`: O(n) - Same analogy with `insert()`. We have to visit each node from `home` to `me` to find the handler for `/home/about/me`.

* `RouteTrieNode` class:
    * `insert()`: O(1) - this function visits a single node and inserts a new node to it.

* `Router` class:
    * `add_handler()`: O(n) - spliting a HTTP path takes O(n) and inserting handler to the target node also takes O(n).
    * `lookup()`: O(n) - both spliting a path and finding handler takes O(m).
    * `split_path()`: O(n) - for spliting a given path, the function must visit each sub path at least once, thus O(n).

### Space Complexity

* `RouteTrie` class:
    * `insert()`: O(n) - Take `/home/about/me` as an example, all three sub paths possess a node, thus taking n spaces.
    * `find()`: O(1) - This function only takes up a space for `curr` node.

* `RouteTrieNode` class:
    * `insert()`: O(1) - it takes up a space for `self.children[path]` node.

* `Router` class:
    * `add_handler()`: O(n) - the length of splitted HTTP path is O(n). Inserting handler to the target node also takes O(n) as explained in `insert()` of `RouteTrie` class. Thus, O(n) in total.
    * `lookup()`: O(n) - Although `find()` takes O(1) space, splitting a HTTP path takes O(n) space. Thus, O(n) in total. 
    * `split_path()`: O(n) - for splitting a given path consisting of n sub-paths, the length of the created list ends up with n, thus O(n).


