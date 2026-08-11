class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = k
        s = 0
        f = k-1
        l = len(blocks)
        t = blocks[s:f+1].count('B')
        while f < l :
            ans = min(ans, k-t)
            if blocks[s] == 'B' : t -= 1
            if f < l-1 and blocks[f+1] == 'B' : t += 1
            s += 1
            f += 1
        return ans