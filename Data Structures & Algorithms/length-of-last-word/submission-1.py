class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        pos = len(s)-1
        while s[pos] == ' ' :
            pos -= 1
        start = pos
        while pos >= 0 and s[pos] != ' ' :
            pos -= 1
        end = pos
        return start-end