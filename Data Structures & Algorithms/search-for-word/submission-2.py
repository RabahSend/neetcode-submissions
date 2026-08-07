class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        cols = len(board)
        rows = len(board[0])
        visited = set()

        def backtrack(x, y, index):
            if index == len(word):
                return True

            if x < 0 or x >= cols or y < 0 or y >= rows:
                return False

            if board[x][y] != word[index] or (x,y) in visited:
                return False

            visited.add((x,y))

            result = (
                backtrack(x+1, y, index+1) or
                backtrack(x, y+1, index+1) or
                backtrack(x-1, y, index+1) or
                backtrack(x, y-1, index+1)
            )

            visited.remove((x,y))

            return result

        for x in range(cols):
            for y in range(rows):
                if backtrack(x,y,0):
                    return True

        return False
