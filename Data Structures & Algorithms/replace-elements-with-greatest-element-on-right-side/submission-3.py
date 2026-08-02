class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = len(arr)
        ans = [0]*l
        g = -1
        for i in range(l-1, -1, -1) :
            ans[i] = g
            g = max(g, arr[i])
        return ans
