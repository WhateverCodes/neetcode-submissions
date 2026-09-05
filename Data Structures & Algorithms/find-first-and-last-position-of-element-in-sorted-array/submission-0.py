class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums : return [-1, -1]
        ans = [nums.index(target)]
        nums = nums[::-1]
        ans.append(len(nums)-1-nums.index(target))
        return ans