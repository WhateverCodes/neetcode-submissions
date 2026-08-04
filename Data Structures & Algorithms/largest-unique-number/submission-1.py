class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        for i in range(1000, -1, -1) : 
            if nums.count(i) == 1 : return i
        return -1