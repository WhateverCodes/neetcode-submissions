class Solution:
    def confusingNumber(self, n: int) -> bool:
        match = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }

        t = str(n)
        rotated = ""

        for x in t:
            if x not in match:
                return False
            rotated += match[x]

        return rotated[::-1] != t