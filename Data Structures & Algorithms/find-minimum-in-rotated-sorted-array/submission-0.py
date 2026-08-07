class Solution:
    def findMin(self, nums: List[int]) -> int:
        r = len(nums) - 1
        l = 0
        min_elem = nums[0]

        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] < min_elem:
                min_elem = nums[mid]
                r = mid - 1
            else:
                l = mid + 1

        return min_elem