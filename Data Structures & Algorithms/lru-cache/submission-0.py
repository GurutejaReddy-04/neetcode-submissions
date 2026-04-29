class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}

        self.left = Node(0, 0)   # LRU
        self.right = Node(0, 0)  # MRU

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        node.prev = prev

        node.next = nxt
        nxt.prev = node

    def get(self, key):
        if key not in self.cache:
            return -1

        self.remove(self.cache[key])
        self.insert(self.cache[key])

        return self.cache[key].val

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
