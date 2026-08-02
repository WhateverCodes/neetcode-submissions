class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        l = len(nums)
        t = l//3
        ans = []
        a = nums[t]
        b = nums[(2*l)//3]
        if nums.count(a) > t : ans.append(a)
        if b != a and nums.count(b) > t : ans.append(b)
        return ans