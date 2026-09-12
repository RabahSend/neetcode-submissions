class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        neighbors = [[] for _ in range(numCourses)]
        nodes = 0

        for u, v in prerequisites:
            indegree[u] += 1
            neighbors[v].append(u)

        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                nodes += 1

        while queue:
            curr = queue.popleft()

            for nei in neighbors[curr]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)
                    nodes += 1

        return nodes == numCourses