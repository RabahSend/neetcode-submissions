class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.right, self.left = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node):
        end = self.right.prev
        end.next, node.next = node, self.right
        self.right.prev = node
        node.prev = end

    def remove(self, node):
        prv, nxt = node.prev, node.next
        nxt.prev, prv.next = prv, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            keyToRemove = self.left.next.key
            self.remove(self.cache[self.left.next.key])
            self.cache.pop(keyToRemove)
