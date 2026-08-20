class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        x = max(set(nums), key = nums.count)
        total = nums.count(x)
        left = 0
        for i in range(len(nums) - 1):
            if nums[i] == x:
                left += 1
            right = total - left
            if left * 2 > i + 1 and right * 2 > len(nums) - i - 1:
                return i
        return -1