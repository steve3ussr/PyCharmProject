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
        pass


if __name__ == '__main__':
    todo_list = [6, 5, 1, 2, 3]
    res = SortUtils().selectionSort(todo_list)
    print(res)
