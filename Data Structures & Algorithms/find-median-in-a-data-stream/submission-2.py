import heapq

class MedianFinder:

    def __init__(self):
        self.lowerHeap = []  
        self.higherHeap = [] 

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lowerHeap, -num)

        if self.higherHeap and -self.lowerHeap[0] > self.higherHeap[0]:
            value = -heapq.heappop(self.lowerHeap)
            heapq.heappush(self.higherHeap, value)

        if len(self.lowerHeap) > len(self.higherHeap) + 1:
            value = -heapq.heappop(self.lowerHeap)
            heapq.heappush(self.higherHeap, value)

        if len(self.higherHeap) > len(self.lowerHeap) + 1:
            value = heapq.heappop(self.higherHeap)
            heapq.heappush(self.lowerHeap, -value)

    def findMedian(self) -> float:
        if len(self.lowerHeap) > len(self.higherHeap):
            return -self.lowerHeap[0]

        if len(self.higherHeap) > len(self.lowerHeap):
            return self.higherHeap[0]

        return (-self.lowerHeap[0] + self.higherHeap[0]) / 2