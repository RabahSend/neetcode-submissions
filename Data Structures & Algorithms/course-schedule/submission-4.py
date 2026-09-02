class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] *numCourses
        adj = [[] for _ in range(numCourses)]
        queue = deque()
        finished = 0

        for u, v in prerequisites:
            indegree[v] += 1
            adj[u].append(v)

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            elem = queue.popleft()
            finished += 1

            for nei in adj[elem]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)

        return len(queue) == 0 and finished == numCourses
                    

