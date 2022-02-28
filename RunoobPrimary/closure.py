def line_conf():
    a = 1
    b = 2

    def line(x):
        print(a * x + b)

    return line


L = line_conf()
print(L.__closure__)  # (<cell at 0x05BE3530: int object at 0x1DA2D1D0>,
# <cell at 0x05C4DDD0: int object at 0x1DA2D1E0>)
for i in L.__closure__:  # 打印引用的外部变量值
    print(i.cell_contents)  # 1  ； #2

print('----------')

listA = []
for i in range(3):
    def outer_func(i): # 要有i，这样内部函数能保留 i 这个参数
        def inner_func(a):
            return a + i
        return inner_func
    listA.append(outer_func(i))

for func in listA:
    print(func(2))
    # 返回 2，3，4
