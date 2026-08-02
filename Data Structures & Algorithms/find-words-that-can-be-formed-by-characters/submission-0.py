from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c = Counter(chars)
        ans = 0
        for word in words :
            t = Counter(word)
            if t <= c : ans += len(word)
        return ans