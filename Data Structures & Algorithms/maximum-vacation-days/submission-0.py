class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        n = len(flights)
        dp = [-10000] * n
        dp[0] = 0
        for week in range(len(days[0])):
            nxt = [-10000] * n
            for src in range(n):
                if dp[src] < 0:
                    continue
                for dst in range(n):
                    if src == dst or flights[src][dst]:
                        nxt[dst] = max(nxt[dst], dp[src] + days[dst][week])
            dp = nxt
        return max(dp)
