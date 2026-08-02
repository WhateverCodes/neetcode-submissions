class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        count = 0
        while count < k:
            if tickets[count] <= tickets[k] : res += tickets[count]
            else : res += tickets[k]
            count += 1
        count = k + 1
        while count < len(tickets):
            if tickets[count] <= tickets[k] - 1 : res += tickets[count]
            else : res += tickets[k] - 1
            count += 1
        return res + tickets[k]