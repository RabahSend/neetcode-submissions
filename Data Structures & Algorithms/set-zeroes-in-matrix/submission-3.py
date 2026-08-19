class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])
        zeroRows = set()
        zeroCols = set()

        for i in range(bottom):
            for j in range(right):
                if matrix[i][j] == 0:
                        zeroRows.add(i)
                        zeroCols.add(j)


        for x in zeroRows:
            for i in range(right):
                matrix[x][i] = 0

        for y in zeroCols:
            for i in range(bottom):
                matrix[i][y] = 0