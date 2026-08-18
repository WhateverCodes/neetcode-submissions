class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count = [0]*26
        for w in words :
            for ch in w : count[ord(ch)-ord('a')] += 1
        c = len(words)
        for n in count :
            if n%c != 0 : return False
        return True