class Solution:
    def isArmstrong(self, n: int) -> bool:
        power = len(str(n))
        t = 0
        for ch in str(n) : t += int(ch)**power
        return t == n