import math


class SortUtils(object):
    def __init__(self):
        pass

    @staticmethod
    def bubbleSort(alist):
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

    @staticmethod
    def shortBubbleSort(alist):
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

    @staticmethod
    def selectionSort(alist):
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

    @staticmethod
    def insertionSort(alist):
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

    @staticmethod
    def shellSort(alist):
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

    @staticmethod
    def mergeSort(alist):

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

    @staticmethod
    def mergeSort_Opt(alist):

        def _mergeSort_Opt(st, end):
            if (end - st + 1) <= 1:
                return

            mid_index = (end - st + 1) // 2 + st
            _mergeSort_Opt(st, mid_index - 1)
            _mergeSort_Opt(mid_index, end)

            i = st
            j = mid_index
            k = 0
            tmp_list = [None] * (end-st+1)

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
            """
            assert (len(tmp_list) == (end - st + 1)), f'{st} -> {mid_index} -> {end} ERROR, {len(tmp_list)}'

            for i, v in enumerate(tmp_list):
                alist[st + i] = v
            """
            alist[st:end+1] = tmp_list

        if len(alist) <= 1:
            pass
        else:
            _mergeSort_Opt(0, len(alist) - 1)
        return alist

    @staticmethod
    def quickSort(alist):
        if len(alist) <= 1:
            return alist
        else:
            pass

        def _quickSort(st, end):
            if (end-st+1) <= 1:
                return
            else:
                pass

            left_index = st+1
            right_index = end
            base = alist[st]

            while right_index >= left_index:
                while







            pass

        _quickSort(0, len(alist)-1)



    @staticmethod
    def quickSort_Opt(alist):
        pass


if __name__ == '__main__':
    import random
    todo_list = []
    for i in range(100):
        todo_list.append(int(random.random() * 1000))
    # todo_list = [6, 5, 1, 2, 3]

    todo_list = [54,26,93,17,77,31,44,55,20]
    res = SortUtils().shellSort(todo_list)
    print(res)
