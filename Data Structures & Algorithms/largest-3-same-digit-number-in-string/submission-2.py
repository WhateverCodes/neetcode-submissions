class Solution:
    def largestGoodInteger(self, num: str) -> str:
        nums = '0123456789'
        ans = ""
        for ch in nums :
            if ch*3 in num : ans = ch*3
        return ans