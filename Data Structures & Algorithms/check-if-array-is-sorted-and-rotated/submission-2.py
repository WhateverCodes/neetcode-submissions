class Solution:
    def check(self, nums: List[int]) -> bool:
        drops = 0
        l = len(nums)
        for i in range(l) :
            if nums[(i+l)%l] < nums[(i-1+l)%l] : drops += 1
        return drops < 2