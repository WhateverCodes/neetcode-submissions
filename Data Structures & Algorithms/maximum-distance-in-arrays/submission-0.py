class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mini = arrays[0][0]
        maxi = arrays[0][-1]
        ans = 0
        for i in range(1, len(arrays)):
            cmin = arrays[i][0]
            cmax = arrays[i][-1]
            ans = max(ans, cmax - mini, maxi - cmin)
            mini = min(mini, cmin)
            maxi = max(maxi, cmax)
        return ans