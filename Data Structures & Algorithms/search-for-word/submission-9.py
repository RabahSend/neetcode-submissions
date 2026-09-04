class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()
        movs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def dfs(i, j, letter):
            if (i, j) in seen:
                return False

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False

            if board[i][j] != word[letter]:
                return False

            if letter == len(word) - 1:
                return True

            seen.add((i,j))
            
            for mov in movs:
                if (i + mov[0], j + mov[1]) not in seen and dfs(i + mov[0], j + mov[1], letter + 1):
                    return True

            seen.remove((i, j))

            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True

        return False