class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for n in nums :
            if n > 0 : pos.append(n)
            else : neg.append(n)
        for p, n in enumerate(pos) :
            nums[p*2] = n
        for p, n in enumerate(neg) :
            nums[p*2+1] = n
        return nums