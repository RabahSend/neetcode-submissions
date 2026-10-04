class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]

            if i == len(days):
                return 0

            memo[i] = float("inf")
            j = i

            for d, c in zip([1, 7, 30], costs):
                while j < len(days) and days[j] < days[i] + d:
                    j += 1
                memo[i] = min(memo[i], dfs(j) + c)

            return memo[i]

        return dfs(0)