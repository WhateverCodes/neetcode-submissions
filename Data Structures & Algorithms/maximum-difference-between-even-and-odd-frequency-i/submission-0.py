class Solution:
    def maxDifference(self, s: str) -> int:
        lett = set(s)
        odd = 0
        even = float('inf')
        for l in lett :
            t = s.count(l)
            if t%2 == 0 : even = min(even, t)
            else : odd = max(odd, t)
        return odd-even
