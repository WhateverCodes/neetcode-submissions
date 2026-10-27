class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        ans = arrays[0].copy()
        for a in arrays[1:]:
            for n in ans.copy():
                if n not in a:
                    ans.remove(n)
        return ans