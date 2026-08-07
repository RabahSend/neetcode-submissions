class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}

        def dfs(coords):
            if (coords[0],coords[1]) in memo:
                return memo[(coords[0],coords[1])]

            result = 1
            neighbours = [[coords[0] - 1, coords[1]], [coords[0] + 1, coords[1]], [coords[0], coords[1] - 1], [coords[0], coords[1] + 1]]

            for neighbour in neighbours:
                if (0 <= neighbour[0] < len(matrix)) and (0 <= neighbour[1] < len(matrix[coords[0]])):
                    if matrix[neighbour[0]][neighbour[1]] > matrix[coords[0]][coords[1]]:
                        result = max(result, 1 + dfs(neighbour))

            memo[(coords[0],coords[1])] = result
            return memo[(coords[0],coords[1])]

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                dfs([i, j])

        return max(memo.values())