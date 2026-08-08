class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        queue = deque()
        ans = []
        
        for dest, src in prerequisites:
            indegree[dest] += 1
            adj[src].append(dest)

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            curr = queue.popleft()
            print(curr)
            ans.append(curr)

            for nei in adj[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        return ans if len(ans) == numCourses else []
            