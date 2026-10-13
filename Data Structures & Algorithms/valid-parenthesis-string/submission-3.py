class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {}

        def dfs(i, parenthesis):
            if (i, parenthesis) in memo:
                return memo[(i, parenthesis)]

            if i >= len(s):
                if parenthesis == 0:
                    return True

                return False

            if parenthesis < 0:
                return False

            if s[i] == '(':
                memo[(i, parenthesis)] = dfs(i + 1, parenthesis + 1)
            elif s[i] == ')':
                memo[(i, parenthesis)] = dfs(i + 1, parenthesis - 1)
            elif s[i] == '*':
                memo[(i, parenthesis)] = dfs(i + 1, parenthesis + 1) or dfs(i + 1, parenthesis - 1) or dfs(i + 1, parenthesis)

            return memo[(i, parenthesis)]

        return dfs(0, 0)