class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1
        r = s[::-1]
        l = len(s)
        for p in range(l) :
            n = r.index(s[p])
            ans = max(ans, l-p-n-2)
        return ans