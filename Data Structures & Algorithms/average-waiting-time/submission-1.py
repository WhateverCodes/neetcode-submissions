class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait = 0
        time = 0
        for c in customers :
            if time <= c[0] :
                wait += c[1]
                time = c[0]+c[1]
            else :
                wait += time-c[0]+c[1]
                time += c[1]
        return wait/len(customers)