class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elems = set()
        start = 0
        longest = 0

        for num in nums:
            elems.add(num)

        for i in range(len(nums)):
            length = 0
            if(nums[i] - 1 not in elems):
                start = nums[i]
                length += 1

            while(nums[i] + 1 in elems):
                length += 1
                nums[i] += 1
            
            longest = max(longest, length)

        return longest


            