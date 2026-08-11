class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = len(nums)
        ans = float('inf')
        s = 0
        e = k-1
        while e < l :
            t = nums[e]-nums[s]
            ans = min(ans, t)
            s += 1
            e += 1
        return ans