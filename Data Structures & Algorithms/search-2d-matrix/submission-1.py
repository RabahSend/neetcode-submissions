class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        right_m = len(matrix) - 1
        left_m = 0

        while left_m <= right_m:
            mid_m = (right_m + left_m) // 2

            if matrix[mid_m][0] == target:
                return True
            elif matrix[mid_m][0] < target:
                left_m = mid_m + 1
            else:
                right_m = mid_m - 1

            right_n = len(matrix[0]) - 1
            left_n = 0
            while left_n <= right_n:
                mid_n = (right_n + left_n) // 2
                if matrix[mid_m][mid_n] == target:
                    return True
                elif matrix[mid_m][mid_n] < target:
                    left_n = mid_n + 1
                else:
                    right_n = mid_n - 1

        return False