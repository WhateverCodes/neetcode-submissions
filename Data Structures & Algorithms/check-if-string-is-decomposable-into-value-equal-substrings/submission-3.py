class Solution:
    def isDecomposable(self, s: str) -> bool:
        two = 0
        p = 0
        l = len(s)
        while p < l :
            if p+1 == l : return False
            if p+2 == l :
                if s[p] == s[p+1] :
                    two += 1
                    p += 2
                else : return False
            elif s[p] == s[p+1] and s[p] != s[p+2] :
                two += 1
                p += 2
            elif s[p] == s[p+1] and s[p] == s[p+2] :
                p += 3
            else : return False
        return two == 1