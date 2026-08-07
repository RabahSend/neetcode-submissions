class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = set()
        res = []
        path = []

        def backtrack():
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for i in range(len(nums)):
                if i in used:
                    continue

                used.add(i)
                path.append(nums[i])

                backtrack()

                path.pop()
                used.remove(i)

        backtrack()
        return res