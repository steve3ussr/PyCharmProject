class Stack(object):
    def __init__(self):
        self.peak = None
        self.content = []

    def isEmpty(self):
        return self.content == []

    def push(self, i):
        self.content.append(i)

    def peek(self):
        if self.content:
            return self.content[len(self.content)-1]
        else:
            return None

    def size(self):
        return len(self.content)

    def pop(self):
        return self.content.pop()

    def __str__(self):
        return f"{self.content}"


if __name__ == '__main__':
    s = Stack()
    print(s.peek())
