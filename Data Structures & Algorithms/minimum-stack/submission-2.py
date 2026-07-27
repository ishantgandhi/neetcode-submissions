class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        minval = min(val, self.minstack[-1] if self.minstack else val)
        self.stack.append(val)

        self.minstack.append(minval)
        

    def pop(self) -> None:
        self.minstack.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]

