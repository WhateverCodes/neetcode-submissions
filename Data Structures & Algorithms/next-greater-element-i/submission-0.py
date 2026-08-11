class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        l = len(nums2)
        for n in nums1 :
            if n in nums2 :
                pos = nums2.index(n)
                f = 0
                while pos < l :
                    if nums2[pos] > n :
                        f = 1
                        ans.append(nums2[pos])
                        break
                    pos += 1
                if f == 0 : ans.append(-1)
            else : ans.append(-1)
        return ans