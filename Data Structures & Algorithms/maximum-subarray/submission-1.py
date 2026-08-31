class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        t = 0
        for num in nums:
            if t < 0:
                t = 0
            t += num
            ans = max(ans, t)
        return ans