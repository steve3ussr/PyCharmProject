import sys


def fib(k):
    cnt = 0
    a, b = 0, 1
    while cnt < k:
        a, b = b, a + b
        yield a
        cnt += 1
    return "done"


f = fib(10)
while True:
    try:
        print(next(f))
    except StopIteration as qwe:
        print(qwe.value)
        sys.exit()
