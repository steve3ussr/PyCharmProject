import functools
import time


def decorator_outer(a_func):
    @functools.wraps(a_func)
    def decorator_inner(*args, **kw):
        start_time = time.time()
        a_func(*args, **kw)
        end_time = time.time()
        print(f'{a_func.__name__} executed in {(end_time - start_time) * 1000} ms')
        return
    return decorator_inner


@decorator_outer
def test_func(a, b):
    time.sleep(0.100514)
    print(a + b)


test_func(11, 22)
print(test_func.__name__)

