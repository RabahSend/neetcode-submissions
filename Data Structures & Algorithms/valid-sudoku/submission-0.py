class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                elem = board[i][j]

                if (elem == "."):
                    continue

                pos = (i // 3) * 3 + j // 3

                if (elem in rows[i]) or (elem in cols[j]) or (elem in squares[pos]):
                    return False

                rows[i].add(elem)
                cols[j].add(elem)
                squares[pos].add(elem)

        return True