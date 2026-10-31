class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        ans = mat[0]
        for ops in mat :
            for n in ans :
                if n not in ops : ans.remove(n)
        if ans == [] : return -1
        return min(ans)