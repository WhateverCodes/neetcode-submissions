class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1] : return True
        start = 0
        end = len(s)-1
        while start < end :
            if s[start] == s[end] :
                start += 1
                end -= 1
            else :
                opt1 = s[start+1:end+1]
                opt2 = s[start:end]
                return opt1 == opt1[::-1] or opt2 == opt2[::-1]
        return True