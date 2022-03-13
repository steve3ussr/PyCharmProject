def addd(i, j=1, k=100):
    return i+j+k


# 默认参数
print(addd(5))
print(addd(5, 58))
print(addd(5, 58, 564))
# 关键字
print(addd(i=5, k=58))
print(addd(5, k=58))


print('------below: 可变参数')
def sq_sum(*args):
    s = 0
    for i in args:
        s += i * i

    return s


listA = [1,2,3,4,5,6,7,8,9,10]
print(sq_sum(*listA))

