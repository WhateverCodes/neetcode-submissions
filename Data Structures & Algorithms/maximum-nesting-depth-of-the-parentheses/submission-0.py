class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        t = 0
        for ch in s :
            if ch == '(' :
                t += 1
                ans = max(ans, t)
            elif ch == ')' : t -= 1
        return ans