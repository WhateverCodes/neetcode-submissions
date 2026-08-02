class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ""
        for ch in s:
            if ch.isalnum():
                t += ch.lower()
        return t == t[::-1]