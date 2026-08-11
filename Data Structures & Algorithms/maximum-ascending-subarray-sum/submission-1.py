class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = nums[0]
        t = ans
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                t = 0
            t += nums[i]
            ans = max(ans, t)
        return ans