class Solution:
    def meetRequirement(self, n: int, lights: List[List[int]], requirement: List[int]) -> int:
        t = [0] * n
        for light in lights :
            b = light[0]
            d = light[1]
            l = max(0, b-d)
            u = min(n-1, b+d)
            for i in range(l, u+1) : t[i] += 1
        ans = 0
        for i in range(n) :
            if t[i] >= requirement[i] : ans += 1
        return ans