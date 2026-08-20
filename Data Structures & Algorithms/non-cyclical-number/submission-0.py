class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        
        def dfs(i):
            if i == 1:
                return True

            if i in visited:
                return False

            visited.add(i)
            
            count = 0

            while i > 0:
                digit = i % 10
                count += digit * digit
                i = i // 10

            return dfs(count)

        return dfs(n)