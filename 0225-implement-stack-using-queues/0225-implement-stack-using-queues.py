from collections import deque

class MyStack:
    def __init__(self):
        self.arr = deque()

    def push(self, x: int) -> None:
        self.arr.appendleft(x)

    def pop(self) -> int:
        return self.arr.popleft()

    def top(self) -> int:
        return self.arr[0]

    def empty(self) -> bool:
        if self.arr:
            return False
        else:
            return True