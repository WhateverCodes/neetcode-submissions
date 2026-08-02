class MinStack:

    def __init__(self):
        self.stack = []
        self.length = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.length += 1

    def pop(self) -> None:
        self.stack.pop()
        self.length -= 1

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        min = self.stack[0]
        for num in self.stack :
            if num < min :
                min = num
        return min