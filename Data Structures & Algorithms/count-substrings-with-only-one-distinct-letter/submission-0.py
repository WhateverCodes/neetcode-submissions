class Solution:
    def countLetters(self, s: str) -> int:
        ans = 0
        t = 0
        last = s[0]
        for i in range(len(s)) :
            if s[i] == last :
                t += 1
            else :
                t = 1
            ans += t
            last = s[i]
        return ans