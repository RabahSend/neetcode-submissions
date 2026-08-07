class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(t):
            if t[0] >= len(matrix) or t[1] >= len(matrix[t[0]]):
                return 0

            if t in memo:
                return memo[t]

            max_dist = 1

            for direction in directions:
                neighbour = (t[0] + direction[0], t[1] + direction[1])
                if (0 <= neighbour[0] < len(matrix)) and (0 <= neighbour[1] < len(matrix[neighbour[0]])):
                    if matrix[neighbour[0]][neighbour[1]] > matrix[t[0]][t[1]]:
                        max_dist = max(max_dist, 1 + dfs(neighbour))

            memo[t] = max_dist
            return memo[t]

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                dfs((i,j))

        return max(memo.values())