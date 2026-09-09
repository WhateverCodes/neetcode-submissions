class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        t = 0
        for n in set(nums) : t += 2*n
        return t-sum(nums)