class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []

        for i in range(len(points)):
            distance = math.sqrt(points[i][0]**2 + points[i][1]**2)

            if i < k:
                heapq.heappush(heap, [-distance, points[i]])
            else:
                if -distance > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, [-distance, points[i]])

        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return res