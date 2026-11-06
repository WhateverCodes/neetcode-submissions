class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        f = 0
        l = len(s)-1
        while f != l and f < l:
            if s[f] != s[l] : return False
            f += 1
            l -= 1
        return True