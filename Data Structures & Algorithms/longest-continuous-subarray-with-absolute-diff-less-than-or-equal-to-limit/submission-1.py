class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxi = 0

        for i in range(len(nums)):
            minimum = nums[i]
            maximum = nums[i]

            for j in range(i, len(nums)):
                minimum = min(minimum, nums[j])
                maximum = max(maximum, nums[j])

                if maximum - minimum <= limit:
                    maxi = max(maxi, j - i + 1)


        return maxi