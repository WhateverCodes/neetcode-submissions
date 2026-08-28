class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        c = 0
        ans = 0
        for w in weight :
            if c+w > 5000 : return ans
            ans += 1
            c += w
        return ans