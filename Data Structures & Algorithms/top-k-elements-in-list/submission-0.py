class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        buckets = [[] for _ in range(len(nums) + 1)]

        for i in range(0, len(nums)):
            count[nums[i]] = count.get(nums[i],0) + 1

        for i,n in count.items():
            buckets[n].append(i)

        res = []

        for count in range(len(buckets) - 1, 0, -1):
            for num in buckets[count]:
                res.append(num)

                if len(res) == k:
                    return res
