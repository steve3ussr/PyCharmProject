"""
min heap: min element at top
"""


# TODO: 考虑minChild独立为方法

class BinaryHeap(object):
    def __init__(self, minVal):
        self.heap = [minVal]

    def insert(self, k):
        self.heap.append(k)
        childPos = len(self.heap) - 1  # new node index
        parentPos = childPos // 2
        while self.heap[childPos] < self.heap[parentPos]:
            (self.heap[childPos], self.heap[parentPos]) = (self.heap[parentPos], self.heap[childPos])
            childPos = parentPos
            parentPos = childPos // 2

    def delMin(self):
        # TODO: indexError情况改进，可能出现在while判断，或者min判断中（未考虑到）
        if len(self.heap) == 2:
            return self.heap.pop()
        else:
            pass

        heapMin = self.heap[1]
        self.heap[1] = self.heap.pop()
        parent = 1
        childLeft = 2 * parent
        childRight = childLeft + 1

        try:
            while self.heap[parent] > self.heap[childLeft] or self.heap[parent] > self.heap[childRight]:
                childMin = childLeft if self.heap[childLeft] <= self.heap[childRight] else childRight
                (self.heap[parent], self.heap[childMin]) = (self.heap[childMin], self.heap[parent])
                parent = childMin
                childLeft = 2 * parent
                childRight = childLeft + 1
        except IndexError:  # parent at last layer
            pass

        return heapMin

    def findMin(self):
        return self.heap[1]

    def isEmpty(self):
        return len(self.heap) == 1

    def size(self):
        return len(self.heap) - 1

    def buildHeap(self, a_list):
        # TODO： 从最后一个parentNode，如果不满足堆的有序性，就和minChild交换
        self.heap.extend(a_list)
        i = len(a_list) // 2  # the last parent node

    def __str__(self):
        return f'{self.heap[1:]}'


if __name__ == '__main1__':
    test_list = [9, 6, 5, 3, 0, 2]
    print(BinaryHeap(-1).buildHeap(test_list))

if __name__ == '__main__':
    alist = [i for i in range(1, 10)]
    print(alist)
    h = BinaryHeap(0)
    for i in alist:
        h.insert(i)
    print(h)
    minEle = h.delMin()
    print(h)

if __name__ == '__main1__':
    h = BinaryHeap(-10000)
    h.insert(5)
    h.insert(9)
    h.insert(11)
    h.insert(14)
    h.insert(18)
    h.insert(19)
    h.insert(21)
    h.insert(33)
    h.insert(17)
    h.insert(27)
    print(h)
    h.insert(7)
    print(h)
    h.delMin()
    h.delMin()
    print(h)
    h.delMin()
    print(h)
    h.delMin()
    print(h)
    h.delMin()
    print(h)
    h.delMin()
    print(h)
    h.delMin()
    print(h)
    h.delMin()
    print(h)
    h.delMin()
    print(h)
    h.delMin()
    print(h)
    h.delMin()
    print(h)
    print(h.isEmpty())
