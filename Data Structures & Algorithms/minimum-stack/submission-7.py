class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minstack.append(val)
        self.minstack=sorted(self.minstack)
    def pop(self) -> None:
        l=self.stack.pop()
        self.minstack.remove(l)
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[0]