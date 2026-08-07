class MedianFinder:

    def __init__(self):
        self.heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap, num)

    def findMedian(self) -> float:
        if len(self.heap) == 1:
            return self.heap[0]

        mid = len(self.heap) / 2
        false_heap = self.heap[:]

        if mid % 1 == 0:
            while len(false_heap) > mid + 1 and len(false_heap) > 2:
                 heapq.heappop(false_heap)
            
            return (heapq.heappop(false_heap) + heapq.heappop(false_heap)) / 2
        else:
            while len(false_heap) > mid + 1:
                heapq.heappop(false_heap)

            return heapq.heappop(false_heap)

        

            
        