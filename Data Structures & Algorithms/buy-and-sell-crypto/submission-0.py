class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buylow = prices[0]
        ops = []
        for p in prices :
            if p < buylow : buylow = p
            else : ops.append(p-buylow) 
        return max(ops)