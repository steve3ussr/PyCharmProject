[TOC]

# TODO

with上下文管理器protocol

# PyCharm 文件名颜色含义

- 绿色，已经加入版本控制暂未提交； 
- 红色，未加入版本控制； 
- 蓝色，加入版本控制，已提交，有改动； 
- 白色，加入版本控制，已提交，无改动； 
- 灰色：版本控制已忽略文件

# Python基础语法

在 Python 里，标识符由字母、数字、下划线组成。

在 Python 中，所有标识符可以包括英文、数字以及下划线(_)，但不能以数字开头。

Python 中的标识符是区分大小写的。

以下划线开头的标识符是有特殊意义的。以单下划线开头 `_foo` 的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 `from xxx import \`* 而导入。

以双下划线开头的 `__foo` 代表类的私有成员，以双下划线开头和结尾的 `__foo__` 代表 Python 里特殊方法专用的标识，如 `__init__()` 代表类的构造函数。

Python 可以同一行显示多条语句，方法是用分号 `;` 分开

---

Python中的保留字,不能用作常数或变数，或任何其他标识符名称。

所有 Python 的关键字只包含小写字母。

---

python 最具特色的就是用缩进来写模块。

缩进的空白数量是可变的，但是所有代码块语句必须包含相同的缩进空白数量，这个必须严格执行。

建议你在每个缩进层次使用 **单个制表符** 或 **两个空格** 或 **四个空格** , 切记不能混用

---

`#` 注释

` ```, """ ` 多行注释、

---

`print` 默认换行输出，在末尾加逗号可以不换行输出

![](https://www.runoob.com/wp-content/uploads/2013/11/20150529155203684.png)

# Python 输入

# Python 输出

基本：`print(var)`

## 转义字符

## 字符串格式化

示例：

```python
print("%s 今天花了 %f 元" % ('Tony', 20))
```

<table class="reference">
<tbody<tr><th>
    符   号</th>
<th>描述</th></tr><tr><td><font face="宋体" size="2" style="line-height: 23px; ">      %c</font></td><td><font face="宋体" size="2" style="line-height: 23px; "> 格式化字符及其ASCII码</font></td></tr><tr><td><font face="宋体" size="2" style="line-height: 23px; ">      %s</font></td><td><font face="宋体" size="2" style="line-height: 23px; "> 格式化字符串</font></td></tr><tr><td><font face="宋体" size="2" style="line-height: 23px; ">      %d</font></td><td><font face="宋体" size="2" style="line-height: 23px; "> 格式化整数</font></td></tr><tr><td><font face="宋体" size="2" style="line-height: 23px; ">      %u</font></td><td><font face="宋体" size="2" style="line-height: 23px; "> 格式化无符号整型</font></td></tr><tr><td><font face="宋体" size="2" style="line-height: 23px; ">      %o</font></td><td><font face="宋体" size="2" style="line-height: 23px; "> 格式化无符号八进制数</font></td></tr><tr><td><font face="宋体" size="2" style="line-height: 23px; ">      %x</font></td><td><font face="宋体" size="2" style="line-height: 23px; "> 格式化无符号十六进制数</font></td></tr><tr><td><font face="宋体" size="2" style="line-height: 23px; ">      %X</font></td><td><font face="宋体" size="2" style="line-height: 23px; "> 格式化无符号十六进制数（大写）</font></td></tr><tr><td><font face="宋体" size="2" style="line-height: 23px; ">      %f</font></td><td><font face="宋体" size="2" style="line-height: 23px; "> 格式化浮点数字，可指定小数点后的精度</font></td></tr><tr><td><font face="宋体" size="2" style="line-height: 23px; ">      %e</font></td><td><font face="宋体" size="2" style="line-height: 23px; "> 用科学计数法格式化浮点数</font></td></tr><tr><td><font face="宋体" size="2" style="line-height: 23px; ">      %E</font></td><td><font face="宋体" size="2" style="line-height: 23px; "> 作用同%e，用科学计数法格式化浮点数</font></td></tr><tr><td><font face="宋体" size="2" style="line-height: 23px; ">      %g</font></td><td><font face="宋体" size="2" style="line-height: 23px; "> %f和%e的简写</font></td></tr><tr><td><font face="宋体" size="2" style="line-height: 23px; ">      %G</font></td><td><font face="宋体" size="2" style="line-height: 23px; "> %f 和 %E 的简写</font></td></tr><tr><td><font face="宋体" size="2" style="line-height: 23px; ">      %p</font></td><td><font face="宋体" size="2" style="line-height: 23px; "> 用十六进制数格式化变量的地址</font></td></tr></tbody></table>

## f-string

> 3.6 新增的格式化方法，比%更好用，不用判断类型

```python
>>> name = 'Runoob'
>>> f'Hello {name}'  # 替换变量
'Hello Runoob'
>>> f'{1+2}'         # 使用表达式
'3'

>>> w = {'name': 'Runoob', 'url': 'www.runoob.com'}
>>> f'{w["name"]}: {w["url"]}'
'Runoob: www.runoob.com'
```

> 在3.8中还可以：

```python
>>> x = 1
>>> print(f'{x+1=}')   # Python 3.8
x+1=2
```

# Python 变量类型

在交互模式下，最后输出的结果被保存在只读变量`_`

---

`type(var)`查询类型

索引都是[]

> 知识点：python中，万物皆对象。
> 
> python中不存在所谓的传值调用，一切传递的都是对象的引用，也可以认为是传址。
> 
> python中，对象分为可变(mutable)和不可变(immutable)两种类型，
> 
> **不可变对象**：元组（tuple)、数值型（number)、字符串(string)
> 
> **可变对象**：字典型(dictionary)和列表型(list)和集合型(set)的。
> 
> 如果对不可变对象进行修改，其对应的ID（内存地址）也会变化
> 
> 对可变对象进行修改，其对应的ID（内存地址）不会变化
> 
> python 函数的参数传递：
> 
> - **不可变类型：**类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
> - **可变类型：**类似 c++ 的引用传递，如 列表，字典，集合。如 fun（la），则是将 a 真正的传过去，修改后fun外部的a也会受影响
> 
> python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
> 
> [ref1](https://www.cnblogs.com/evening/archive/2012/04/11/2442788.html)
> 
> [ref2](https://zhuanlan.zhihu.com/p/34395671)
> 
> [ref3](https://www.runoob.com/python/python-functions.html)
> 
> 如：
> 
> ```python
> def myfunc(t):
>     t += 2
>     print(id(t))
> 
> 
> a = 1
> print(id(a))
> myfunc(a)
> print(a)
> print(id(a))
> --------------------
> 2543723217136
> 2543723217168
> 1
> 2543723217136
> # 因为 *不可变对象number* ，所以只传入了内存里的值；
> # 可以看到a对应的地址没变，函数myfunc没有改变a对应的地址的内存里的内容，而是另外找了个地方
> # 最后 a 对应的地址里面的内存内容还是 1 
> 
> -----------------------------------------------
> 
> def myfunc2(t):
>     t.append('fuck')
>     print(id(t))
> 
> 
> b = [1, 2, 'a']
> print(id(b))
> print(myfunc2(b))
> print(b)
> print(id(b))
> --------------------
> 2345014392832
> 2345014392832
> None
> [1, 2, 'a', 'fuck']
> 2345014392832
> # 可以看到 *可变对象list* 所指的内存地址是不变的
> ```

- 查看内存地址对应的内容：

```python
import ctypes


get_value = ctypes.cast(Address, ctypes.py_object).value  # 读取地址中的变量
print(get_value)
```

---

> ```python
> a = 1
> b = 1
> c = a
> ```
> 
> 此时c和a是同一个地址，这没问题，**但b和a竟然也是同一个地址**
> 
> 虽然a和c不是用a = c赋值的，但是实际上他们还是指向同一个位置。说明在python中，1这个不可变的常数对象是有固定的位置的，而所有赋值为1的变量都是它的引用。
> 
> [https://blog.csdn.net/edogawachia/article/details/79919038](https://blog.csdn.net/edogawachia/article/details/79919038)

6个标准的数据类型：

## Numbers

- int（表现相等于python 2.0中的long）
- bool
- float
- complex

## String

> 单个字符也是string，不是chr/char

- 从0开始，可以用-1从右索引

- 索引：`str1[0]`

- 截取`str1[1:4]`表示第2个到第4个，**不是到第5个**
  
  <img src="https://www.runoob.com/wp-content/uploads/2013/11/o99aU.png" style="zoom:200%;" />

> **左闭右开**

- 可设置步长：`str1[1:100:2]`
- 可只有一个参数：`str1[1:]`
- 截取后返回的还是string

## List[]

- **常用**
- 可包含字符，数字，字符串甚至可以包含列表（即嵌套）
- 定义：`listA = [a, b, c]`
- 索引和截取同string
- **允许更新**

---

一些小技巧：

- 可用`del list[index]` ，根据索引删除值。如果 `del list[:]` 则清空列表。
- 可用enumerate()同时读出索引值和对应的值：

```python
for i, v in enumerate(listA): 
    print(i, v)
```

- reverse()可反向遍历；
- zip()可同时遍历多个序列：

```python
for a, b, c in zip(listA, listB, listC): 
    print(a, b, c)
```

- list.sort() 可对列表排序，不返回，直接排序；
- sorted(list) 可以返回排序后的列表，并且不改变原有列表；

---

- 可以把list当作stack使用，因为`list.append(var) `和 `list.pop()` 使得list和stack有一样的特性。
- `list.append(var) `和 `list.popleft()` 使得list可以被当作一个队列，先进先出。
- 

## Tuple()

- 和list差不多，但是不能更新，相当于**只读**
- 使用圆括号创建
- 元组中只包含一个元素时，需要在元素后面添加逗号，`Tuple_1 = ('a',)`
- 不能修改，但是可以连接

## Dictionary{}

> dict和哈希表差不多，速度快

- 也是储存变量，**可变**，**几乎任意变量**，但是不是通过偏移（1， 3）来存取
- 由key和value组成，用键[]访问
- 定义：`dictTemp = {key1:value1, key2:value2}`，用{}定义
- key一般是唯一的，value不用唯一、
- key：字符串，数字或元组，**指必须是不可变的变量**
- value：
- `dictTemp['Name'] = 'Value'`可用于键值更新，如果没有这个键则相当于往词典里添加
- 删除：`del dictTemp[key1]`只删除一个， `del dictTemp`会删除这个词典, `dictTemp.clear`可删除全部条目
- 可用 `dict()` 从包含(((键值对)的元组)列表)创建列表：

```python
dict_a = dict( [ (key1: value1), (key2: value2), (key3: value3) ] )
```

- 可用关键字创建：

```python
dict(sape=4139, guido=4127, jack=4098)
```

- 遍历：可用items()方法同时读出：

```python
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    for k, v in knights.items():
        print(k, v)
```

> 待证实：dict中的key都是传入的真值，即传入的是key1这个变量对应的值，而不是一个地址
> 
> 索引的时候用[key1]和[44]都行
> 
> 验证：
> 
> ```python
> key1 = 44
> key2 = 'abc'
> key3 = ('q', 'w', 3)
> 
> dictA = {key1: 1, key2: 2, key3: 3}
> print(dictA)
> 
> a = 22
> a *= 2
> print(dictA[a])
> ```

## set

是一个无序的不重复元素（自动去重）序列。

创建：`A = set(1, 2) / A = {1, 2}`，创建空集合时只能用前者，因为后者是用来创建词典的

判断：boolvar = var in setA

添加：set.add, set.update(后者可以是列表、元组、词典等)，**区别如下**

```python
setA = {'q', 'w'}
setA.add('asd')        # {'asd', 'w', 'q'}

setB = set()           
setB.update('asd')     # {'a', 'd', 's'}
```

set.remove(如果不在里面会报错，使用set.discard就不会报错)

set.pop随即删除一个

# Python 推导式

## list

```python
listA = [expression for varsA in listB if condition]

#tuple和set类似
```

## dict

```python
dictA = {key_expr: value_expr for value in collection if condition}
```

# Python 运算符

## 数学运算符

- `/` 商
- `%` 余
- `**` 幂
- `//` 商，但是向下取整，自带floor函数（-4.5 变成 -5）

**2.0：整数 / 相除只能得到整数，需要改成一个float**

**3.0：整数 / 相除直接得到float**

- `:=` 海象运算符，可在表达式内部为变量赋值。**Python3.8 版本新增运算符**

```python
if (n := len(a)) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")
```

---

## 位运算符：

|     |     |                     |
| --- | --- | ------------------- |
| 与   | &   | ab都为1则返回1，否则为0      |
| 或   | \|  | 有一个为1，就返回1          |
| 异或  | ^   | ab不同则返回1，相同返回0      |
| 取反  | ~   | 按位取反                |
| 左移  | <<  | a<<3，左移三位，高位丢弃，低位补0 |
| 右移  | >>  | 同上                  |

## 逻辑运算符

a = 10, b = 20

<table class="reference">
<tbody><tr>
<th>运算符</th><th>逻辑表达式</th><th>描述</th><th>实例</th>
</tr>
<tr>
<td>and</td><td>x and y</td><td> 布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。    </td><td> (a and b) 返回 20。</td>
</tr>
<tr>
<td>or</td><td>x or y</td><td>布尔"或"    - 如果 x 是非 0，它返回 x 的计算值，否则它返回 y 的计算值。</td><td> (a or b) 返回 10。</td>
</tr>
<tr><td>not</td><td>not x</td><td>布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。</td><td> not(a and b) 返回 False </td>
</tr>
</tbody></table>
> bool()函数，对于0、空字符串、空列表、空字典之后都返回0，其他都返回1
>
> 所以bool(20) = 1

## 身份运算符（用于比较两个对象的存储单元）

`a is b`判断内存地址（ID）是否一致

`a == b` 判断值

## 优先级

<table class="reference">
<tbody><tr><th>运算符</th><th>描述</th></tr>
<tr>
<td>**</td>
<td>指数 (最高优先级)</td>
</tr><tr>
<td>~ + -</td>
<td>按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)</td>
</tr><tr>
<td>* / % //</td>
<td>乘，除，取模和取整除</td>
</tr><tr>
<td>+ -</td>
<td>加法减法</td>
</tr><tr>
<td>>> <<</td>
<td>右移，左移运算符</td>
</tr><tr>
<td>&</td>
<td>位 'AND'</td>
</tr><tr>
<td>^ |</td>
<td>位运算符</td>
</tr><tr>
<td><= < > >=</td>
<td>比较运算符</td>
</tr><tr>
<td><> == !=</td>
<td>等于运算符</td>
</tr>
<tr>
<td>= %= /= //= -= += *= **=</td>
<td>赋值运算符</td>
</tr>
<tr>
<td>is is not</td>
<td>身份运算符</td>
</tr>
<tr>
<td>in not in</td>
<td>成员运算符</td>
</tr><tr>
<td>not and or</td>
<td>逻辑运算符</td>
</tr>
</tbody></table>

# Python 条件语句

Conditional Statement

```python
if condition1: 
    xxx
elif condition2: 
    xxx
else: 
    xxx
```

条件为true或false

- python不支持switch/case，只能用elif
- 条件可用逻辑运算符（and两个都满足才true， or一个满足就true， not）

> python 复合布尔表达式计算采用短路规则，即如果通过前面的部分已经计算出整个表达式的值，则后面的部分不再计算。如下面的代码将正常执行不会报除零错误：
> 
> ```python
> a=0
> b=1
> if ( a > 0 ) and ( b / a > 2 ):
>     print "yes"
> else :
>     print "no"
> ```

下面是一段~~没看懂的~~（lambda是匿名函数，见 # Python函数），因为用if/elif/else不便于维护，可以用字典：

```python
import os


def zero():
    return "zero"


def one():
    return "one"


def two():
    return "two"


def num2Str(arg):
    switcher = {
        0: zero,
        1: one,
        2: two,
        3: lambda: "three"
    }
    func = switcher.get(arg, lambda: "nothing")
    return func()


if __name__ == '__main__':
    print(num2Str(4))
```

`dict.get`: 返回指定键的值

`dict.get(key, default=None)`

- key -- 字典中要查找的键。
- default -- 如果指定键的值不存在时，返回该默认值。

返回指定键的值，如果键不在字典中返回默认值 None 或者设置的默认值。

# Python 循环语句

## while

![](https://www.runoob.com/wp-content/uploads/2013/11/886A6E10-58F1-4A9B-8640-02DBEFF0EF9A.jpg)

```python
while condition: 
    statements
```

---

## 循环控制

<img src="https://static.runoob.com/images/mix/python-while.webp" style="zoom:50%;" />

- `continue`跳过这次循环，循环后面的都不执行
- `break` 退出循环
- `pass`维持程序完整，执行循环后面的语句，常用于占位，写和不写都行
- `while/for-else` 当cond为false时，执行statements（break的时候不会执行else后的语句，只有正常循环执行完才会执行else后的语句）

```python
else:
    statements
```

## for

![](https://www.runoob.com/wp-content/uploads/2013/11/A71EC47E-BC53-4923-8F88-B027937EE2FF.jpg)

```python
for iterating_var in sequence:
   statements(s)
```

sequence可以是string，list，等

---

range函数返回的是一个class，不是list

`range(start, stop)`

`range(start, stop, *step*)`

**range(5) 对应的序列为0、1、2、3、4，从0开始**

**range(5， 3) 对应的序列为5、6、7，从0开始**

**range(anynumber， 1) 对应的序列是空的**

---

```python
# 从a到b，判断是否为质数

import math

a = 10
b = 100
for num in range(a, b + 1):
    for i in range(2, math.ceil(math.sqrt(num))+1):
        if num % i == 0:  # 无余数
            print('%d 被 %d 整除，不是质数' % (num, i))
            break
    else:
        print('%d 是质数' % num)
```

# Python 函数

## 函数说明文档

```python
def myfunc():
    '''
    qweeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeq
    qewwwwwwwwwwwwwww
    dweqfew
    :return:
    '''
    print("q")


myfunc()
print(myfunc.__doc__)
```

## 函数结束和返回

return函数会结束函数

如果没有要返回的，可以就写一个return

> 如果没有要返回的，不写也行，但我不知道会有什么后果

可以返回多个值（tuple type）

## 匿名函数、表达式、lambda

可以不用def定义函数，用匿名函数或者说表达式比较方便写，可以不用命名函数。写法：

```python
# funcName = lambda arguments:expression
multifunc = lambda x, y, z: x*y*z
print(multifunc(3, 4, 5))

# 或者不用函数名直接用
print((lambda x, y: x+y)(5, 100)) # 105

# 如果没有args
a = lambda : "eqwe"   # a 是一个函数
print(a)              # 会显示是个在某地址的lambda函数
print(a())            # 显示"eqwe"
```

## 定义函数

```python
def funcname(args): 
    statements
    [return(args)]
```

不return的话，返回的就是None

`a = 1`：1是对象，对象的类型是`int`；a是对对象1的引用，a没有类型

## 参数

### 必备参数

就平时写的那种

### 关键字参数

使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。

在内部组装成dict

### 默认参数

> default args should be immutable, `None` for example. 

定义函数时可以写默认值，**默认参数在定义时必须在最后面**

```python
def myfunc(q, w=100): 
    """这里可以注释"""
    return(q + 2*w)

---
myfunc(1, 2)        # ans = 5
myfunc(w=1, q=2)    # ans = 4
myfunc(5)           # ans = 205
myfunc(w=5)         # ERROR
myfunc(77)          # ans = 277
```

### 不定长参数

可以让函数处理额外的参数。

- 一个星号，导入的是tuple
- 两个星号，导入的是dict
- **在函数内不用写星号**
- **强制位置参数**：`def func(a, /, b, * c)`则星号后面的必须以关键字参数的形式传入，/ 之前的必须是不能是关键字参数，之间的随便

例子：假如我们要计算一些数的平方和，我们可以传入[1, 2, 3]，但是这不优雅，所以利用*args可以不组装成list。

```python
def sq_sum(*args):
    s = 0
    for i in args:
        s += i * i
    return s


print(sq_sum(1,2,3,4,5,6,7,8,9,10))
```

如果我们已经有一个list或者tuple，想把里面的元素都当作参数传入，可以写`sq_sum(*list)`

```python
def myfunc(a, *extra_args):
    """喜加一"""
    a += 1

    for var in extra_args:
        print("WARNING: EXTRA ARGUMENTS: ", var)

    return a


print(myfunc(3, 4, 5))
```

## 局部变量

函数内的是局部变量，函数外的是全局变量

想要在函数内改变全局变量：**应该在函数内global这个变量，不是在函数外部global**

```python
def myfunc(str1):
    print(str1)
    global i
    i += 1


i = 0
myfunc('func')
print(i)
```

## Recursion 递归

典型例子是求阶乘：

```python
def factorial(i): 
    prod = 1
    if i == 1:
        return prod
    else: 
        return i * factorial(i-1)
```

但是这里return的是一个带有递归函数本身的表达式，容易造成栈溢出。

解决方法是可以用尾递归：

```python
def factorial(i, prod=1): 
    if i == 1:
        return prod
    else: 
        return factorial(i-1, i * prod)
```

但由于大部分语言对尾递归也没有优化，所以不一定有用。

---

如何给recursion func加decorator？正常加会报错。所以应该给递归函数加一个不递归的函数：

```python
import functools
import time


def decorator_outer(a_func):
    @functools.wraps(a_func)
    def decorator_inner(*args, **kw):
        start_time = time.time()
        res = a_func(*args, **kw)
        end_time = time.time()
        print(f'{a_func.__name__} executed in {(end_time - start_time) * 1000} ms')
        return res
    return decorator_inner


@decorator_outer
def fact_opt(i):
    time.sleep(1)
    return fact_true(i, 1)


def fact_true(i, prod=1):
    if i == 1:
        return prod
    else:
        return fact_true(i-1, i*prod)


print(fact_opt(5))
```

## 函数嵌套——闭包

> 我觉得最常用的一个场景：假如我们需要一个函数输入两个args，但是由于某种原因只能留下一个arg，就可以用这种方法。
> 
> ```python
> def outer(arg1): 
>     def inner(arg2): 
>         statements with arg1 & arg2
>     return inner
> ```

[Ref](https://blog.csdn.net/sc_lilei/article/details/80464645)

首先给出[闭包](https://so.csdn.net/so/search?q=闭包&spm=1001.2101.3001.7020)函数的必要条件：

- 闭包函数（外层函数）必须返回一个函数对象（内部函数）
- 闭包函数返回的那个函数必须引用外部变量（一般不能是全局变量），而返回的那个函数内部不一定要return

如：

```python
def func1(x):
    def func2(y):
        return x * y
    return func2    # return func2返回的是一个对象，可理解为func1是func2的一个对象


print(func1(7)(8)) # 56
```

> **以上有两个括号! 才能执行内部嵌套函数!!**

def 限定了局部变量的作用域，超过作用域就会被销毁，函数内的代码访问变量的方式是从其所在层级由内向外的。比如内部函数发现没有x，就像外层找，在 func1 找到了，那就能用；找不到就ERROR了。（可以找外层函数-父函数作用域内的任意变量，参数）

>  闭包大大提高了代码的可复用性

闭包的内部函数在被 return 的时候，其所引用的全部参数，包括自己的还有外部的，都被保存起来了，是固定的。查看内部函数的`__closure__`属性（返回 tuple 变量）可知都有哪些变量。

如果没引用，就会显示None（而且没引用外部变量的话，从定义上也不是闭包）

如果外部函数没有return，就没有`__closure__`属性，会显示报错（也不是闭包）

```python
def line_conf():
    a = 1
    b = 2

    def line(x):
        print(a * x + b)

    return line


L = line_conf()
print(line_conf().__closure__) #(<cell at 0x05BE3530: int object at 0x1DA2D1D0>,
# <cell at 0x05C4DDD0: int object at 0x1DA2D1E0>)
for i in line_conf().__closure__: #打印引用的外部变量值
    print(i.cell_contents) #1  ； #2
```

```
def line_conf(a):
    b = 1

    def line(x):
        return a * x + b

    return line


line_A = line_conf(2)
b = 20
print(line_A(1))  # 3
```

这里可以看出，内部函数引用的变量已经固定了，保存在 `__closure__`属性里。

所以闭包可以保存运行时的环境。

---

```python
_list = []
for i in range(3):
    def func(a):
        return i+a
    _list.append(func)
for f in _list:
    print(f(1))
```

此时会显示3，3，3。因为list的每个元素都是函数：i+a。直到执行的时候才会查找值，其中由于i循环到2，a为写的1，所以全都是2+1=3。

所以最后输出的都是3。

```python
_list = []
for i in range(3):
    def func(i):
        def real_func(k):
            k += i
            return k

        return real_func


    _list.append(func(i))

for j in _list:
    print(j(1))
```

此时输出的就是0+k, 1+k, 2+k。

---

“内部函数”可以修改“外部函数（装饰器）”的局部变量值，通过关键字 `nonlocal`。

# Python 高级特殊函数

## map, reduce, filter

`map(func, Iterable)`，将函数作用于可迭代变量的每一个元素中。 最后返回一个**Iterator**。

```python
def f(i):
    return i * i


listA = [x for x in range(1, 10)]
it = map(f, listA)
print(type(it))
print(list(it))
```

`reduce(func, Iterable)`，其中这个func必须有两个arg。reduce将Iterable的前两个值进行func，将得到的结果再和第三个func。

比如我对一个整数list求和。

map和reduce组合应用的例子：

```python
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
```

`filter()`也是接受两个变量，一个函数和一个可迭代。对序列中每个元素进入函数并返回True或者False，以此为依据，filter决定是否删除某些元素，比如删除string中空格，删除数字中的奇数。

**filter返回的也是惰性序列**

## sort

排序，高级的排序。

`sort(obj, [key = abs[, reverse = True]])`

- key: 创造一个映射，将key的函数作用于obj，再进行比较，返回的是obj原有的元素；
- reverse：默认从小到大，可改成从大到小；

## sorted

区别：

- `sort`作用于列表，直接改变列表；
- `sorted`作用于容器，返回一个新的容器；

常见用法：`sorted(obj, [key=lambda ... ])`，根据函数值返回新容器。

## 偏函数

> 并非数学中的概念

比如int函数可以把str转为十进制int，传入额外的参数可以转化为其他进制，比如`int(obj, 16)`或者写成`int(obj, base=16)`。

但假如说我们要批处理，就不方便。可以定义一个`int2`函数。

```python
def int2(a_str):
    return int(a_str, 8)


print(int2('114514'))
print(int('114514', 8))
```

python还有内置的一个写法：

```python
import functools
int2 = functools.partial(int, base=2)
```

意思是可以把int这个函数的base关键字设定为默认值为2（原来是10）

# Python 模块、包

## Module

模块里：定义对象和语句，一般是定义函数。比如模块文件`mymodule.py`里定义了函数`myfunc`，在主函数里调用方法：

```python
import mymodule
import mymodule as mm # 我猜如果这两句话同时出现，仍然只会导入一次（py不会重复导入），但是使用原名和昵称 *确实* 都行
---
mm.myfunc(args)

-------------------------
from mymodule import myfunc [as xxx] # 就可以不加module.了，而且可以自定义名字
from mymodule import *      # 全部导入
myfunc(args)
```

---

`dir()` 函数，返回一个字符串列表，里面是查询对象的所有属性名称。

- 如果我想查看列表这个变量类型的属性，`dir([])`
- 如果我想查看词典这个变量类型的属性，`dir({})`
- 如果是一个模块，可以返回其属性、函数（**说是还能返回变量，但我试了怎么没看到呢**）

---

py 3.0 从 imp 导入reload函数可以重新加载模块，但是得使用模块才开始加载，只reload不调用是不行的。

---

## Package

包就是一个文件夹

包是一个分层次的文件目录结构，它定义了一个由模块及子包，和子包下的子包等组成的 Python 的应用环境。

**里面必须包含__init__.py，里面可以是空的**

如果在PyCharm里新建一个软件包，里面自带一个`__init__.py`

调用方法：

- 在某处有一个主程序，在同级目录里还有一个包（文件夹），这是前提；
- 导入方法：`from package_name import file_name(推荐使用)`，`import package_name.file_name`，`from package.file import func(然后就可直接用函数名了)`；

---

在win下文件不分大小写，因此导入可能会有问题。所以一般在`__init__.py`里写一个变量：

```python
__all__ = [
    'file1', 'file2', ...
]
```

示例：模块里定义了一个类：

![](https://i.imgur.com/XBJKAlP.png)

```python
from pythonds.basic.Stack import Stack
```

这是正确的写法。

我的错误写法是：

```python
from pythonds.basic import Stack
```

问题在于：

我是从Stack.py这个文件里导入Stack这个类，所以虽然文件和类重名，但是关系要搞清楚。

## 路径

例子：

`from .TreeNode import TreeNode`

1个点：同一文件夹，当前目录

每多第一个点：上一层目录

# Python `__name__ == '__main__'`

[ref](https://blog.csdn.net/heqiang525/article/details/89879056)

有的时候一个python文件我们希望既可以单独执行，也可以 *作为模块* 被导入到别的程序中，所以就需要这种写法。

原理：

1. 每个py文件都有一个内置的属性：`__name__`，是一个字符串，如果单独执行这个程序，则该属性为`__main__`；如果被导入到别的地方，则为不带后缀的文件名（模块名）；
2. 因此若直接执行某个文件，`(__name_ == '__main__') == true`；
3. **通常利用这个来进行模块的测试，测试代码放在条件语句后**。

# Python 命名空间、作用域

- 变量是拥有匹配对象的名字（标识符）。
- 命名空间是一个包含了变量名称们（键）和它们各自相应的对象们（值）的字典。
- 一个 Python 表达式可以访问局部命名空间和全局命名空间里的变量。如果一个局部变量和一个全局变量重名，则局部变量会覆盖全局变量。
- 如果在局部空间直接使用全局空间里的变量，就会报错；必须使用**在局部空间global函数**

globals和locals函数可以返回所在空间的名字（包括被global的）。返回的是个字典，可以用keys函数获取名字

# Python Iterable, Iterator, Generator

## 概述

![](https://i.imgur.com/s8eYkp8.jpg)

1. 可迭代协议：实现了`__iter__()`方法；
2. 迭代器协议：实现了`__iter__()`和`__next__()`方法；
3. `iterable`：**可迭代对象**，实现了`__iter__()`方法的一个类；往往预先知道长度和数据；
4. `iterator`：**迭代器**，继承自`iterable`，实现了`__iter__()`和`__next__()`方法的类。是惰性的，只有通过`next`才能返回元素；
5. `generator`：**生成器**，也能实现实现了`__iter__()`和`__next__()`方法，但更像是一个函数而不是一个类；属于迭代器，但是更高级更简洁；
6. `container`：**容器**，只能用来装元素，比如列表、元组。大部分容器都实现了`__iter__()`方法；但是不实现`__next__()`方法就不能 *取* 元素；
7. 内置函数`iter()`可以把可迭代对象变成迭代器，加了一个`__next__()`方法。比如`for mem in list`，或者`enumerate`其实是先使用了`list.iter()`，然后不断`next()`，直到`ErrorIteration`停止；
8. `generator`更优雅，比如一个函数中通过`yield`返回元素，或者推导式中用`()`代替`[]`。并不提前计算所有值，而是在需要的时候才计算，因此节约内存；

## Generator

生成平方数，常规方法：

```python
listA = [x*x for x in range(10)]
for i in listA: 
    print(i)
```

改成generator只要改成圆括号：

```python
listA = (x*x for x in range(10))
for i in listA: 
    print(i)
```

或者用next输出（直到StopIteration）。

这两种的区别是：第一种一开始就把所有元素写到内存里，比较占空间；后者是定义了一种递推，需要循环多少次就循环多少次，节约内存。

另一种定义generator的方法：

如果def func中包含`yield`关键字，则该函数是**generator函数**，调用时会返回一个generator。yield的原理是：

1. 在被next调用时，函数运行到yield这一行之后就返回yield后面的内容；
2. 下一次被next调用时，从yield后面的开始执行，再到yield停止；
3. 到return 真正终止。

```python
import sys


def fib(k):
    cnt = 0
    a, b = 0, 1
    while cnt < k:
        a, b = b, a + b
        yield a
        cnt += 1
    return "done"


f = fib(10)
while True:
    try:
        print(next(f))
    except StopIteration as qwe:
        print(qwe.value)
        sys.exit()
```

`except StopIteration as qwe `：如果不加as的话就无法捕捉return的值，因为这个值包含在异常内部，所以要这么写。

杨辉三角：

```python
import sys
from typing import Iterable # or from collections.abc


def yanghui(maxit):
    yh = [1]
    cnt = 0
    while cnt < maxit:
        yield yh
        yh = [1] + [yh[i] + yh[i+1] for i in range(len(yh)-1)] + [1]
        cnt += 1
    return "Job Complete"


yh_test = yanghui(10)
print(isinstance(yh_test, Iterable))
while True:
    try:
        print(next(yh_test))
    except StopIteration as error_content:
        print(error_content.value)
        sys.exit()
```

## Iterator

`iter()`返回一个迭代对象，`next()`返回迭代对象的下一个元素。

迭代器只能单向前进。

可以用for循环，或者next+StopIteration+sys.exit控制。

> 迭代对象：属于Ierable类，可用isinstance判断。

# Python 装饰器

> 对于递归函数直接用decorator不行，得给递归函数外面加一层不递归的函数

代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。一般用来给一个函数增加新功能。

```python
def add_print(afunc): 
    def print_content(): 
        print("adding")
        afunc()
        print("added")

    return print_content
```

对于一个传入的函数`afunc`，返回的是这样一个函数：在开始和结束增加了两行输出。

比如：

```python
def print_func(): 
    print('fuck')


print_func = add_print(print_func)
print_func()
```

输出有三行。

这里有一个操作，就是要给`print_func`赋值，python有个方法可以把这个操作简化一下，使用`@`。在被传入decorator的函数之前加一句话：

```python
@add_print
def print_func(): 
    print('fuck')


print_func()
```

结果是一样的。

---

如果被装饰的函数带有一些参数，在定义最内层函数的时候应该：`def inner(*args, **kw)`，在其中执行原函数的时候也应该带有`*args, **kw`。

---

以上的都有问题。返回的函数里，`__name__`属性会被替换成decorator内部的函数名，有些依赖函数签名的代码执行就会出错。python中的解决方案：

1. 在decorator中定义`innerFuc.__name__ = original.__name__`

2. python内置了一个方法：
   
   1. `import functools`
   
   2. 在最内层函数前面加上`@functools.wraps(ori_func)`

例子：

```python
import functools


def deroctator(k)
    def outer(afunc):
        @functools.wrap(afunc)
        def inner（*args, **kw): 
            print(k)
            afunc(*args, **kw)
            print(k)
        return inner
    return outer

@deractator(k)
def func(): 
    pass
```

# Python 面向对象

> Object Oriented Programming，简称 OOP

和面向对象相对的是面向过程。

如果采用面向对象的程序设计思想，我们首选思考的不是程序的执行流程，而是把数据被视为一个对象。

面向对象里最重要的就是Class和Instance。Class是抽象的模板，形容了一系列instance；而instance是一个个对象。

对象包括两大点：属性（**attribute**，不是他妈的property）和方法（**class method**）。

比如定义一个类student，“Alice”和“Bob”是这个类下的两个实例。在类中包括了属性：学号，身高，体重，年龄；还有方法（函数），比如吃饭，学习。

## 创建类型和对象

> 类型（class）实际上是一种我们定义的数据类型（type），和int、list一样，
> 
> 都是`type(int)`返回`<class 'type'>`

```python
class Student(object): 
```

- 对象的名称通常为首字母大写（妈的，object都不大写）；
- `object`是继承的类，所有的class最终都将继承object，没指定就这么写；

类是一个**模板**，所以应该把类里的inst的**所有属性和方法**都定义了：

```python
class Student(Object): 
    # __init__ 是初始化的函数，这里面都是properties
    # __init__ 的第一个参数必须是self，表示inst本身，并且调用的时候不用传递这个arg
    def __init__(self, name, number, age): 
        self.name = name
        self.number = number
        self.age = age  
```

如果没有定义任何属性，则可以`alice = Student()`；

如果定义了参数，则应当`alice = Student('Alice', 114514, 19)`;

> Python是动态的，可以在外部给一个inst一个在class内部没定义的属性，但是这样不安全，可读性差

## 数据封装

> “封装也称为信息隐藏,是利用抽象数据类型将数据和基于数据的操作封装在一起,使其构成一个不可分割的独立实体,数据被保护在抽象数据类型的内部,尽可能地隐藏内部的细节,只保留**一些对外接口**使之与外部发生联系。”
> 
> 好处：
> 
> 1. 控制存取属性值的语句来避免对数据的不合理的操作
> 2. 一个封装好的类，是非常容易使用的
> 3. 代码更加模块化，增强可读性
> 4. 隐藏类的实现细节，让使用者只能通过程序员规定的方法来访问数据

通过在class里定义一些方法（一些函数），来实现各种接口。比如定义打印年龄的函数：

```python
    ...
    # 除了第一个参数是self外，其他和普通函数一样
    def print_age(self): 
        print(f"{self.name}的年龄是：{self.age}")
```

使用方法的方法：

```python
alice.print_age()
```

## 限制访问

为了不让内部属性被随意访问和修改（但是可以初始化），在创建类的属性时应这样：

```python
class Student(object): 
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
```

在Python中，实例的变量名如果以`__`开头，就变成了一个私有变量（private），只有内部可以访问，外部不能read。

==疑问：这里不应该是属性变成了private吗，如果有的属性public有的属性private，那这个inst应该是也不能说是完全public或者private==

- `__name__`这种是可以直接访问的特殊变量；
- `__name`这种是private变量；
- `_name`这种是在class中表示是公开的，但是不建议随意访问。*按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。*
- 单下划线`_name`命名的变量（包括类，函数，普通变量）不能通过**from module import **导入到另外一个模块中。
- 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问`__name`是因为Python解释器对外把`__name`变量改成了`_Student__name`，所以，仍然可以通过`_Student__name`来访问`__name`变量：`alice._Student__name`。但是不同版本的Python解释器可能会把`__name`改成不同的变量名。

---

但是这样就不能赋值了，所以在类里一般定义`get_property`和`set_property`来做访问和赋值。

而且这样还可以在赋值语句之前进行检查，避免传入无效参数。

```python
class Student(object):
    def __init__(self, name, age):
        self.__grade = None
        self.name = name
        self.age = age

    def set_grade(self, num):
        self.__grade = num

    def print_age(self):
        print(f"{self.name}的年龄是：{self.age}")

    def print_grade_level(self):
        if self.__grade >= 90:
            print(f"{self.name}的成绩是：牛B")
        elif self.__grade >= 80:
            print(f"{self.name}的成绩是：良")
        elif self.__grade >= 70:
            print(f"{self.name}的成绩是：中")
        elif self.__grade >= 60:
            print(f"{self.name}的成绩是：及格")
        else:
            print(f"{self.name}的成绩是：寄")


# create inst
alice = Student("Alice Whitman", "12")
colin = Student("Colin McRae", "25")


list_student = [alice, colin]
list_grade = [59, 100]

# 我猜这里元组自动拆包
for mem, grade in zip(list_student, list_grade):
    mem.set_grade(grade)
    mem.print_grade_level()
```

> Alice Whitman的成绩是：寄
>         Colin McRae的成绩是：牛B

以上代码可以运行，但是`__init__`也可以写成：

```python
    def __init__(self, grade, name, age):
        self.__grade = grade
        self.__name = name
        self.__age = age
```

==疑问：如果都是private属性应该可以这么写，因为都得通过调用方法来赋值。但如果是公有私有都存在，可能只能按我的写法来==

如果写成`alice.__grade = 100`并不能真正的赋值，因为这时alice有两个属性`__grade`（自创的）和`_Student__grade`（预定义的）。

## 继承和多态

判断inst的class用`iainstance()`；

---

> 继承：extend, inheritance

可以从一个父类、基类（base class）超类（**Super class**）创建子类（subclass），这叫继承。

继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以**把父类不适合的方法覆盖重写**。

继承什么？公有的属性和方法：

- 假如子类和父类都有同样名字的方法，子类的会覆盖父类的（多态）；
- 假如一个inst属于某个subclass，那他也属于base class；

> 多态：polymorphism，指为不同数据类型的实体提供统一的接口，同一个行为具有多个不同表现形式或形态的能力。

多态存在的三个必要条件：

- 继承
- 重写
- 父类引用指向子类对象：**Parent p = new Child();**（这句是Java的，我还不懂这句话什么意思）

![](https://www.runoob.com/wp-content/uploads/2013/12/2DAC601E-70D8-4B3C-86CC-7E4972FC2466.jpg)

假如一个base class有很多subclass，这些不同的类都要实现一个方法，如果我在base class直接定义，可能subclass用起来会有问题。比如在主函数定义:

```python
def print_twice(inst): 
    Class.run()
    Class.run()
```

在base class定义：

```python
    def run(self): 
        pass
```

然后在sub classes里定义不同的具体的run()，**比如print不同的内容**，就都可以正确实现，因为他们都属于base class。

1. 在执行时先到最顶层的父类里寻找run，没有的话就报错；
2. 在父类里找到之后，再去inst所属的子类里寻找有没有**重写**run；
3. 执行能找到的“最子类”的run；

---

著名的“开闭”原则：

- 对扩展开放：允许新增`BaseClass`的子类；

- 对修改封闭：不需要修改依赖`BaseClass`类型的`run_twice()`等函数。

---

## 鸭子类型

> 鸭子类型（英语：duck typing）是动态类型的一种风格。在这种风格中，一个对象有效的语义，不是由继承自特定的类或实现特定的接口，而是由"当前方法和属性的集合"决定。
> 
> 当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子。
> 
> ​                                                                                                                                                    ——James Whitcomb Riley

Python这种动态语言不要求严格的继承，假如我新建一个class，不从animal继承，直接从object继承，再给他写一个run方法，那么也可以run。

我觉得都可以理解，因为是根据inst所在的class来找run的。只要这inst有run这个名字的方法，就都可以用。

```python
class Human(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_age(self):
        print(f"{self.name}的年龄是{self.age}")

    def print_secret(self):
        pass


class Student(Human):
    def set_grade(self, i):
        self.__grade = i

    def print_grade_level(self):
        if self.__grade >= 90:
            print(f"{self.name}的成绩是优")
        elif self.__grade >= 60:
            print(f"{self.name}的成绩是还行")
        else:
            print(f"{self.name}的成绩是寄")

    def print_secret(self):
        print(f"{self.name}的秘密是：这次考试考了{self.__grade}")


class Teacher(Human):
    def set_wage(self, i):
        self.__wage = i

    def print_wage_level(self):
        if self.__wage >= 20000:
            print(f"{self.name}是大老板")
        elif self.__wage >= 10000:
            print(f"{self.name}是小老板")
        else:
            print(f"{self.name}是打工人")

    def print_secret(self):
        print(f"{self.name}的秘密是：这月工资拿了{self.__wage}")


# initialization
list_student_name = ['Alice Whitman', 'Colin McRae']
list_student_age = [16, 25]
list_student_grade = [59, 100]
list_teacher_name = ['Yigang Wang', 'Zhigang Yang']
list_teacher_age = [57, 61]
list_teacher_wage = [10000, 20000]

alice = Student(list_student_name[0], list_student_age[0])
colin = Student(list_student_name[1], list_student_age[1])
xiaogang = Teacher(list_teacher_name[0], list_teacher_age[0])
dagang = Teacher(list_teacher_name[1], list_teacher_age[1])
list_student_mem = [alice, colin]
list_teacher_mem = [xiaogang, dagang]

for mem, grade in zip(list_student_mem, list_student_grade):
    mem.set_grade(grade)

for mem, wage in zip(list_teacher_mem, list_teacher_wage):
    mem.set_wage(wage)


# test
def uncover(human_inst: Human): # 强调了具体类型，但是不是强制的，“鸭子类型”也可以用
    human_inst.print_secret()


if __name__ == '__main__':
    for mem in list_student_mem:
        mem.print_age()
        mem.print_grade_level()
        uncover(mem)

    for mem in list_teacher_mem:
        mem.print_age()  # public base method
        mem.print_wage_level()  # methods in different subclasses
        uncover(mem)  # methods in different subclasses


# ---DUCK
class Duck(object):
    def __init__(self):
        pass

    def print_secret(self):
        print("GAGA, I'm Duck!")


uncover(Duck()) # 你看，即使 line: 68 声明了得用Human，也还是行得通
```

## 获取对象信息

使用type()，可以知道一个对象是什么class，比如int，Student，list。

如果对象引用了一个函数，此时可以：

```python
import types
def fn(): 
    pass


>>> type(fn)==types.FunctionType
True
>>> type(abs)==types.BuiltinFunctionType
True
>>> type(lambda x: x)==types.LambdaType
True
>>> type((x for x in range(10)))==types.GeneratorType
True
```

但是以上方法不太适合判断继承的class。所以用`isinstance()`,**推荐**.

`isinstance(object, ClassName)` 会返回bool。

type也可以用这个函数替代：`isinstance(1, int)`

或者可以判断对象是否是某些类型中的一种，比如：`isinstance(object, (int, str))`

---

dir()可以获取对象的所有属性和方法。

---

`__len__`是对象的一个方法，而常用的`len()`函数只是调用了对象的这个方法，比如`len(list)`。

如果我想让自定义的类也能用len，可以自己在class里写一个：

```python
    def __len__(self): 
        self.__len__ = 100
```

三个和属性有关的函数：

1. `getattr(obj, 'attr_name'[, default_return])` 
2. `hasattr(obj, 'attr_name')` return bool
3. `setattr(obj, 'attr_name', var)`可以给对象属性+1

## 类属性和实例属性

之前的attr都是inst的，但是我们也可以给class一个attr。

```python
class Human(object): 
    def __init__(self): 
        pass

    name = "Human_defaultName"
```

创建两个inst：

```python
tny = Human()
lyb = Human()
lyb.name = "lybKing"
print(lyb.name)  # "lybKing"
print(tny.name)  # "Human_defaultName"
del lyb.name
print(lyb.name)  # "Human_defaultName"
```

类属性感觉相当于默认值，实例属性的优先级比类属性高，因此并不是覆盖。

**不要对实例属性和类属性使用相同的名字**

一个案例：假如class有个attr是计数器，统计有多少个inst；每创建一个inst就+1，如何实现？

```python
class Student(object):

    def __init__(self, name):
        self.name = name
        Student.count += 1

    count = 0


# main
if __name__ == "__main__":
    alice = Student("Alice")
    colin = Student("Colin")
    print(Student.count)
```

因为每次创建inst都会调用`__init__`函数，所以可以在这里实现+1。

并且count的初始赋值可以在任何一个位置，只要在class里面就行。

# Python 面向对象 Prime

[廖雪峰：Python面向对象高级编程](https://www.liaoxuefeng.com/wiki/1016959663602400/1017501655757856)

## 给实例和类添加属性和方法

假设定义了一个空的class，那么通过`inst.attr = var`可以给这个inst单独增加属性；

也可以给inst单独加一个方法：

```python
def set_method(self, arg): 
    inst.attr = arg
```

```python
from types import MethodType
inst.set_method = MethodType(set_method, var)
```

也可以给class整体加一个方法：

```python
Class.set_method = set_method
```

也可以给class加一个类属性：

```python
Class.attr = var
```

## `__slots__`限制属性

> 一种写在类内部的声明，通过预先声明实例属性等对象并移除实例字典来节省内存。虽然这种技巧很流行，但想要用好却并不容易，最好是只保留在少数情况下采用，例如极耗内存的应用程序，并且其中包含大量实例。——Python Official Doc

那么如何限制属性呢？

在class里定义一个特殊变量：

`__slots__ = ('attr_1', "attr_2")`，这样就限制了能添加的属性名字。

**如果是只读变量，指加了下划线，那么在字符串里应该也加下划线。比如变量叫score，在`__init_`定义为`__score`,那在`__slots__`里也应该加下划线。**

> 这里用元组，因为用list会造成混乱

> 但是子类在继承时并不会继承这些属性的限制，除非子类在定义时也定义一个slots，这样会**在父类的基础上加上新的限制**；而如果不定义slots就完全没有限制。

如果赋予slots以外的属性会报错

https://wiki.python.org/moin/UsingSlots

slots本身是类的一个固有变量。如果正常情况下增加属性，这些属性会创建`__dict__`和`__weakref__`变量（dict这个动态变量导致可以随意增加属性），结果是：1. 访问速度慢；2. dict作为动态变量不安全。使用slots就不会创建dict和weakref。子类直接继承父类的话，如果不声明slots则还是会生成dict和weakref，所以没有属性限制。

而slots安全，访问速度更快（直接写到内存，比dict快），直接把属性名字写到类属性里。

## @property

> 前置要求：看python 装饰器

假如我要限制inst的attr的读写，可以定义get和set方法，典型例子如下：

```python
class Student(object):
    def __init__(self):
        self.__score = None

    def get_score(self):
        return self.__score

    def set_score(self, i):
        # check value
        if not isinstance(i, int):
            raise ValueError('int only, you fool')
        elif 0 <= i <= 100:
            pass
        else:
            raise ValueError('[0, 100] only, you fool')
        # set value
        self.__score = i


instA = Student()
instA.set_score(76)
print(instA.get_score())
```

这么写吧好是好，但是不够优雅，因为我们赋值或者读取，不能直接调用属性了，比如`inst.score`，只能使用方法，所以有没有什么解决方案呢？

python自带了装饰器`@property`和`@*.setter`，可以把method当attr用 / 把setter方法变成赋值。

比如：

```python
class Student(object):

    def __init__(self):
        self.__score = None

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, i):
        # check value
        if not isinstance(i, int):
            raise ValueError('int only, you fool')
        elif 0 <= i <= 100:
            pass
        else:
            raise ValueError('[0, 100] only, you fool')
        # set value
        self.__score = i


instA = Student()
instA.score = 76   # set score
print(instA.score) # get score
```

目前看来，有几个要注意的点：

1. 必须先写`@property`把一个方法变成属性，才能写`@attr.setter`，调换顺序不行；而且应该是先把某个method变成attr了，接下来才能写`@attr.setter`，不同名是不行的；
2. 这里不用担心两个函数重复名字的问题，方法都写成属性名字就行（不该加下划线）；
3. 现在在外部可以和之前一样赋值和读取了
4. `@property`和`@*.setter`都写是可读写，如果只写第一个就是只读
5. 假如是只读的，就不能给它赋值，包括在`__init__`里定义并初始化也不行
6. **属性和实例不能重名**

```python
    @property
    def score(self): 
        return self.score
```

仔细看，在之前的例子里属性是`__score`，这里是`score`，而且会报错。因为假如我在外部进行`inst.score`，在执行时会转化成赋值的方法，但是在return的时候的`self.score`又会调用这个方法，造成无限递归，最终导致栈溢出报错`RecursionError`。

一个含有读写、只读的例子：

```python
class Student(object):

    def __init__(self, k):
        self.value = k
       #self._value = k also OK
       #self.__value=k is OK, if replace _ with __ in 

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, i):
        # check value
        if not isinstance(i, int):
            raise ValueError('int only, you fool')
        elif 0 <= i <= 100:
            pass
        else:
            raise ValueError('[0, 100] only, you fool')
        # set value
        self._value = i

    @property
    def inv_value(self):
        return 100 - self._value


instA = Student(45)
print(instA.inv_value)
```

> **注意上面的例子中，`__init__`里和之前的不一样。因为这里的`self.value`实际上会调用setter方法，self实际拥有的属性也是`_value`**

## 多重继承

1. 有的时候代码中不得不让一个子类继承多个父类
2. 通常我们不希望代码中一个子类能找到多个父类
3. python中通过MixIn改善继承关系

例如说，汽车为父类，按内燃机和电动车分了子类，但是我又希望增加前驱、后驱、四驱的分类。

**第一种思路**：汽车为最大的父类，内燃机和电机是两个一级子类，二级子类有：前驱内燃机、后驱内燃机、四驱内燃机等。**这样不好**。如果我希望再按照A级、B级、C级车分类，这个树将会极其复杂。

**第二个思路**：最大父类：汽车，前驱，后驱，四驱。汽车往下是ICE和MOTOR，再往下是前驱内燃机、后驱内燃机、四驱内燃机等。其中这些子类**多重继承**，除了ICE或MOTOR，还会继承前、后、四驱。

**第三个思路**：第二个思路很好，但是我们不希望这么设计，因为我们希望一个单一继承的树，而不是乱七八糟的树。所以python有`MixIn`，意味着把一些class作为Mix In的功能，使得树简化。

`MixIn`的功能：给一个类增加多个功能的同时，保持继承树的单一。这样，在设计类的时候，我们优先考虑通过多重继承来组合多个`MixIn`的功能，而不是设计多层次的复杂的继承关系。

## 重载，用魔方方法定制类

### `__str__`, `__repr__`

当我们print(obj)的时候，返回的是`obj.__str__`。如果我们不提前定义，那么返回的可能是：

`<__main__.Auto object at 0x00000289E3335420>`

为了增加可读性，我们可以在类里定义一个：

```python
     def __str__(self):
        return f"{self.name} is Auto"
```

这样print的时候就好看多了。

`__str__`是面向用户的，即用户在控制台输入`print(obj)`即可返回友好的提示。

`__repr__`差不多，但是是面对开发者的。在控制台直接输入obj回车，也会返回：

`<__main__.Auto object at 0x00000289E3335420>`

为了增加可读性，我们在类里重构一下：

```python
    __repr__ = __str__
```

这样就更方便开发者。

此时`obj.__repr__`是一个和`__str__(self)`绑定的函数，`obj.__repr__()`是友好的提示。

### 把类用于迭代`__iter__`

> 重载`for x in`方法

在class里可定义方法`__iter(self)__`，并且该方法的返回对象必须是一个迭代器，即`return 迭代器`。这个方法只会调用一次，**该操作返回一个迭代对象，不必是self**。

如果在外部使用`for`循环，就会调用迭代对象（迭代器）所在的class里的`__next__`方法。因为有next方法的class才是个迭代器。

也就是说想让一个类迭代，必须要next和iter方法。

当然也可以分开，但似乎没什么意义。

```python
class IterMain(object):

    def __iter__(self):
        print('return an iterator')
        # global instA
        return K


class Iterator(object):
    def __init__(self, i):
        self.num = i

    def __next__(self):
        self.num = self.num + 1
        if self.num <= 10:
            return self.num
        else:
            raise StopIteration()


K = Iterator(0)
for instB in IterMain():
    print(instB)
```

另一个斐波那契数列的写法：

```python
class Fib(object):
    def __init__(self, j):
        """j is the limit of iterations"""
        self.a = 0
        self.b = 1
        self.limit = j
        self.cnt = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        self.cnt += 1
        if self.cnt <= self.limit:
            return self.a
        else:
            raise StopIteration()


for instA in Fib(10):
    print(instA)
```

这个程序会首先`instA = Fib(10)`，然后print的时候执行，首先返回一个迭代器（它本身），然后因为在for循环里所以会执行next，即迭代语句，直到数量限制。

> 但我感觉这个真的是奇技淫巧，想不到有什么实用之处

### `__getitem__`

重载`[]`运算符，可以让一个class像list、tuple一样允许遍历和切片（slice）。

比如一个自定义的deque类，用了这个可以像普通列表一样访问——记得区别int和slice：

```python
    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            return self.items[n]
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            return self.items[n.start:n.stop]
```

### `__setitem__`

重载`[]`运算符，可以让一个class像dict一样，通过`[]`设置k-v对。

```python
def __setitem__(self, k, v): 
    self.put(k, v)
```

### `__contains__`

重载`in`。

### `__getattr__`

正常情况下，当调用不存在的属性时会报错。但是我们可以这样定义，让class对特定的一些属性作出响应：

```python
    def __getattr__(self, attr): 
        if attr == 'score': 
            return stm
```

返回啥都行，变量，函数。

但是对于未考虑到的attr，为了也作出相应，可以这么写：

```python
    def __getattr__(self, attr): 
        if attr == 'score': 
            return something
        raise AttributeError('you fool')
```

### 链式调用

```python
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(eval("Chain().status.user.timeline.list"))
```

`/status/user/timeline/list`

因为每次返回的都是一个新的对象

```python
class Student(object):
    def __init__(self):
        self._score = None
        self._age = None
        self._name = None

    def set_name(self, name=''):
        self._name = name
        return self

    def set_age(self, age=18):
        self._age = age
        return self

    def set_score(self, score=100):
        self._score = score
        return self


instA = Student().set_name("Colin").set_age(25).set_score(10000)
```

### call 调用

在class里定义一个`__call__()`，即可把一个inst当func来用。甚至可以加一些args。

可用`callable()`函数，判断一个对象是否能被调用（是否可以被当作函数）。

## 枚举类

## MetaClass

## Super() 和 MRO

MRO: Method Resolution Order，主要相关的是在多继承时，调用方法到底调用的是哪个父类的方法。这是一种广度优先搜索。相对的是深度优先搜索 BFS。

![img](https://i.imgur.com/G3Gdnkf.png)

在上图中，箭头指向父类。如果有多个子类继承了同一个父类，那么这个父类则放在它能够出现的所有位置中最左的位置。

MRO是一个列表，满足原则：

1. 子类永远在父类前面；

2. 如果有多个父类，会根据它们在列表中的顺序被检查；

3. 如果对下一个类存在两个合法的选择，选择第一个父类；比如`A(B, C)`，选择B；

入度为0：没有箭头指向一个类。

在解析上图时，先找入度为0的类，并剪掉所有与之相连的箭头；两个符合条件的类，先整左边的。所以就能得到`[A, B, C, D, E, F, Object]`。

`class.__mro__`可知道这个类的MRO列表。

`super(class, obj)`，返回的是`obj`的MRO中`class`类的父类，**是一个类的对象**，其中`obj`一般是`self`；使用这个函数一般是要调用父类中的方法。

所以在说`super()`的时候要先提到MRO，否则在多继承情况下，我们不知道调用的是哪个父类中的方法。

# Python 异常处理

## ErrorClass

```python
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- EncodingWarning
           +-- ResourceWarning
```

## 错误处理机制

<img src="https://www.runoob.com/wp-content/uploads/2019/07/try_except_else_finally.png" style="zoom: 50%;" />

```PYTHON
try: 
    statements
except: SomeError as e:
     print(e.value) / print(e)
else: 
    print('yeah')
finally: 
    print("Job Complete")
```

- except 可以有多个，用来捕获多种异常；
- 所有的Error都继承自`BaseException`，并且Error之间也存在继承关系；
- 如果except后懒得处理，可以直接raise

## 错误记录log

```python
import logging
...
    except Exception as e:
        logging.exception(e)
```

*同样是出错，但程序打印完错误信息后会继续执行，并正常退出*

## raise

`raise SomeError(expression)`

假如except 一个ZeroDivisionError，可以raise一个ValueError

或者自定义的Error。

`class CustomError(ValueError): pass`

# Python 调试

1. print，很简单，但是debug后还得删掉;
2. `assert expression, 'string'`，如果expression判断为true则无事发生，判断为false则会raise `AssertionError: string`。启动Python解释器时可以用`-O`参数来关闭`assert`（字母O）
3. 使用`logging`

异常和报错是两个东西，异常是正常现象，可以手动提出异常。比如使用`raise`：

`raise ValueError("you fool")`

## 单元测试 unittest

第一个文件：写我们正在开发的程序；

第二个文件（测试用）： 

```python
import unittest
from program_file import func



class Testxxxxx(unittest.TestCase): 
    # 必须以Test开头才行
    def test_xxxxxxx(self): 
        self.assertEqual(func(a), res[, msg='fesfefe'])


if __name__ == '__main__':
    unittest.main()
    # (argv=['first-arg-ignored'], exit=Fals
```

如果运行正常，console会显示OK

每个要测试的函数写一个对应的的测试函数

除了`self.assertEuqal()`，还有很多：

# Python 杂的函数

- `eval()`，重新运算求出参数的内容；比如令a=1，eval('a')=1， 可以获得字符串里面的变量的值；

- `repr()`，给一个对象（具体内容，不是引用比如var1，a，str1）加上引号，成为字符串；

- `(obj == eval(repr(obj))) is True`

- `ord()`返回`chr`的ascii；

- `chr()`返回ascii对应的字符；
