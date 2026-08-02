class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        diff = set(nums)
        ans = 0
        for n in diff :
            t = nums.count(n)
            ans += (t * (t-1))//2
        return ans