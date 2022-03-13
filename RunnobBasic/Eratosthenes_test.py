"""
埃拉托色尼筛选法(the Sieve of Eratosthenes)简称埃氏筛法，是古希腊数学家埃拉托色尼(Eratosthenes 274B.C.～194B.C.)提出的一种筛选法。
序列2，3，4，5，6，7，8，9
第一个元素一定是素数，把他的倍数都去掉，得到：
3，5，7，9
第一个元素一定是素数，把他的倍数都去掉，得到：
5，7
"""


# 1 全体自然数generator
def every_num():
    i = 1
    while True:
        i += 1
        yield i


# 2 过滤函数
def filter_outer(ele0):
    """
    我觉得这是最大的难点，
    因为filter func应该只接受一个参数并返回bool，
    但是通常这里的判断都得输入两个参数才行，
    所以用了嵌套，
    他妈的我怎么就想不出来这种写法呢
    """

    def filter_inner(i_inner):
        return i_inner % ele0 > 0
    return filter_inner


# 3 素数generator
def primes():
    num_set = every_num()
    while True:
        next_prime = next(num_set)
        yield next_prime
        num_set = filter(filter_outer(next_prime), num_set)


# main func
def print_primes(lmt):
    for i in primes():
        if i < lmt:
            print(i)
        else:
            return


print_primes(20)
