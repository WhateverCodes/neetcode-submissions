from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = Counter(arr)
        uniq = 0
        for ch in arr :
            if c[ch] == 1 : uniq += 1
            if uniq == k : return ch
        return ''