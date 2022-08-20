from DSA_python.pythonds.basic.Unorderlist import Unorderlist as Lst
from DSA_python.pythonds.basic.Unorderlist import Node as Node


def main_solve(head_set):
    res_head_dump = Node()
    res_head_dump.data = 0
    res_head_dump.next = None
    res_curr = res_head_dump
    cnt = 0

    while True:
        if



if __name__ == '__main__':
    lst1 = Lst().build([1, 4, 7])
    lst2 = Lst().build([2, 3, 5])
    lst3 = Lst().build([0, 6])

    lst_set = [lst1, lst2, lst3]
    for _ in lst_set:
        print(_)

    main_solve([_.head for _ in lst_set])
