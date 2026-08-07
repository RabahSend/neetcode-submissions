class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def backtracking(start):
            if start == len(s):
                res.append(path.copy())
                return

            for i in range(start, len(s)):
                substring = s[start:i + 1]

                if substring == substring[::-1]:
                    path.append(substring)
                    backtracking(i + 1)
                    path.pop()  

        backtracking(0)

        return res