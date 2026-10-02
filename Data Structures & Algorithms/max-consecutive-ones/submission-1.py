class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        t = 0
        p = 0
        while p < len(nums) :
            if nums[p] == 0 :
                ans = max(ans, t)
                t = 0
            else :
                t += 1
            p += 1
        ans = max(ans, t)
        return ans