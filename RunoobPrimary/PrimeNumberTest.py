# 从a到b，判断是否为质数

import math

a = 10
b = 100
for num in range(a, b + 1):
    for i in range(2, math.ceil(math.sqrt(num))+1):
        if num % i == 0:  # 无余数，被整除，是合数，不是质数
            print('%d 被 %d 整除，不是质数' % (num, i))
            break
    else:
        print('%d 是质数' % num)
