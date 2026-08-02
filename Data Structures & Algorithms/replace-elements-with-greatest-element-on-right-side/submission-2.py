class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = []
        l = len(arr)
        for i in range(l-1) :
            ans.append(max(arr[i+1 : l]))
        ans.append(-1)
        return ans