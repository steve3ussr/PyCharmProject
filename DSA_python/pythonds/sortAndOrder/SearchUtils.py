class SearchUtils(object):
    def __init__(self, alist: list, tgt):
        self.alist = alist
        self.tgt = tgt

    def disordered_search(self):
        for i, v in enumerate(self.alist):
            if v == self.tgt:
                return i
            else:
                pass
        return None

    def ordered_search(self):
        for i, v in enumerate(self.alist):
            if v == self.tgt:
                return i
            elif v > self.tgt:
                break
            else:
                pass
        return None

    def binary_search(self):

        tmp_list = self.alist
        start = 0
        end = len(self.alist)-1

        while start != end:
            mid = (start + end) // 2
            if self.alist[mid] == self.tgt:
                return mid
            elif self.alist[mid] > self.tgt:
                end = mid - 1
            elif self.alist[mid] < self.tgt:
                start = mid + 1

        return start if self.alist[start] == self.tgt else None


if __name__ == '__main__':
    seq = [17, 20, 26, 31, 44, 54, 55, 65, 77, 93]
    x = 77
    inst = SearchUtils(seq, x)
    print(res_disordered := inst.disordered_search())
    print(res_ordered := inst.ordered_search())
    print(res_bin := inst.binary_search())
