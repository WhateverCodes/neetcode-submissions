class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans = len(s)
        lett = 'abcdefghijklmnopqrstuvwxyz'
        for ch in lett :
            if s.count(ch) == 1 :
                ans = min(ans, s.index(ch))
        if ans == len(s) : return -1
        return ans