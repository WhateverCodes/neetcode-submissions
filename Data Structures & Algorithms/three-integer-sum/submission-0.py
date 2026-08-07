class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        l = len(nums)
        pos = 0
        while pos < l-2 :
            if pos > 0 and nums[pos] == nums[pos-1] : pos += 1
            else :
                left  = pos+1
                right = l-1
                while left < right :
                    s = nums[pos]+nums[left]+nums[right]
                    if s == 0 :
                        ans.append([nums[pos], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1] : left += 1
                        while right > left and nums[right] == nums[right+1] : right -= 1
                    elif s > 0 : right -= 1
                    else : left += 1
                pos += 1
        return ans