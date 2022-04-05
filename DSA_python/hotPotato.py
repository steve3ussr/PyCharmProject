def potatoTransfer(mem_list, i):
    from pythonds.basic.Queue import Queue
    q = Queue()

    for mem in mem_list:
        q.enqueue(mem)

    while q.size() > 1:
        for cnt in range(i):
            q.enqueue(q.dequeue())
        q.dequeue()

    return q.dequeue()


if __name__ == '__main__':
    test_list = ['2131557', '2164332', '3545232', '4321564']
    res = potatoTransfer(test_list, 7)
    print(res)
