class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        memo = {}

        def dfs(start):
            if start == len(s):
                return True

            if start in memo:
                return memo[start]

            for end in range(start, len(s)):
                if s[start:end+1] in words:
                    if dfs(end+1):
                        memo[start] = True
                        return memo[start]

            memo[start] = False
            return memo[start]

        return dfs(0)