class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            queue = deque()
            grid[r][c] = "0"
            queue.append((r, c))
            
            while queue:
                row, col = queue.popleft()
                for rd, cd in directions:
                    n_r, n_c = row + rd, col + cd
                    if 0 > n_c or n_c >= cols or 0 > n_r or n_r >= rows or grid[n_r][n_c] == "0":
                        continue

                    queue.append((n_r, n_c))
                    grid[n_r][n_c] = "0"


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    bfs(i, j)
                    islands += 1

        return islands