class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ps = 0
        end = len(s)
        if ps == end: return True
        for ch in t :
            if ch == s[ps] :
                ps += 1
                if ps == end : return True
        return ps == end