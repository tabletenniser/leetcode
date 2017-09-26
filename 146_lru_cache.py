'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''
class DoubleLLNode(object):
    key = None
    p = None
    n= None

    def __init__(self, key, p, n):
        self.key = key
        self.p = p
        self.n = n

class LRUCache(object):
    capacity = None
    first, last = None, None
    hash_table = None
    cur_size = None

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.hash_table = dict()
        self.cur_size = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.hash_table:
            return -1
        node = self.hash_table[key][1]
        # Update last node
        if self.last == node and self.cur_size > 1:
            self.last = node.p
        # Remove from current position
        if node != self.first:
            if node.p:
                node.p.n = node.n
            if node.n:
                node.n.p = node.p
            # Add it to the beginning of the doubly LL.
            assert(self.first)
            node.n = self.first
            node.p = None
            self.first.p = node
            self.first = node

        print "GET: (", key, self.hash_table[key][0], ")", self.hash_table.keys(), self.first.key, self.last.key, self.last.p.key
        return self.hash_table[key][0]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity == 0:
            return

        node = None
        if key in self.hash_table:
            node = self.hash_table[key][1]
            if node == self.first:
                self.hash_table[key] = (value, node)
                return
            # Update last node
            if self.last == node and self.cur_size > 1:
                self.last = node.p
            # Remove from current position
            if node.p:
                node.p.n = node.n
            if node.n:
                node.n.p = node.p
        else:
            node = DoubleLLNode(key, None, self.first)
            # Remove least-used element if we are at capacity.
            if self.cur_size == self.capacity:
                del self.hash_table[self.last.key]
                self.last = self.last.p
                self.last.n = None
                self.cur_size -= 1

            if self.cur_size == 0:
                self.last = node
            self.cur_size += 1
        # Update self.first
        node.n = self.first
        node.p = None
        if self.first:
            self.first.p = node
        self.first = node

        self.hash_table[key] = (value, node)
        print "PUT: (", key, value, ")", self.hash_table.keys(), self.first.key, self.last.key
        return


# Your LRUCache object will be instantiated and called as such:
cache = LRUCache(3)
cache.put(1, 1);
cache.put(2, 2);
cache.put(3, 3);
cache.put(4, 4);
print cache.get(4);       # returns 3
print cache.get(3);       # returns 3
print cache.get(2);       # returns 3
print cache.get(1);       # returns 3
cache.put(5, 5);
print cache.get(1);       # returns 3
print cache.get(2);       # returns 3
print cache.get(3);       # returns 3
print cache.get(4);       # returns 3
print cache.get(5);       # returns 3
