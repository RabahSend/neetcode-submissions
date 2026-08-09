class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        number = 0
        adj = [[] for _ in range(n)]
        visited = set()

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node, prev):
            if node in visited:
                return 0

            visited.add(node)

            for nei in adj[node]:
                if prev != nei and dfs(nei, node):
                    continue

            return 1

        for node in adj:
            if not node:
                number += 1

        for edge in edges:
            for node in edge:
                number += dfs(node, -1)

        return number