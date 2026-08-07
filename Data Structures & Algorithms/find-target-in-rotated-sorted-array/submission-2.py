class Solution:
    def search(self, nums: List[int], target: int) -> int:
        segment_break = 0

        for i in range(len(nums)):
            if i < len(nums) - 1 and nums[i] > nums[i+1]:
                segment_break = i + 1

        left = 0
        right = segment_break

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        left = segment_break
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1