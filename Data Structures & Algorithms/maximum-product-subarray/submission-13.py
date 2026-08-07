class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        curMin = curMax = 1

        for num in nums:
            candidates = (
                curMax * num,
                curMin * num,
                num
            )

            curMax = max(candidates)
            curMin = min(candidates)
            result = max(result,curMax)

        return result

            