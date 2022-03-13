import functools

intk = functools.partial(int, base=8)


def int2(a_str):
    return int(a_str, 8)


print(int2('114514'))
print(intk('114514'))
print(int('114514', 8))
