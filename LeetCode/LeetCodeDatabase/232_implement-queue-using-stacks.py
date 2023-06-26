class MyQueue:

    def __init__(self):
        self.data = []
        self.nums = 0

    def push(self, x: int) -> None:
        self.nums += 1
        self.data.append(x)

    def pop(self) -> int:
        if not self.nums:
            return

        tmp_stack = []
        while self.data:
            tmp_stack.append(self.data.pop())
        res = tmp_stack.pop()
        while tmp_stack:
            self.data.append(tmp_stack.pop())
        self.nums -= 1
        return res

    def peek(self) -> int:
        if self.nums:
            return self.data[0]

    def empty(self) -> bool:
        return True if self.nums == 0 else False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()