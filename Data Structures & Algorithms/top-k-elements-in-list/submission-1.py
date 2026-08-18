class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = []
        res = []

        for value, count in counts.items():
            heapq.heappush(heap, (count, value))

            if len(heap) > k:
                heapq.heappop(heap)

        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res