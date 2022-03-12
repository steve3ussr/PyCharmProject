import sys
from collections.abc import Generator, Iterator, Iterable


def yanghui(maxit):
    yh = [1]
    cnt = 0
    while cnt < maxit:
        yield yh
        yh = [1] + [yh[i] + yh[i+1] for i in range(len(yh)-1)] + [1]
        cnt += 1
    return "Job Complete"


yh_test = yanghui(10)
print(isinstance(yh_test, Generator))
while True:
    try:
        print(next(yh_test))
    except StopIteration as error_content:
        print(error_content.value)
        sys.exit()
