class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        ans = []
        for ch in s :
            ans.append(ch)
            if len(ans) >= k and ans[-k:] == [ch]*k :
                for i in range(k) : ans.pop()
        return ''.join(ans)