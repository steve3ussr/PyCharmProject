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
            print(f'{index_max}, {i}')
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

        def gapInsertSort(start, step):
            pass

        gap_cnt = len(alist)//2
        for i in range(gap_cnt):
            gapInsertSort(i, gap_cnt)
            # TODO: unfinished







if __name__ == '__main__':
    todo_list = [6, 5, 1, 2, 3]
    res = SortUtils().insertionSort(todo_list)
    print(res)
