class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = {0: 1}
        count = 0
        res = 0

        for i in range(len(nums)):
            count += nums[i]
            remain = count % k

            res += prefix_sum.get(remain, 0)
            prefix_sum[remain] = prefix_sum.get(remain, 0) + 1

        return res