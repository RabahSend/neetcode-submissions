class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        movements= [[1, 0], [-1, 0], [0, 1], [0, -1]]
        seen = set()

        def backtracking(i, j, letter):
            if letter >= len(word):
                return True

            if (i >= len(board) or i < 0) or (j >= len(board[0]) or j < 0):
                return False

            print(i, j, letter)

            if board[i][j] == word[letter]:
                seen.add((i, j))
                for mov in movements:
                    if (i + mov[0], j + mov[1]) not in seen and backtracking(i + mov[0], j + mov[1], letter + 1):
                        return True

                seen.remove((i, j))

            return False


        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtracking(i, j, 0):
                    return True

        return False