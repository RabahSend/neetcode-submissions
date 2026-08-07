class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for elem in stones:
            heapq.heappush(heap, -elem)

        while len(heap) > 1:
            first_stone = -heapq.heappop(heap)
            second_stone = -heapq.heappop(heap)

            if first_stone != second_stone:
                mini, maxi = min(first_stone, second_stone), max(first_stone, second_stone)
                heapq.heappush(heap, -(maxi - mini))

        return 0 if len(heap) < 1 else -heap[0]