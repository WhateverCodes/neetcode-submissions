class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        t = min(len(word1), len(word2))
        for i in range(t) :
            ans.append(word1[i])
            ans.append(word2[i])
        ans += word1[t:]
        ans += word2[t:]
        return ''.join(ans)