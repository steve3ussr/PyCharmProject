class MaxBinaryHeap(object):
    def __init__(self):
        self.heap = [0]
        self.length = 0

    def findChild(self):
        return self.heap[1]

    def maxChild(self, parent):
        childLeft = 2 * parent
        childRight = childLeft + 1
        if childLeft > self.length:
            return None
        elif childRight > self.length:
            return childLeft
        else:
            return childLeft if self.heap[childLeft] > self.heap[childRight] else childRight

    def switchDown(self, parent):
        while (childMax := self.maxChild(parent)) and self.heap[parent] < self.heap[childMax]:
            (self.heap[parent], self.heap[childMax]) = (self.heap[childMax], self.heap[parent])
            parent = childMax

    def insert(self, i):
        self.length += 1
        self.heap.append(i)
        child = self.length
        parent = child // 2
        while self.heap[child] > self.heap[parent]:
            (self.heap[parent], self.heap[child]) = (self.heap[child], self.heap[parent])
            child = parent
            parent = child // 2

    def delMax(self):
        if len(self.heap) == 2:  # only has 1 ele
            return self.heap.pop()
        else:
            pass

        self.length -= 1
        heapMax = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.switchDown(1)
        return heapMax

    def isEmpty(self):
        return self.length == 0

    def size(self):
        return self.length

    def buildHeap(self, a_list):
        self.length += len(a_list)
        self.heap.extend(a_list)
        i = len(a_list) // 2  # the last parent node
        while i > 0:
            self.switchDown(i)
            i -= 1

    def __str__(self):
        return f'{self.heap[1:]}'


if __name__ == '__main__':
    # buildHeap
    test_list = [0, 3, 2, 9, 6, 5]
    h = MaxBinaryHeap()
    h.buildHeap(test_list)
    print(h)
