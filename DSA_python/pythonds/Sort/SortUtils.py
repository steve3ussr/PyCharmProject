import math


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
    def shellSort(cls, alist):
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
            n = len(alist)
            max_step = int(math.log(len(alist) + 1, 3))
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
            _quickSort(st, r_idx-1)
            _quickSort(r_idx + 1, end)
            return

        _quickSort(0, len(alist) - 1)
        return alist

    @classmethod
    def quickSort_Opt(cls, alist):

        def switch(a, b):
            (alist[a], alist[b]) = (alist[b], alist[a])

        def _quickSort_Opt(st, end):
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
                    switch(l_idx, r_idx)
                else:
                    break

            switch(base_idx, r_idx)
            _quickSort_Opt(st, r_idx-1)
            _quickSort_Opt(r_idx + 1, end)
            return

        _quickSort_Opt(0, len(alist) - 1)
        return alist


if __name__ == '__main__':
    import random

    todo_list = []
    for i in range(20000):
        todo_list.append(int(random.random() * 1000))
    print(todo_list)
    # todo_list = [6, 5, 1, 2, 3]

    # todo_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # todo_list = [722, 192, 23, 392, 354, 957, 16, 346, 841, 997, 658, 875, 229, 101, 981, 343, 392, 576, 45, 452]
    res = SortUtils.quickSort(todo_list)
    print('YES!') if res == sorted(todo_list) else print('NO!')
    print(res)
    print(sorted(todo_list))
