# TODO

- P56，2.7.4，似乎是改动的快排；
- P67，3.3.7，表达式转换；

# 1 导论

## 1.4 Python基础

`range(a, b)`和`list[a:b]`差不多，都从a下标开始，但是不包括b下标。

# 2 算法分析

## 2.3 Python数据结构的性能

- `list = list  + [i]`比`list.append(i)`慢得多，连接比追加慢；
- `pop()`和`pop(i)`时间复杂度分别为1和n，即使是`pop(0)`也要慢很多；

![](https://i.imgur.com/rMbbmB7.png)

![](https://i.imgur.com/R5NNqpt.png)

# 3 基本数据结构

## 3.3 栈

- 栈具有反转特性；
- 在py里可以自定义一个类，用原生的list实现各种方法；
- ![](https://i.imgur.com/oIMIeme.png)

## 3.4 队列

- 和栈相反，先进先出，FIFO；
- 主要内容就是dequeue和enqueue；
- 可以用list实现；

![](https://i.imgur.com/RgCiE4I.png)

## 3.5 双端队列（deque）

- 像是stack和queue的结合，从两端都可以添加或者移除元素；
- add、remove和front、rear四种结合，以及查询个数和是否为空；
- 这里会涉及到`pop(0)`和`append(0, i)`，可以把这两种都放在前端，这样统一从后端比较快；

## 3.6.2 无序列表：链表

- 首先需要一个Node类，包括data和next两种属性；
- 重点在于Unorderlist类；
  - head用来保存head；
  - isEmpty看有没有节点；
  - add，添加到开头比较方便；
  - 遍历：
    - length
    - search
    - remove：需要双指针
    - append
    - insert
    - index
    - pop

### 3.6.3 有序列表

比如一些数字，它们会按照数字大小排列，而不是直接添加到开头——元素的位置取决于他们的特征。

# 4 Recursion

## 4.2 Introduction

**The Three Principles of Recursion**

以递归求数列的和为例：

1. 递归算法必须有基本情况（数列长度为1时返回）；
2. 递归算法必须改变其状态并向基本情况靠近（数列拆分为**首项**和**其余项**）；
3. 递归算法必须递归地调用自己（返回首项和**其余项的和**）。

## 4.3 Realization

递归通过**栈帧**来实现。

![](https://i.imgur.com/0gh20r1.png)

栈底部的将保留函数和使用的变量（局部变量作用域为该帧）；

栈顶计算的结果将一层层向下替换，直至栈空；

## 4.7 DP, GA

> DP: Dynamic Programming
>
> GA: Greedy Algorithm

例子：

有1、5、10、25美分的硬币，而我需要63美分，怎么才能让硬币数量最少呢？

GA：试图最大程度地解决问题，但这只是局部最优解。如果GA的话，需要2个25美分，1个10美分，3个1美分，暂时是全局最优；

但如果还有21美分的硬币，最优解是3个21美分硬币——这时候GA就不起作用了。

---

利用递归的思想：

> 1. 递归算法必须有基本情况（数列长度为1时返回）；
> 2. 递归算法必须改变其状态并向基本情况靠近（数列拆分为**首项**和**其余项**）；
> 3. 递归算法必须递归地调用自己（返回首项和**其余项的和**）。

1. 基本情况：当剩下的金额和某个硬币金额一样；
2. 多种靠近方式：
   1. 1美分+剩下的；
   2. 5美分+剩下的；
   3. 10美分+剩下的；
3. 递归：拆分成一个硬币剩下的金额；

> 但这有很大的问题：
>
> ![](https://i.imgur.com/yYDBYXJ.png)
>
> 重复调用的次数太多，比如16就出现了很多次

初始解法：

``` python
def calc_coins_recursion(self, val_list: list, charge: int):
    if charge in val_list:
        return 1
    else:
        return 1 + min(self.calc_coins_recursion(val_list, charge - x) for x in val_list if x < charge)
```

cache 解法，速度快了很多：

``` python
self.cache = dict()

def calc_coins_recursion_cache(self, val_list: list, charge: int):
    if _ := self.cache.get(charge):
        return _
    else:
        pass

    if charge in val_list:
        tmp = 1
    else:
        tmp = 1 + min(self.calc_coins_recursion_cache(val_list, charge - x) for x in val_list if x < charge)

    self.cache[charge] = tmp
    return tmp
```

dp解法：

``` python
    def dp_coins(self, val_list, change):
        # build
        for i in range(1, change+1):
            if i in val_list:
                self.dp[i] = 1
            else:
                self.dp[i] = min((self.dp[i-x] + 1 for x in val_list if x < i))

        return self.dp[change]
```

**DP是自下而上的，从初始值开始构建整个表格；虽然占用了一些空间用于储存，但是速度很快**

**递归是自上而下的，有可能会栈溢出**

# Search & Sort





# 6 树

## 6.3 术语和定义

![](https://i.imgur.com/I1tWzCs.png)

![](https://i.imgur.com/tLyO7QD.png)

![](https://i.imgur.com/WHa5qWx.png)

> - 边：两个节点的连线；
> - 节点也叫key；
> - 可用Root、Child、branch表示；

## 6.4 实现方法

### 6.4.1 list of list

> 不怎么用

- 基本结构：`[root value, [left branch], [right branch]]`

- 叶子：`[value, [], []]`

- 所以每一个节点要么是长度为3，要么是`[]`；

- 这个不仅可以二叉树，其他树也可以；

![](https://i.imgur.com/AgmtuoK.png)

- insert实际上只插入了一个节点；
- 假如 insert `val`时，原来的位置有棵树`oldTree`，那`insertLeft`会把这个位置变成`[val, oldTree, []]`；
- 

### 6.4.2 节点与引用

> 遵循面向对象，常用

![](https://i.imgur.com/FCsowYJ.png)

二叉树的每个子树都是二叉树。

## 6.5 二叉树应用

### 6.5.1 解析树

> 解析树：是语法分析结果的一种表现形式,通常以树状表示语言的语法结构。

`((7 + 3) ∗ (5 − 2)) ->`  

![](https://i.imgur.com/m7DoslL.png)

从一棵空树开始：

- 左括号：为当前节点加一个左子节点，并且下沉到该节点；
- 数字：当前节点key，并返回父节点；
- 操作符：当前节点key，添加右子节点，并且下沉到该节点；
- 右括号：返回父节点；

> 只能是正整数的加减乘除

**在这里，所有的父节点满足FILO，可以用栈回退节点。**

以`(1+2)`为例，push两次，pop三次，所以一开始应该把根节点，或者空节点push进去。

操作符如何使用：

- import operator
- dict: `'+': operator.add`

### 6.5.2 树的遍历

三种遍历：

- 前序遍历：先访问根节点，然后递归地前序遍历左子树，最后递归地前序遍历右子树。（`*+73-52`）
- 后序遍历：先递归地后序遍历右子树，然后递归地后序遍历左子树，最后访问根节点。（`25-37+*`）
- 中序遍历：先递归地中序遍历左子树，然后访问根节点，最后递归地中序遍历右子树。（`7+3*5-2`），可以还原原来的表达式

**也可以改成非递归，以中序为例：**

1. 找到最小节点，并把路径上的节点都 push ；
2. pop，print
   1. 如果存在右子树，把从右子节点，到右子树的最小节点的全都push；
   2. 如果不存在右子树，pass
   3. 循环
3. 



## 6.6 二叉堆实现优先队列

> Binary Heap
>
> **每个父节点都小于等于左右节点, 但是并不意味着左右节点有大小关系**

优先队列：和队列一样FIFO，但是队列中的元素是有优先级的，按照优先级IO。I的时候就要根据特征进行优先级排列。

可以用排序O(nlogn)和插入O(n)，但是更快的方法是**二叉堆——可实现O(logn)**。分为最小堆（最小的元素在队首）和最大堆（最大的元素在队首）。

### 6.6.2 基本方法及其实现

> 可以实现一个$O(nlogn)$的排序算法

![](https://i.imgur.com/mEaHewY.png)

![](https://i.imgur.com/T2TuuTQ.png)

为了保持O(logn)这样良好的性能，应该让左右子树大小差不多，而不是一边特别大一边特别小——维持树的平衡。

> - 满二叉树：每一层都是满的；
> - 完全二叉树（此处使用）：除了最后一层，其他都是满的；并且最后一层从左往右排列；

![](https://i.imgur.com/V0R7LwS.png)

完全二叉树的神奇性质：

- 不需要list of list / node and reference，可以用一个列表表示，因为——
- 对于深度为k的一层，有$2^{k-2}$个左节点，左节点都是偶数；右节点都是奇数；
- 其中左节点分别为：$2^{k-1},\ 2^{k-1}+2\times1,\ \cdots,\ 2^{k-1}+2\times(2^{k-2}-1)=2^k-1$;
- 深度为k-1的一层，一共有$2^{k-2}$个节点，分别为$2^{k-2},\ 2^{k-2}+1,\ \cdots,\ 2^{k-2}+2^{k-2}-1=2^{k-1}-1$；
- 不难发现这两层是2倍的映射关系；
- 所以如果一个列表从1开始index（**为了实现这点，可以让第堆顶元素为一个最小值，如果要添加的元素都大于0的话**），`[p]`的左节点为`[2p]`，右节点为`[2p+1]`；
- `[p]`的父节点为`[p//2]`；
- 以上的神奇性质使得二叉堆可以用一个列表表示；

**堆的有序性**：每个父节点都小于等于左右节点，但是并不意味着k层完全大于k-1层，比如上面那张图；

具体的实现：

#### insert $O(logn)$

为了保证是个完全二叉树，应该加到队伍末尾，但是可能会破坏堆的有序性，因此需要将其进行交换。假设一个父节点只有一个子节点（子节点 > 父节点），又加入了一个节点，那么可能会有新节点 < 父节点 < 子节点，因此应该让新节点当父节点：

![](https://i.imgur.com/t03TDgo.png)

可以用递归或者循环，感觉似乎没差别，但是没有验证；

#### delMin $O(logn)$

找到最小的很简单，难点在于如何重建。

为了维持完全二叉树的形态，应该把列表最后一个移动到堆顶；然后根据parent和child的关系不断移动这个元素。

- 如果parent小于两个childs，那就没问题；
- parent应该和两个child中最小的交换；
- **循环**：直到parent小于两个childs，终止；
- **交换**：在这个过程中，交换后要先确认一个childMin，再让childMin和parent交换。然后parent为childMin，两个child根据parent可计算出；
- **问题**：
  - 但如果parent在最后一层，child就会越界，就没法比较
  - parent为末尾节点的父节点，并且该父节点只有一个子节点，也就是single child；
  - 可以用一个minChild函数，判断存在几个child，并且返回相应的值；
- 如果堆里只有1个元素（不包括为了凑数的那个），应该直接执行，不然把最后一个元素放到堆顶的操作会有问题；

#### buildHeap $O(n)$

- [ ] 一种想法是一个一个insert（O(nlogn)）；

- [ ] 一种想法是既然这是个有序数组，可以用二分法（O(logn)）找到插入的位置，但是可能会导致其他元素都移动（O(n)）—— 这样总体为（O(nlogn)）；

- [x] 书上说可以做到O(n)，但是证明太复杂不考虑；

- [x] 我想可以用py自带的排序，底层优化还是快的，直接extend；

书上的方法：

1. 直接extend；
2. 所有父节点的index是从1到`len(new_list) // 2`，只要考虑移动这些父节点就行；
3. 从最后一个父节点开始往前遍历；
4. 如果父节点大于子节点，就向下一直移动，直到满足有序性；

> 这里向下交换以满足堆的有序性的过程和delMin一样，可以把switchDown抽出来；

> 相比switch down, 常用 perc down: percolate(过滤)

## 6.7 二叉搜索树

和二叉堆不一样，二叉搜索树的目的是为了实现二分查找，因此其各节点之间的关系和之前不一样：`childLeft < parent < childRight`。

<img src="https://i.imgur.com/lsjeDcc.png" style="zoom:33%;" />

### 基本代码

> 书中直接给出

在这里的`TreeNode`更加复杂，特点包括：

- payload：即键值对中的值；
- 显式储存的parent；
- 方法：
  - 是否有LR子节点，有的话返回；
  - isChild
  - isRoot
  - isLeaf
  - 几个children
  - 更换数据**但是不更换parent**

外部的BinarySearchTree：

- 包含一个迭代器`__iter__`==？==

### put——生成或插入节点

> `put, _put, __setitem__`

put：检查有没有根节点，没有的话就`TreeNode -> root`；

有的话，就要按其他方法搜索位置。私有的辅助函数`_put(self)`：

1. 从根节点开始，比较键，然后决定左右；
2. 如果左或右节点节点为空，说明有地方可以放；没地方的话就递归；
3. `new TreeNode()`，insert；
4. 如果key一样，就更新value

### get——获取value

> `get, _get, __getitem__, __contains__`

和之前的差不多。

注意：

- `get`获取值
- `_get`获取键所在的Node
- `__getitem__`重构`[]`，可通过`[k]`访问v
- `__contains__`重构`in`

### delete——删除节点

> `delete(), __delitem__(), remove()`

#### delete主函数

基本思路：

1. `_get`找到待删除的节点；
2. 找不到key就raise error；
3. 找到了就改变size，
   1. 如果这个节点是root，置None；
   2. remove函数

#### `__delitem__`

简单地调用delete

#### remove

三种情况，取决于这个node有几个children

##### case 1: no child

删除，并且让parent没有孩子

但是要分清LR，以此判断删除parent的哪个attr

##### case2: single child

让孩子替代待删除节点。

但是要分情况：待删除节点LR，因为要改变parent的LR；

孩子改parent就行

##### case3: both children

不太可能用其中一个子节点代替，所以要想别的方法。

能不能找到一个**后继元素**代替这个节点，同时保持二叉搜索树的特征呢？

可以用**左子树的最大节点**，或者**右子树的最小节点**来代替待删除节点。

这里可以分成三个部分：

1. `findMin`：对于一个TreeNode，返回以这个节点为根节点的子树中的最小键，也就是一直往左走；
2. `findSuccessor`：对于一个待删除的节点，找到右子树的最小键，作为`succ`后继节点返回；（*这个函数里有别的condition分支，还有其他用途*）
3. `spliceOut`：删除`succ`并重建联系，这里如果递归调用`delete`会慢。**该函数适合`findMin`和`findMax`**，因为`succ`的位置是比较明确的（对于删除操作）。

![Imgur](https://i.imgur.com/Yiv89Qn.jpg)

## 6.8 平衡搜索树 AVL

### 6.8.1 概述

构建BST的时候，有可能构建出一个全是左子节点的树，相比于左右完全平衡的树，各项操作会从$O(logn)$变成$O(n)$，因为时间复杂度取决于树的深度。

AVL树是一种自动保持左右平衡的树，通过记录每个节点的平衡因子（balance factor）来保持平衡。

> 和红黑树不一样，据说红黑树更好。

平衡因子：左右子树高度之差：

- 为-1、0和1的时候都可以算平衡；
- 如果大于0就是左倾，左边更深；
- 小于0是右倾，右边更深；

![](https://i.imgur.com/k100SuI.jpg)

这个近似于斐波那契数列，而斐波那契数列两项之比趋近于$\displaystyle\frac{1+\sqrt5}{2}$...略去数学过程，可得：$h=1.44\log_2{N_h}$。

### 6.8.2 AVL实现

#### 插入 put set

在NodeTree新增属性`balanceFactor`，新class继承自`BinarySearchTree`。

平衡因子：左边高度减去右边高度。

put：overload，需要在插入的同时更新所有父节点的平衡因子。向上更新的过程中：

1. 如果一个平衡因子被变成了0，那就不会再影响上面的父节点；
2. 到了根节点，停止；
3. 如果一个节点的平衡因子不是-1、0或者1，就进行**再平衡**;

#### 再平衡 rebalance

##### 左旋实现

<img src="https://i.imgur.com/34VIKkB.png" style="zoom:50%;" />

<img src="https://i.imgur.com/WqcQ9eA.png" style="zoom:50%;" />

具体的重建connection可分为三部分：

1. `newRoot`，和`oldRoot.parent`的连接；
2. 把节点`3`和`oldRoot`连接；
3. 把`oldRoot`和`newRoot`重建连接；
4. 重新计算父节点的平衡因子：
   1. 旋转前后，非父节点的高度是不变的，因此首先把两个父节点的平衡因子用非父节点的高度表示；
   2. 写出旋转后父节点的平衡因子（用同样的非父节点的高度表示）；
   3. 对于每个节点，计算其前后变化；
   4. 能用到的数学：$\max(x,\ y)=-\min(-x,\ -y)$，$\max(x,\ y)-a=\max(x-a,\ y-a)$；

##### 右旋实现

<img src="https://i.imgur.com/coTBdlL.png" style="zoom:50%;" />

类似左旋

##### 旋转的时机

一个怎么左旋右旋都不行的例子：

![](https://i.imgur.com/RcqxP2f.png)

>  要解决这种问题，必须遵循以下规则：
> 
> - 如果子树需要左旋，首先检查右子树的平衡因子。如果右子树左倾，就对右子树做一次右旋，再围绕原节点做一次左旋；
> - 如果子树需要右旋，首先检查左子树的平衡因子。如果左子树右倾，就对左子树做一次左旋，再围绕原节点做一次右旋；
> - **如果右倾，就让右边的更加右倾；如果左倾，就让左边的更加左倾；**

![](https://i.imgur.com/9Vq9oE3.png)

#### delete

1. 如果是 leaf ，那就没事：更新向上的父节点 balance factor，必要的时候 rebalance；
2. 如果不是leaf：找 succ 替代，并重建 succ 附近的连接（`TreeNode.spliceOut`）；
3. 从 succ 的父节点开始向上更新；

