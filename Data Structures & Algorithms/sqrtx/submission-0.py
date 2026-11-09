class Solution:
    def mySqrt(self, x: int) -> int:
        ans = 0
        while True :
            if ans*ans == x : return ans
            elif ans*ans > x : return ans-1
            ans += 1
        return ans