class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        diff = set(nums)
        for n in diff :
            if nums.count(n)%2 != 0 : return False
        return True