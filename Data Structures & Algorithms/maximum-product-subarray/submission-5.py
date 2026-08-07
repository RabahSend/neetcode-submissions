class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = cur_max = cur_min = nums[0]

        for x in nums[1:]:
            candidates = (
                x,
                x * cur_min,
                x * cur_max
            )

            cur_max = max(candidates)
            cur_min = min(candidates)

            result = max(result, cur_max)

        return result

            