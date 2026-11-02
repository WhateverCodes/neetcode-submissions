class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        ans = nums[0]
        l = len(nums)
        t = 0
        for i in range(l) :
            t += nums[i]
            ans = max(ans, t)
        t = 0
        for i in range(l-1, -1, -1) :
            t += nums[i]
            ans = max(ans, t)
        return ans