class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dif = list(set(nums1))
        dif += list(set(nums2))
        ans = set()
        for n in dif :
            if dif.count(n) == 2 : ans.add(n)
        return list(ans)