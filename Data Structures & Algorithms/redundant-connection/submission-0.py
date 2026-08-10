class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(len(edges) + 1)]

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        cycle_nodes = set()
        visited = set()

        def dfs(node, parent):
            visited.add(node)

            for nei in adj[node]:
                if nei == parent:
                    continue

                if nei in visited:
                    cycle_nodes.add(nei)
                    cycle_nodes.add(node)
                    return nei

                cycle_start = dfs(nei, node)

                if cycle_start != -1:
                    cycle_nodes.add(node)

                    if node == cycle_start:
                        return -1

                    return cycle_start

            return -1

        dfs(1, -1)

        for a, b in reversed(edges):
            if a in cycle_nodes and b in cycle_nodes:
                return [a, b]