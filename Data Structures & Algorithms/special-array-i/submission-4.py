class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        l = len(nums)
        if l == 1 : return True
        p = l-1
        while p > 0 :
            if (nums[p]+nums[p-1])%2 == 0 : return False
            p -= 1
        return True