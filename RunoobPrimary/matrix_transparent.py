from random import random


# 生成随机矩阵
row_value = 3
column_value = 4
matrix_A = []
for i in range(row_value):
    list_temp = []
    for j in range(column_value):
        list_temp.append(random())
    matrix_A.append(list_temp)
print(matrix_A)

# 转置
'''


matrix_T = []
for i in range(column_value):
    list_temp = []
    for j in range(row_value):
        list_temp.append(matrix_A[j][i])
    matrix_T.append(list_temp)
print(matrix_T)
'''

'''

'''
