class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)

        for i in range(len(nums)):
            heapq.heappush(heap, nums[i])

        for i in range(len(nums) - k):
            heapq.heappop(heap)

        return(heap[0])