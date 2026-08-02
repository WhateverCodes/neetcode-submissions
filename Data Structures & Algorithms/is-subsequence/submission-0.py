class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        spos = 0
        travel = 0
        while travel < len(t) and spos < len(s) :
            if s[spos] == t[travel] :
                spos += 1
            travel += 1
        if spos == len(s) :
            return True
        return False