class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words) : return False
        ctw = {}
        for i, (c, w) in enumerate(zip(pattern, words)) :
            if c in ctw :
                if words[ctw[c]] != w : return False
            else :
                for k in ctw :
                    if words[ctw[k]] == w : return False
                ctw[c] = i
        return True