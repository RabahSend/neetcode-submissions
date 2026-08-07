class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def backtrack(number_open, number_close):
            if len(path) == n*2:
                res.append("".join(path))
                return


            if number_open < n:
                path.append("(")
                backtrack(number_open+1, number_close)
                path.pop()

            if number_close < number_open:
                path.append(")")
                backtrack(number_open, number_close+1)
                path.pop()

        backtrack(0, 0)
        
        return res

