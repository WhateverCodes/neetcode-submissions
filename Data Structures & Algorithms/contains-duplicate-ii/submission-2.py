class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = len(nums)
        s = 0
        e = min(k+1, l)
        while s < l :
            if len(set(nums[s:e])) != (e-s) : return True
            s += 1
            e = min(e+1, l)
        return False