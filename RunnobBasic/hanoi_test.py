def hanoi_move(n, origin, dest):
    global cnt
    if n == 1:
        cnt += 1
        print(f'{cnt}: {origin} --> {dest}')
    else:
        mid = [i for i in column_tup if (i in [origin, dest]) is False][0]
        hanoi_move(n-1, origin, mid)
        cnt += 1
        print(f'{cnt}: {origin} --> {dest}')
        hanoi_move(n-1, mid, dest)


cnt = 0
column_tup = {'A', 'B', 'C'}
hanoi_move(10, 'A', 'C')
