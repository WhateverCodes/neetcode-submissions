class Solution:
    def removeVowels(self, s: str) -> str:
        ans = ''
        vs = ['a', 'e', 'i', 'o', 'u']
        for ch in s :
            if ch not in vs : ans += ch
        return ans