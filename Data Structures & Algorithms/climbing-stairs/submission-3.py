class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 2
        last = 2
        while last < n :
            one += two
            two += one
            last += 2
        if last == n : return two
        return one