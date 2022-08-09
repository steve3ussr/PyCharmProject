"""
min heap: min element at top
"""


class MinBinaryHeap(object):
    def __init__(self, min_ele=0):
        self.heap = [min_ele]
        self.length = 0

    def minChild(self, parent):
        """
        parent -> parent node 'index'
        return:
            1. None, if 2 children non-exist
            2. the only child
            3. the min child
        """
        childLeft = 2 * parent
        childRight = childLeft + 1
        if childLeft > self.length:  # childLeft non exists
            return None
        elif childRight > self.length:  # only childLeft exists
            # print(f"{parent}父节点的最小子节点为{childLeft}")
            return childLeft
        else:  # both exist
            minChild = childLeft if self.heap[childLeft] <= self.heap[childRight] else childRight
            # print(f"{parent}父节点的最小子节点为{minChild}")
            return minChild

    def switchDown(self, parent):
        # WHILE (childMin exists) and (heap is non-ordered)
        while (childMin := self.minChild(parent)) and (self.heap[parent] > self.heap[childMin]):
            (self.heap[parent], self.heap[childMin]) = (self.heap[childMin], self.heap[parent])
            # print(f"switch 父节点{parent} 和 子节点{childMin} Done")
            parent = childMin

    def insert(self, k):
        self.length += 1
        self.heap.append(k)
        childPos = self.length  # new node index
        parentPos = childPos // 2
        while self.heap[childPos] < self.heap[parentPos]:  # switch parent and newChild
            (self.heap[childPos], self.heap[parentPos]) = (self.heap[parentPos], self.heap[childPos])
            childPos = parentPos
            parentPos = childPos // 2

    def delMin(self):
        if len(self.heap) == 2:  # only has 1 ele
            return self.heap.pop()
        else:
            pass

        self.length -= 1
        heapMin = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.switchDown(1)
        return heapMin

    def findMin(self):
        return self.heap[1]

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

    def __contains__(self, item):
        return True if item in self.heap else False


if __name__ == '__main1__':
    # buildHeap
    test_list = [9, 6, 5, 3, 0, 2]
    h = MinBinaryHeap()
    h.buildHeap(test_list)
    print(h)

if __name__ == '__main1__':
    # delMin
    alist = [i for i in range(1, 10)]
    print(alist)
    h = MinBinaryHeap()
    for i in alist:
        h.insert(i)
    print(h)
    minEle = h.delMin()
    print(h)

if __name__ == '__main__':
    q = MinBinaryHeap()
    q.buildHeap([5, 9, 11, 14, 18, 19, 21, 33, 17, 27])
    print(q)
