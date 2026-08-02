class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        lett = set(s)
        odd = 0
        for ch in lett :
            if s.count(ch)%2 == 1 : odd += 1
        return odd < 2