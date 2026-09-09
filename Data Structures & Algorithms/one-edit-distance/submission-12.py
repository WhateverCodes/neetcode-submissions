class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == t : return False
        ls = len(s)
        lt = len(t)
        if abs(ls - lt) > 1 : return False
        if ls > lt:
            s, t = t, s
            ls, lt = lt, ls
        pos = 0
        while pos < ls and s[pos] == t[pos] : pos += 1
        if ls == lt:
            pos += 1
            return s[pos:] == t[pos:]
        return s[pos:] == t[pos + 1:]