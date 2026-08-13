class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        pos = 0
        l = len(word)
        p = 0
        a = len(abbr)
        while p < a :
            if pos >= l : return False
            if abbr[p].isdigit() :
                ad = 0
                while p < a and abbr[p].isdigit() :
                    ad *= 10
                    ad += int(abbr[p])
                    if ad == 0 : return False
                    p += 1
                pos += ad
            elif word[pos] == abbr[p] :
                pos += 1
                p += 1
            else : return False
        return pos == l