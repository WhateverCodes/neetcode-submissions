class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gpos = len(g)-1
        spos = len(s)-1
        ans = 0
        while gpos >= 0 and spos >= 0 :
            if g[gpos] <= s[spos] :
                ans += 1
                gpos -= 1
                spos -= 1
            else :
                gpos -= 1
        return ans