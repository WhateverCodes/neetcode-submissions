class Solution:
    def isHappy(self, n: int) -> bool:
        happ = []
        while n != 1 :
            t = 0
            for ch in str(n) : t += int(ch)**2
            n = t
            if n in happ : return False
            happ.append(n)
        return True