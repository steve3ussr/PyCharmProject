class Deque(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def addFront(self, i):
        self.items.insert(0, i)

    def addRear(self, i):
        self.items.append(i)

    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self):
        return self.items.pop()

    def __str__(self):
        return f'{self.items}'

    def index(self, i):
        return self.items[i]


if __name__ == '__main__':
    deq = Deque()
    deq.addFront(1)
    print(deq)
    deq.addFront(43)
    print(deq)
    deq.addRear(4)
    print(deq)

    print(deq.index(-1))
    print(deq.isEmpty())
    deq.removeFront()


