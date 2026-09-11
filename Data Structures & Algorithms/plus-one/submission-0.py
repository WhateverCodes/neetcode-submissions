class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        move = 1
        for i in range(len(digits)-1, -1, -1) :
            digits[i] += move
            move = digits[i]//10
            digits[i] %= 10
        if move > 0 :
            return [move] + digits
        return digits