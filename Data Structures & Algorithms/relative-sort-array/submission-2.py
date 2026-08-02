class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        for n in arr2 :
            ans += [n]*arr1.count(n)
        diff = sorted(list(set(arr1)))
        for n in diff :
            if n not in arr2 :
                ans += [n]*arr1.count(n)
        return ans