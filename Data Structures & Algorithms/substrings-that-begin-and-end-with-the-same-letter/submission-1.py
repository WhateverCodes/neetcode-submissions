class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = [0]*26
        ans = 0
        for ch in s :
            p = ord(ch) - ord('a')
            count[p] += 1
            ans += count[p]
        return ans