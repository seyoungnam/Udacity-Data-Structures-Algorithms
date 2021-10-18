class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRU_Cache(object):
    def __init__(self, capacity=0):
        self.cap = 0 if type(capacity) is not int or capacity <= 0 else capacity
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

    def __str__(self):
        if self.left.next == self.right:
            return "This cache is empty."
        else:
            curr = self.left.next
            out_string = "Least Recent Unit" + " -> "
            while curr:
                out_string += str(curr.val) + " -> "
                curr = curr.next
                if curr == self.right:
                    break
            out_string += "Most Recent Unit"
            return out_string


if __name__ == "__main__":
    # test case 1
    cache1 = LRU_Cache(5)
    print(cache1.get(7))      # -1 

    cache1.set(1, 1);
    cache1.set(2, 2);
    cache1.set(3, 3);
    cache1.set(4, 4);

    print(cache1)             # Least Recent Unit -> 1 -> 2 -> 3 -> 4 -> Most Recent Unit

    print(cache1.get(1))      # 1
    print(cache1.get(2))      # 2
    print(cache1)             # Least Recent Unit -> 3 -> 4 -> 1 -> 2 -> Most Recent Unit
    print(cache1.get(9))      # -1 because 9 is not present in the cache

    cache1.set(5, 5) 
    cache1.set(6, 6)

    print(cache1)             # Least Recent Unit -> 4 -> 1 -> 2 -> 5 -> 6 -> Most Recent Unit
    print(cache1.get(3))      # returns -1 because 3 is not in the cache any longer

    # test case 2 - edge case
    cache2 = LRU_Cache(0)

    cache2.set(10, 10)
    cache2.set(20, 20)
    cache2.set(30, 30)
    print(cache2)             # This cache is empty. (because cache size sets to 0)
    print(cache2.get(20))     # -1
    print(cache2.get(30))     # -1

    # test case 3 - edge case
    cache3 = LRU_Cache('create cache')

    cache3.set(100, 100)
    cache3.set(200, 200)
    cache3.set(300, 300)
    print(cache3)             # This cache is empty. (because argument for the capacity parameter is given string - 'create cache', not a positive integer)

