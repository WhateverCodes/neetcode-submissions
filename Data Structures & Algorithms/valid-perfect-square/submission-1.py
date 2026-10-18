from math import sqrt
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        sqRoot = int(sqrt(num))
        return sqRoot * sqRoot == num