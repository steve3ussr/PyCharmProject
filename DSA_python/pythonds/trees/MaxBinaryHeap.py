from DSA_python.pythonds.trees.MinBinaryHeap import MinBinaryHeap


class MaxBinaryHeap(MinBinaryHeap):
    def __init__(self, max_ele=1e9):
        super(MaxBinaryHeap, self).__init__(max_ele)
        self.delMax = self.delMin

    def findMax(self):
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


if __name__ == '__main__':
    # buildHeap
    print(issubclass(MaxBinaryHeap, MinBinaryHeap))
    q = MaxBinaryHeap()
    q.buildHeap([5, 9, 11, 14, 18, 19, 21, 33, 17, 27])
    print(q)
