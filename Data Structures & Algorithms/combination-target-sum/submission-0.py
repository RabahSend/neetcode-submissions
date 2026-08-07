class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtracking(start):
            if sum(path) == target:
                res.append(path.copy())

            for i in range(start, len(nums)):
                path.append(nums[i])

                if sum(path) <= target:
                    backtracking(i)

                path.pop()

        backtracking(0)

        return res

