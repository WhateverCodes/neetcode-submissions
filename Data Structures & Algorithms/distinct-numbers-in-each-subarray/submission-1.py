class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        answer = []
        for i, value in enumerate(nums):
            counts[value] = counts.get(value, 0) + 1
            if i >= k:
                old = nums[i-k]
                counts[old] -= 1
                if counts[old] == 0:
                    del counts[old]
            if i >= k-1:
                answer.append(len(counts))
        return answer