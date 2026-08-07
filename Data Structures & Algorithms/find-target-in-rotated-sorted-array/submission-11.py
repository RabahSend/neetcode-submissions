class Solution:
    def binarySearch(self, nums: List[int], target: int, left: int, right: int) -> int:
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1

    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[left]:
                left = mid
            else:
                right = mid

        left_value = self.binarySearch(nums, target, 0, right)
        right_value = self.binarySearch(nums, target, right + 1, len(nums) - 1)

        res = left_value if left_value != -1 else right_value

        return res

            