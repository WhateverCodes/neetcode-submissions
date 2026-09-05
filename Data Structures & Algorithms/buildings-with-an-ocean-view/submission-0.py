class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ans = []
        n = 0
        for i in range(len(heights)-1, -1, -1) :
            if heights[i] > n :
                ans.append(i)
                n = heights[i]
        ans.sort()
        return ans