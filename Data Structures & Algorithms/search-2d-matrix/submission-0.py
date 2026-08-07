class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        print(len(matrix))

        for m in range(len(matrix)):
            right_n = len(matrix[0]) - 1
            left_n = 0

            while left_n <= right_n:
                mid_n = (right_n + left_n) // 2
                if matrix[m][mid_n] == target:
                    return True
                elif matrix[m][mid_n] < target:
                    left_n = mid_n + 1
                else:
                    right_n = mid_n - 1

        return False