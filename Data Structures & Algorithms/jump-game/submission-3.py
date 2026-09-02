class Solution:
    def canJump(self, nums: List[int]) -> bool:
        poss = [-1]*len(nums)
        poss[0] = 1
        for i in range(0, len(nums)) :
            if poss[i] == 1 :
                for j in range(i + 1, min(len(nums), i + nums[i] + 1)) : poss[j] = 1
        return poss[-1] == 1