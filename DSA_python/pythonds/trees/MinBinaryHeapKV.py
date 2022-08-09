"""
min heap: min element at top

ADVANCE:
    1. delete anything
    2. (key, payload)
"""


class MinBinaryHeapKV(object):
    """

   a heap of tuple(k-v set).
   sort by k(a num).
   """

    def __init__(self, min_ele=0, payload=None):
        self.heap = [[min_ele, payload]]
        self.length = 0

    def findMin(self):
        return self.heap[1][0]

    def isEmpty(self):
        return self.length == 0

    def size(self):
        return self.length

    def __str__(self):
        return f'{[i for i in self.heap[1:]]}'

    def __contains__(self, val):
        return True if self.search_val(val) is not None else False

    def minChild(self, parent):
        """
        parent -> parent node 'index'
        return:
            1. None, if 2 children non-exist
            2. the only child index
            3. the min child index
        """
        childLeft = 2 * parent
        childRight = childLeft + 1
        if childLeft > self.length:  # childLeft non exists
            return None

        elif childRight > self.length:  # only childLeft exists
            return childLeft

        else:  # both exist
            minChild = childLeft if self.heap[childLeft][0] <= self.heap[childRight][0] else childRight
            return minChild

    def switchDown(self, parent):
        # WHILE (childMin exists) and (heap is non-ordered)
        while (childMin := self.minChild(parent)) and (self.heap[parent][0] > self.heap[childMin][0]):
            (self.heap[parent], self.heap[childMin]) = (self.heap[childMin], self.heap[parent])
            # print(f"switch 父节点{parent} 和 子节点{childMin} Done")
            parent = childMin

    def insert(self, k, v=None):
        self.length += 1
        self.heap.append([k, v])
        childPos = self.length  # new node index
        parentPos = childPos // 2
        while self.heap[childPos][0] < self.heap[parentPos][0]:  # switch parent and newChild
            (self.heap[childPos], self.heap[parentPos]) = (self.heap[parentPos], self.heap[childPos])
            childPos = parentPos
            parentPos = childPos // 2

    def delMin(self):
        return self.delAny(1)

    def delAny(self, i):
        """

        :param i: node index
        :return: heap[i]
        """
        if i == self.length:
            self.length -= 1
            return self.heap.pop()
        elif i >= 1:
            self.length -= 1
        else:
            raise IndexError(f'cannot delete heap[{i}]')

        res = self.heap[i]
        self.heap[i] = self.heap.pop()
        self.switchDown(i)
        return res

    def buildHeap(self, tup_list):

        for i, val in enumerate(tup_list):
            if len(val) != 2:
                tup_list[i] = [val[0], None]

        self.length += len(tup_list)
        self.heap.extend(tup_list)
        i = len(tup_list) // 2  # the last parent node
        while i > 0:
            self.switchDown(i)
            i -= 1

    def search_key(self, key):
        for i, kv_set in enumerate(self.heap[1:]):
            if key == kv_set[0]:
                return i + 1
        return None

    def search_val(self, val):
        for i, kv_set in enumerate(self.heap[1:]):
            if val == kv_set[1]:
                return i + 1
        return None

    def del_key(self, key):
        tmp_idx = self.search_key(key)
        print(tmp_idx)
        if tmp_idx is None:
            raise KeyError('KEY not in heap')
        else:
            return self.delAny(tmp_idx)

    def del_val(self, val):
        tmp_idx = self.search_val(val)
        if tmp_idx is None:
            raise KeyError('KEY not in heap')
        else:
            return self.delAny(tmp_idx)

    def replace_key_by_val(self, val, new_key):
        tmp = self.del_val(val)
        self.insert(new_key, tmp[1])

    def __iter__(self):
        return iter(self.heap[1:])


if __name__ == '__main__':
    """
    q = MinBinaryHeapPro()
    q.buildHeap([5, 9, 11, 14, 18, 19, 21, 33, 17, 27])
    print(q)
    """
    from random import random as rand

    tmp_k = [int(rand() * 30) for _ in range(10)]
    tmp_lst = [[_, _ ** 2 + 1] for _ in tmp_k]
    # print(tmp_lst)

    tmp_lst = [[11, 122], [27, 730], [1, 2], [16, 257], [5, 26], [10, 101], [24, 577], [10, 101], [4, 17], [8, 65]]
    inst = MinBinaryHeapKV()
    inst.buildHeap(tmp_lst)
    print(inst)
    inst.del_val(17)
    print(inst)
    inst.insert(2, 114514)
    print(inst)
    inst.replace_key(2, 7)
    print(inst)
