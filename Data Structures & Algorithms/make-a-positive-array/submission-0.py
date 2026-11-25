class Solution:
    def makeArrayPositive(self, nums: List[int]) -> int:
        last, answer = -1, 0
        for i in range(len(nums)):
            total = 0
            for j in range(i, max(last, i - 5), -1):
                total += nums[j]
                if i - j + 1 >= 3 and total <= 0:
                    answer += 1
                    last = i
                    break
        return answer