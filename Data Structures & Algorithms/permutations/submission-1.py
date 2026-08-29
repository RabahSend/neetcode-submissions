class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        used = set()
        res = []

        def backtracking():
            if len(path) == len(nums) and path not in res:
                res.append(path.copy())
                return

            for i in range(len(nums)):
                if i in used:
                    continue
                
                path.append(nums[i])
                used.add(i)
                backtracking()
                path.pop()
                used.remove(i)

        backtracking()
        return res