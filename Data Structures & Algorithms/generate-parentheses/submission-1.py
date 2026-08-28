class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def backtracking(number_opened, number_closed):
            if len(path) == n*2:
                res.append(''.join(path))

            if number_opened < n:
                path.append('(')
                backtracking(number_opened + 1, number_closed)
                path.pop()

            if number_closed < number_opened:
                path.append(')')
                backtracking(number_opened, number_closed + 1)
                path.pop()

        backtracking(0, 0)

        return res

