class Solution:
    def lower_bound(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        index = len(nums)
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] >= target:
                end = mid - 1
                index = mid
            else:
                start = mid + 1
        return index

    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        first_index = self.lower_bound(nums, target)
        return first_index + len(nums) // 2 < len(nums) and nums[first_index + len(nums) // 2] == target