class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        number = 0
        adj = [[] for _ in range(n)]
        visited = set()

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node):
            if node in visited:
                return False

            visited.add(node)

            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)

            return True

        
        for i in range(n):
            number += dfs(i)

        return number