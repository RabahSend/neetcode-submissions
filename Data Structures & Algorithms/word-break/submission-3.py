class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dfs(i, j):
            if j >= len(s):
                return True

            if i >= len(s):
                return False

            if (i,j) in memo:
                return memo[(i,j)]

            result = False

            if s[j:i+1] in wordDict:
                result = dfs(i + 1, i + 1)

            if not result:
                result = dfs(i+1, j)

            memo[(i,j)] = result
            return memo[(i,j)]
            

        return dfs(0,0)

        