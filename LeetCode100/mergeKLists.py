from DSA_python.pythonds.basic.Unorderlist import Unorderlist as Lst

def main_solve(list_set):
    input_set = [_.head for _ in list_set]
    map = {_: 0 for _ in input_set}
    print(map)
    print(type(map))
    while True:








if __name__ == '__main__':
    lst1 = Lst().build([1, 4, 5])
    lst2 = Lst().build([1, 3, 4])
    lst3 = Lst().build([2, 6])

    lst_set = [lst1, lst2, lst3]
    for i in lst_set:
        print(i)



    print(lst1.head.data)
    main_solve(lst_set)
