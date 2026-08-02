class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait = 0
        time = 0
        for get, t in customers :
            p = max(time, get)+t
            wait += p-get
            time = p
        return wait/len(customers)