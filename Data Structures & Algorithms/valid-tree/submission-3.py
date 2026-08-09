class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        if not edges:
            return True

        visited = []
        preMap = {}
        finished = 0

        for src, dst in edges:
            if src not in preMap:
                preMap[src] = []
            if dst not in preMap:
                preMap[dst] = []

            preMap[src].append(dst)
            preMap[dst].append(src)

        def dfs(node, last):
            nonlocal finished

            if node in visited:
                return False

            visited.append(node)

            for nei in preMap[node]:
                if last != nei and not dfs(nei, node):
                    return False

            finished += 1
            return True

        return dfs(edges[0][0], -1) and finished == n

