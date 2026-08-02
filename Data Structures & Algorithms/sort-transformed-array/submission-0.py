class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        ans = []
        for n in nums :
            ans.append(a*n*n + b*n + c)
        return sorted(ans)