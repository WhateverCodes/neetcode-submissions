class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1 : return nums[0]
        elif l == 2 : return max(nums)
        elif l == 3 : return max(nums[1], nums[0]+nums[2])
        t = [nums[0], max(nums[0], nums[1]), nums[0]+nums[2]]
        for i in range(3, l) :
            t.append(max(nums[i]+t[i-2], nums[i]+t[i-3]))
        return max(t[-1], t[-2])