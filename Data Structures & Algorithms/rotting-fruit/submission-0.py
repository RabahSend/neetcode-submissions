class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        queue = deque()
        minutes = 0
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        while queue and fresh > 0:
            num_fruits = len(queue)

            for _ in range(num_fruits):
                r, c = queue.popleft()

                for direction in directions:
                    n_r, n_c = r + direction[0], c + direction[1]

                    if (
                        n_r < 0 or n_c < 0 or n_r >= rows or n_c >= cols or grid[n_r][n_c] == 2 
                        or grid[n_r][n_c] == 0
                        ):
                        continue
                    
                    fresh -= 1
                    grid[n_r][n_c] = 2
                    queue.append((n_r, n_c))

            minutes += 1

        return minutes if fresh == 0 else -1
                
