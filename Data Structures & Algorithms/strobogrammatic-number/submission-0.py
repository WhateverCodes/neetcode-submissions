class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mid = (len(num)+1)//2
        pos = 0
        last = len(num)-1
        while pos < mid :
            if num[pos] == '6' and num[last] == '9' :
                pos += 1
                last -= 1
            elif num[pos] == '9' and num[last] == '6' :
                pos += 1
                last -= 1
            elif num[pos] == '8' and num[last] == '8' :
                pos += 1
                last -= 1
            elif num[pos] == '0' and num[last] == '0' :
                pos += 1
                last -= 1
            elif num[pos] == '1' and num[last] == '1' :
                pos += 1
                last -= 1
            else : return False
        return True