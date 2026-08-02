class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        pos = len(s)-1
        while pos > 0 and s[pos] == ' ' : pos -= 1
        ans = 0
        while pos >= 0 and s[pos] != ' ' : 
            pos -= 1
            ans += 1
        return ans