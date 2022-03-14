import functools
import time


def decorator_outer(a_func):
    @functools.wraps(a_func)
    def decorator_inner(*args, **kw):
        start_time = time.time()
        res = a_func(*args, **kw)
        end_time = time.time()
        print(f'{a_func.__name__} executed in {(end_time - start_time) * 1000} ms')
        return res
    return decorator_inner


@decorator_outer
def fact_opt(i):
    time.sleep(1)
    return fact_true(i, 1)


def fact_true(i, prod=1):
    if i == 1:
        return prod
    else:
        return fact_true(i-1, i*prod)


print(fact_opt(5))
