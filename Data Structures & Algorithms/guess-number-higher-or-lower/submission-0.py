# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        while True :
            t = (low+high)//2
            res = guess(t)
            if res > 0 : low = t+1
            elif res < 0 : high = t-1
            else : return t