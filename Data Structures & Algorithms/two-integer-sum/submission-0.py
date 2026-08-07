class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}

        for i, n in enumerate(nums):
            if n not in m:
                m[n] = i
                
        for i, n in enumerate(nums):
            complement = target - n

            if complement in m and i != m[complement]:
                j = m[complement]
                return [min(i,j), max(i,j)]