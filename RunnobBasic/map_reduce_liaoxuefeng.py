"""
https://www.liaoxuefeng.com/wiki/1016959663602400/1017329367486080
是这个教程里的几个题
"""

# 1 规范化string列表
from functools import reduce


def string_norm(a_str):
    return a_str[0].upper() + a_str[1:].lower()


listA = ["LIsA", "gLaDoS", "ColIN"]
listB = list(map(string_norm, listA))
print(listB)


# 2 对list求积
def prod(num1, num2):
    return num1 * num2


listC = [3, 5, 7, 9]
print(reduce(prod, listC))


# 3 实现str2float
def lxf_str2float(a_str):
    digit_dict = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    }

    def chr2num(a_chr):
        """将字符转化为数字"""
        return digit_dict[a_chr]

    def multi10(i, j):
        return i * 10 + j

    i = len(a_str) - 1 - a_str.index('.')
    return reduce(multi10, map(chr2num, a_str.replace('.', ''))) / (10 ** i)


print(lxf_str2float('123.456'))
