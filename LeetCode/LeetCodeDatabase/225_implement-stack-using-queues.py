class MyStack:

    def __init__(self):
        self.data = []
        self.nums = 0


    def push(self, x: int) -> None:
        self.nums += 1
        self.data.append(x)


    def pop(self) -> int:
        if self.nums == 0:
            return

        cnt = self.nums
        tmp_queue = []
        while cnt > 1:
            tmp_queue.append(self.data.pop(0))
            cnt -= 1
        res = self.data.pop(0)

        while tmp_queue:
            self.data.append(tmp_queue.pop(0))

        self.nums -= 1
        return res


    def top(self) -> int:
        if self.nums == 0:
            return

        cnt = self.nums
        tmp_queue = []
        while cnt > 1:
            tmp_queue.append(self.data.pop(0))
            cnt -= 1
        res = self.data.pop(0)
        tmp_queue.append(res)

        while tmp_queue:
            self.data.append(tmp_queue.pop(0))
        return res




    def empty(self) -> bool:
        if self.nums:
            return False
        else:
            return True



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()