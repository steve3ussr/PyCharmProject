def int_generator():
    i = 1
    while True:
        i += 1
        yield i


def judge(ele_1st):
    def inner(ele_inlist):
        return ele_inlist % ele_1st > 0
    return inner


def prime_generator():
    int_list = int_generator()
    while True:
        prime = next(int_list)
        yield prime
        int_list = filter(judge(prime), int_list)


def prime_limit(lmt):
    prime_list = []
    for i in prime_generator():
        if i < lmt:
            prime_list.append(i)
        else:
            return prime_list


print(prime_limit(100))
