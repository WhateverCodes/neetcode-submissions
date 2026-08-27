class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        prv = 1
        for i in range(n) :
            res[i] = prv
            prv *= nums[i]
        last = 1
        for i in range(n-1, -1, -1) :
            res[i] *= last
            last *= nums[i]
        return res