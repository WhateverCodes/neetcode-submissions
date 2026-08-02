class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        pos = 0
        l = len(tickets)
        while tickets[k] > 0 :
            if tickets[pos%l] > 0 :
                tickets[pos%l] -= 1
                ans += 1
            pos += 1
        return ans