class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        m = min(nums)
        t = 0
        while m > 0 :
            t += m%10
            m //= 10
        return 1-t%2