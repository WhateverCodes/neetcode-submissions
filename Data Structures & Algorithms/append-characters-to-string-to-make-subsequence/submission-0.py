class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        spos = 0
        travel = 0
        while travel < len(t) and spos < len(s) :
            if s[spos] == t[travel] :
                travel += 1
            spos += 1
        return len(t)-travel