# ImportPy

介绍一些常用的可导入的库



## collections

### Counter

Counter继承自dict类型，相当于是一种只用来计数的hash table。以下是一部分常用操作：

- 可选的初始化：`c=Counter('ababc')`
- 查询：`c['a']`
- 修改：`c['a'] += 1`
- 删除：`del c['a']`
- 清空：`c.clear()`
- 总数：`c.total() == sum(c.values())`，values是dict的方法
- 合并两个Counter：`c.update(d), d is Counter`
- 减另一个Counter：`c.subtract(d)`
- 查询前若干个，未指定则按出现次数排序所有：`c.most_common(k)`
- 返回键的列表：`sorted(c)`
- 返回键重复值的次数的列表，如`c.elements() == list("aabbc")`

### deque





## requests



## pandas

### install

`pip install pandas`

`pip install "pandas[excel]"`

### read

`DataFrame.read_csv`

### write

`DataFrame.to_csv(index=False)`

### rename column label

`DataFrame.rename(columns=lambda x: re.sub('old', 'new', x))`

### sort

``` python
DataFrame.sort_values(by=list,                    # 比如列标签
                      ascending=list,             # 递增递减
                      kind='quicksort/mergesort', # 排序算法
                      ignore_index=True)          # 不然就把index也跟着排列
```

### loc (location)

loc根据label，iloc根据index

### 给一列数据加上列标签

`Series.to_frame(name=string)`

### 合并

`pandas.concat([DataFrame1, ...], axis=1, ignore_index=True)`会按照列排序，类似matlab中的`[A, B]`



## numpy



## threading

### Timer

