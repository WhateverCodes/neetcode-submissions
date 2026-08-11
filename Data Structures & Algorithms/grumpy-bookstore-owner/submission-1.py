class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        pos = 0
        ans = 0
        l = len(customers)
        while pos < l :
            if grumpy[pos] == 0 :
                ans += customers[pos]
                customers[pos] = 0
            pos += 1
        top = 0
        for i in range(l-minutes+1) :
            top = max(top, sum(customers[i:i+minutes]))
        return ans+top