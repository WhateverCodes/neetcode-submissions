class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = []
        one = set(nums1)
        two = set(nums2)
        ad1 = []
        for n in one :
            if n not in two : ad1.append(n)
        ad2 = []
        for n in two :
            if n not in one : ad2.append(n)
        return [ad1, ad2]