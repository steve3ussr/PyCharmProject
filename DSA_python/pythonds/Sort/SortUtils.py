import math
import pprint

from DSA_python.pythonds.trees.MinBinaryHeap import MinBinaryHeap


class SortUtils(object):
    def __init__(self):
        pass

    @classmethod
    def bubbleSort(cls, alist):
        if len(alist) <= 1:
            return alist
        else:
            pass

        for i in range(len(alist) - 1, 0, -1):
            for j in range(i):
                if alist[j] > alist[j + 1]:
                    (alist[j], alist[j + 1]) = (alist[j + 1], alist[j])
                else:
                    pass

        return alist

    @classmethod
    def shortBubbleSort(cls, alist):
        if len(alist) <= 1:
            return alist
        else:
            pass

        for i in range(len(alist) - 1, 0, -1):
            flg = 0
            for j in range(i):
                if alist[j] > alist[j + 1]:
                    (alist[j], alist[j + 1]) = (alist[j + 1], alist[j])
                    flg = 1
                else:
                    pass

            if flg:
                pass
            else:
                return alist

        return alist

    @classmethod
    def biBubbleSort(cls, alist):
        if len(alist) <= 1:
            return alist
        else:
            pass

        def switch(a, b):
            (alist[a], alist[b]) = (alist[b], alist[a])

        for i in range(len(alist)//2):
            flg = 0
            for j_pos in range(i, len(alist)-1-i):
                if alist[j_pos] > alist[j_pos+1]:
                    switch(j_pos, j_pos+1)
                    flg = 1

            for j_neg in range(len(alist)-1-i, i, -1):
                if alist[j_neg] < alist[j_neg-1]:
                    switch(j_neg, j_neg-1)
                    flg = 1

            if flg:
                pass
            else:
                return alist

        return alist



    @classmethod
    def selectionSort(cls, alist):
        if len(alist) <= 1:
            return alist
        else:
            pass

        for i in range(len(alist) - 1, 0, -1):
            tmp_list = alist[:i + 1]
            index_max = tmp_list.index(max(tmp_list))
            if index_max == i:
                pass
            else:
                (alist[index_max], alist[i]) = (alist[i], alist[index_max])

        return alist

    @classmethod
    def insertionSort(cls, alist):
        if len(alist) <= 1:
            return alist
        else:
            pass

        for i in range(0, len(alist) - 1):
            tmp = alist[i + 1]
            flg = 1
            for j in range(i, -1, -1):
                if alist[j] > tmp:
                    alist[j + 1] = alist[j]
                else:
                    alist[j + 1] = tmp
                    flg = 0
                    break
            if flg:
                alist[0] = tmp

        return alist

    @classmethod
    def shellSort(cls, alist, base=3):
        if len(alist) <= 1:
            return alist
        else:
            pass

        def _gapInsertSort(st, gap):
            """
            :st: start index
            :gap: index step
            :return: None, directly move elements in list
            """
            length = len(alist)
            for i in range(st, length - gap, gap):
                tmp = alist[i + gap]
                flg = 1
                for j in range(i, st - 1, -gap):
                    if alist[j] > tmp:
                        alist[j + gap] = alist[j]
                    else:
                        alist[j + gap] = tmp
                        flg = 0
                        break
                if flg:
                    alist[st] = tmp

        def _gen_step_list():
            n = len(alist)/2*(base-1)+1
            max_step = int(math.log(n, base))
            return list(range(1, max_step + 1))

        step_list = _gen_step_list()
        step_list.reverse()

        for step in step_list:
            for start in range(step):
                _gapInsertSort(start, step)

        return alist

    @classmethod
    def mergeSort(cls, alist):

        def _mergeSort(split_list):
            if len(split_list) <= 1:
                return split_list

            left = split_list[:len(split_list) // 2]
            right = split_list[len(split_list) // 2:]
            left = _mergeSort(left)
            right = _mergeSort(right)

            i = 0
            j = 0
            k = 0
            while i != len(left) and j != len(right):
                if left[i] < right[j]:
                    split_list[k] = left[i]
                    i += 1
                else:
                    split_list[k] = right[j]
                    j += 1
                k += 1
            tmp = split_list[:k]

            tmp.extend(left[i:]) if j == len(right) else tmp.extend(right[j:])
            return tmp

        if len(alist) <= 1:
            pass
        else:
            alist = _mergeSort(alist)
        return alist

    @classmethod
    def mergeSort_Opt(cls, alist):

        def _mergeSort_Opt(st, end):
            if (end - st + 1) <= 1:
                return

            mid_index = (end - st + 1) // 2 + st
            _mergeSort_Opt(st, mid_index - 1)
            _mergeSort_Opt(mid_index, end)

            i = st
            j = mid_index
            k = 0
            tmp_list = [None] * (end - st + 1)

            while i <= mid_index - 1 and j <= end:
                if alist[i] < alist[j]:
                    tmp_list[k] = alist[i]
                    i += 1
                else:
                    tmp_list[k] = alist[j]
                    j += 1
                k += 1

            if i <= mid_index - 1:
                while i <= mid_index - 1:
                    tmp_list[k] = alist[i]
                    i += 1
                    k += 1
            else:
                while j <= end:
                    tmp_list[k] = alist[j]
                    j += 1
                    k += 1

            alist[st:end + 1] = tmp_list

        if len(alist) <= 1:
            pass
        else:
            _mergeSort_Opt(0, len(alist) - 1)
        return alist

    @classmethod
    def quickSort(cls, alist):

        def _quickSort(st, end):
            if end <= st:
                return
            else:
                pass
            base_idx = st
            base_val = alist[base_idx]
            l_idx = st + 1
            r_idx = end

            while True:
                while l_idx <= r_idx and alist[l_idx] <= base_val:
                    l_idx += 1
                while l_idx <= r_idx and alist[r_idx] >= base_val:
                    r_idx -= 1

                if l_idx <= r_idx:
                    (alist[l_idx], alist[r_idx]) = (alist[r_idx], alist[l_idx])
                else:
                    break

            (alist[base_idx], alist[r_idx]) = (alist[r_idx], alist[base_idx])
            _quickSort(st, r_idx - 1)
            _quickSort(r_idx + 1, end)
            return

        _quickSort(0, len(alist) - 1)
        return alist

    @classmethod
    def quickSort_Opt(cls, alist):

        def switch(a, b):
            if a == b:
                return
            else:
                (alist[a], alist[b]) = (alist[b], alist[a])

        def base_decide(st, end):
            mid_idx = (end - st + 1) // 2 + st

            if alist[st] <= alist[mid_idx] <= alist[end] or alist[end] <= alist[mid_idx] <= alist[st]:
                return mid_idx
            elif alist[mid_idx] <= alist[st] <= alist[end] or alist[end] <= alist[st] <= alist[mid_idx]:
                return st
            else:
                return end

        def _quickSort_Opt(st, end):
            if end <= st:
                return
            else:
                pass

            base_idx = base_decide(st, end)
            base_val = alist[base_idx]
            switch(base_idx, st)
            base_idx = st
            l_idx = st + 1
            r_idx = end

            while True:
                while l_idx <= r_idx and alist[l_idx] <= base_val:
                    l_idx += 1

                while l_idx <= r_idx and alist[r_idx] >= base_val:
                    r_idx -= 1

                if l_idx <= r_idx:
                    switch(l_idx, r_idx)
                else:
                    break

            switch(base_idx, r_idx)
            _quickSort_Opt(st, r_idx - 1)
            _quickSort_Opt(r_idx + 1, end)
            return

        _quickSort_Opt(0, len(alist) - 1)
        return alist

    @classmethod
    def bucketSort(cls, alist, size=100):
        def hash_func(x, base):
            return x // base

        if len(alist) <= 1:
            return alist
        else:
            pass

        bucket = [[] for i in range(size)]
        for val in alist:
            bucket[hash_func(val, size)].append(val)

        res_list = []
        for v in bucket:
            res_list.extend(cls.quickSort_Opt(v))

        return res_list

    @classmethod
    def heapSort(cls, alist):
        aHeap = MinBinaryHeap()
        aHeap.buildHeap(alist)
        return [aHeap.delMin() for i in range(len(alist))]

    @classmethod
    def radixSort(cls, alist):
        if len(alist) <= 1:
            return alist
        else:
            pass

        max_digit = len(str(max(alist)))
        digit_dict = [[] for _ in range(10)]

        def extDigit(num, digit):
            tmp1 = num // (10 ** digit)
            tmp2 = num // (10 ** (digit - 1))
            return tmp2 - tmp1 * 10

        # for dgt in range(max_digit, 0, -1):
        for dgt in range(1, max_digit + 1):
            for val in alist:
                digit_dict[extDigit(val, dgt)].append(val)
            alist = []
            for _ in range(10):
                alist.extend(digit_dict[_])
                digit_dict[_] = []
        return alist

    @classmethod
    def countingSort(cls, alist):
        max_num = max(alist)
        res_dict = {_: 0 for _ in range(max_num + 1)}

        for val in alist:
            res_dict[val] += 1

        res_lst = []
        for _ in range(max_num + 1):
            res_lst.extend([_] * res_dict[_])

        return res_lst


if __name__ == '__main__':
    import random

    todo_list = []
    for i in range(10001):
        todo_list.append(int(random.random() * 10))

    todo_list = list(range(1, 21))
    todo_list.reverse()
    res = SortUtils.biBubbleSort(todo_list)
    print('YES!') if res == sorted(todo_list) else print('NO!')
    print(res)
    print(len(res))
    print(sorted(todo_list))
