class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        curr = 0
        for n in nums :
            if n == 1 :
                curr += 1
                ans = max(ans, curr)
            else : curr = 0
        return ans