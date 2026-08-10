class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(len(edges) + 1)]
        visited = set()

        def dfs(node, prev):
            if node in visited:
                return True

            visited.add(node)

            for nei in adj[node]:
                if prev != nei and dfs(nei, node):
                    return True
            
            return False

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

            if dfs(a, -1):
                return [a, b]

            visited.clear()

        return []