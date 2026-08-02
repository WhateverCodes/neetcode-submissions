class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = len(nums)
        e = 0
        o = l-1
        while e < o :
            while e < l and nums[e]%2 == 0 : e += 1
            while o > 0 and nums[o]%2 == 1 : o -= 1
            if e < l and o > 0 and e < o :
                t = nums[e]
                nums[e] = nums[o]
                nums[o] = t
                e += 1
                o -= 1
        return nums