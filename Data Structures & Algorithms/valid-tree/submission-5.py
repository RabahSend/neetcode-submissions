class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adj = [[] for _ in range(n)]

        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        def dfs(node, last):
            if node in visited:
                return False

            visited.add(node)

            for nei in adj[node]:
                if last != nei and not dfs(nei, node):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n

