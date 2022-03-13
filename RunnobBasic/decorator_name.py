import functools, time


def add_outer(word):
    def add_print(a_func):
        @functools.wraps(a_func)
        def wrap():
            print(word)
            a_func()
        return wrap
    return add_print


@add_outer('paladin')
def test_func():
    print("test this func")


test_func()
print(test_func.__name__)
