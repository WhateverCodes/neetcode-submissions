class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        steps = [0, 0]
        for i in range(2, len(cost) + 1) :
            t = min(steps[i-1]+cost[i-1], steps[i-2]+cost[i-2])
            steps.append(t)
        return steps[-1]