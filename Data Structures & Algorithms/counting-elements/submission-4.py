class Solution:
    def countElements(self, arr: List[int]) -> int:
        hashs = [0]*1001
        for n in arr :
            hashs[n] += 1
        ans = 0
        for i in range(1000) :
            if hashs[i] > 0 and hashs[i+1] > 0 : ans += hashs[i]
        return ans