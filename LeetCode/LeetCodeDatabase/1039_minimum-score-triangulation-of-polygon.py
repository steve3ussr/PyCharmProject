from math import inf

data = [35,73,90,27,71,80,21,33,33,13,48,12,68,70,80,36,66,3,70,58]



def dfs(i, j):
    if j - 1 - i == 0:
        return 0
    min_value = inf

    for k in range(i + 1, j):
        min_value = min(min_value, dfs(i, k) + dfs(k, j) + data[i] * data[j] * data[k])
    return min_value


print(dfs(0, len(data)-1))
