class TimeMap:

    def __init__(self):
        self.storage = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage:
            self.storage[key] = []

        self.storage[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.storage:
            right, left = len(self.storage[key]) - 1, 0
            biggest_timestamp_value = ""
            while left <= right:
                mid = (right + left) // 2
                if timestamp >= self.storage[key][mid][0]:
                    left = mid + 1
                    biggest_timestamp_value = self.storage[key][mid][1]
                else:
                    right = mid - 1

            return biggest_timestamp_value

        return ""

