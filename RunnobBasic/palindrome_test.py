"""
判断数字是否是回文数
"""
for i in filter(lambda x: str(x) == str(x)[::-1], range(1, 200)):
    print(i)
# print(list(filter(lambda x: str(x) == str(x)[::-1], range(1, 200))))
