class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = deque()
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache[key]

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.queue.remove(key)
        self.cache[key] = value
        self.queue.append(key)

        if len(self.cache) > self.capacity:
            keyToRemove = self.queue.popleft()
            self.cache.pop(keyToRemove)
