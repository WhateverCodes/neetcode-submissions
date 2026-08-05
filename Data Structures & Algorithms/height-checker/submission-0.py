class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        copy = sorted(heights)
        ans = 0
        for i in range(len(heights)) :
            if heights[i] != copy[i] : ans += 1
        return ans