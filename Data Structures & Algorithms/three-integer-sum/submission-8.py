class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                res = nums[right] + nums[left] + nums[i]

                if res == 0:
                    ans.append([nums[right], nums[left], nums[i]])

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    right -= 1
                    left += 1

                elif res < 0:
                    left += 1
                else:
                    right -= 1


        return ans
