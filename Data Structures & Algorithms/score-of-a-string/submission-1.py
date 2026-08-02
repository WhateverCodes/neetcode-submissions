class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        l = len(s)
        for i in range(l-1) :
            total += abs(ord(s[i]) - ord(s[i+1]))
        return total