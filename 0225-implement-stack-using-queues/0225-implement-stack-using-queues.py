from collections import deque
class MyStack:

    def __init__(self):
        self.dq = deque()

    def push(self, x: int) -> None:
        self.dq.append(x)

    def pop(self) -> int:
        if self.dq:
            return self.dq.pop()

    def top(self) -> int:
        if self.dq:
            return self.dq[-1]

    def empty(self) -> bool:
        if not self.dq:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()