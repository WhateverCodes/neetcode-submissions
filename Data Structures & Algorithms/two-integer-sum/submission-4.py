class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed_nums = sorted([(num, i) for i, num in enumerate(nums)])
        l = 0
        r = len(indexed_nums)-1
        while l < r :
            t = indexed_nums[l][0] + indexed_nums[r][0]
            if t == target :
                res = [indexed_nums[l][1], indexed_nums[r][1]]
                res.sort()
                return res
            if t < target : l += 1
            else : r -= 1
        return [-1, -1]