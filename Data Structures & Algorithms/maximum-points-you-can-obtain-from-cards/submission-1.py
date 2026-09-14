class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l = len(cardPoints)
        if k == l : return sum(cardPoints)
        window = l - k
        total = sum(cardPoints)
        t = sum(cardPoints[:window])
        mini = t
        for i in range(window, l):
            t += cardPoints[i]
            t -= cardPoints[i - window]
            mini = min(mini, t)
        return total - mini