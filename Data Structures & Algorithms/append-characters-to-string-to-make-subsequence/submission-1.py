class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        m = len(t)
        pos = 0
        for ch in s :
            if t[pos] == ch :
                pos += 1
                if pos == m : return 0
        return m-pos