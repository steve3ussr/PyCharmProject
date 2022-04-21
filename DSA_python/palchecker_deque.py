def palchecker(a_str):
    from pythonds.basic.Deque import Deque
    str_deque = Deque()

    for i in a_str:
        str_deque.addRear(i)

    while str_deque.size() > 1:
        if str_deque.removeRear() == str_deque.removeFront():
            pass
        else:
            return False

    return True


if __name__ == '__main__':
    str_test = 'radddar'
    print(palchecker(str_test))
