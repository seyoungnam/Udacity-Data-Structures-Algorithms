class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRU_Cache(object):
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = dict()
        # left = helper node located in left side of the Least Recently Used(LRU) cache
        # right = helper node located in right side of the Most Recently Used(MRU) cache
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node from list
    def remove(self, node):
        pre_node, nxt_node = node.prev, node.next
        pre_node.next, nxt_node.prev = nxt_node, pre_node

    # insert node from right
    def insert(self, node):
        pre_node, nxt_node = self.right.prev, self.right
        pre_node.next = nxt_node.prev = node
        node.next, node.prev = nxt_node, pre_node

    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def set(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from the list and delete the LRU from the hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


if __name__ == "__main__":

    our_cache = LRU_Cache(5)
    print(our_cache.get(7))      # returns -1 

    our_cache.set(1, 1);
    our_cache.set(2, 2);
    our_cache.set(3, 3);
    our_cache.set(4, 4);


    print(our_cache.get(1))      # returns 1
    print(our_cache.get(2))      # returns 2
    print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5) 
    our_cache.set(6, 6)

    print(our_cache.get(3))      # returns -1 because the cache reached its capacity and 3 was the least recently used entry
