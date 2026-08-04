class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        hitMap = [0] * 1000
        for num in nums:
            hitMap[num] += 1
        for index in range(len(hitMap) - 1, 0, -1):
            if hitMap[index] == 1:
                return index
        return -1