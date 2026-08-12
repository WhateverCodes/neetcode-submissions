class Solution:
    def isValid(self, s: str) -> bool:
        hold = []
        for ch in s :
            if ch in '({[' : hold.append(ch)
            elif len(hold) == 0 : return False
            elif ch == ')' and hold[-1] == '(' : hold.pop()
            elif ch == '}' and hold[-1] == '{' : hold.pop()
            elif ch == ']' and hold[-1] == '[' : hold.pop()
            else : return False
        return len(hold) == 0