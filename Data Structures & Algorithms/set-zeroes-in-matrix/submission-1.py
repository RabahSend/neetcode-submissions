class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])
        areZeros = []

        for i in range(bottom):
            for j in range(right):
                if matrix[i][j] == 0:
                    areZeros.append((i, j))


        for x, y in areZeros:
            for i in range(bottom):
                matrix[i][y] = 0
            
            for i in range(right):
                matrix[x][i] = 0