class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        m = set()

        for i in range(0, len(nums)):
            if nums[i] in m:
                return True
            m.add(nums[i])

        return False