class Solution:
    def maxScore(self, s: str) -> int:
        ones = s.count('1')
        ans = ones
        if s[0] == '1' : ans -= 1
        else : ans += 1
        t = ans
        for i in range(1, len(s)-1) :
            if s[i] == '0' :
                t += 1
                ans = max(ans, t)
            else : t -= 1
        return ans