# 计算 30 以内可以被 3 整除的整数
listA = [i for i in range(1, 31) if i % 3 == 0]
print(listA)

# 提供三个数字，以三个数字为键，三个数字的平方为值来创建字典：
dictA = {i: i**2 for i in [1, 2, 3]}
print(dictA)


