class MinStack:

    def __init__(self):
        self.stack = [] # 2d array (val, min)

    def push(self, val: int) -> None:
        if val < self.getMin():
            self.stack.append((val, val))
        else:
            self.stack.append((val, self.getMin()))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0] # last index

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else math.inf