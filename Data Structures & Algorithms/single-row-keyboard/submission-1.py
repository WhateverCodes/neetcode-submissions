class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        p = 0
        ans = 0
        for ch in word :
            t = keyboard.index(ch)
            ans += abs(t-p)
            p = t
        return ans