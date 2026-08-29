class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = res = 0
        multiply = 1

        for right in range(len(nums)):
            multiply *= nums[right]

            while left <= right and multiply >= k:
                multiply //= nums[left]
                left += 1
            
            res += right - left + 1

        return res