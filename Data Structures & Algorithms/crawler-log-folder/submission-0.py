class Solution:
    def minOperations(self, logs: List[str]) -> int:
        level = 0
        for s in logs :
            if s == '../' : level = max(level-1, 0)
            elif s == './' : continue
            else : level += 1
        return level