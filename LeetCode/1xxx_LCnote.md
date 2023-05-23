# 1xxx_LCnote

> LeetCode笔记：id号2000-3000的题目



## [1015. 可被 K 整除的最小整数](https://leetcode.cn/problems/smallest-integer-divisible-by-k/)

就是判断余数，从1，11往下。

- 判断余数：可以只判断（前一个余数*10+1）的余数
- 只用判断k个，因为只有k种可能的余数：
  - 如果碰到0，可以返回
  - 如果是一个未见过的余数，储存起来
  - 如果是见过的相同的余数，说明是循环，return -1

## [1016. 子串能表示从 1 到 N 数字的二进制串](https://leetcode.cn/problems/binary-string-with-substrings-representing-1-to-n/)

==TODO==



## [1017. 负二进制转换](https://leetcode.cn/problems/convert-to-base-2/)

其实没有太多技巧，就是不断除 -2 ......我总是想太多。

商其实无所谓，但余数必须保证 0 或 1，因此要调整商。



## [1019. 链表中的下一个更大节点](https://leetcode.cn/problems/next-greater-node-in-linked-list/)

> 经典**单调栈**题目：构建一个单调的栈

这个题目要求是，顺序遍历，构建一个单调递减（不严格，可以相等）的栈。如果遍历到某个元素大于栈顶，则说明栈里某几个元素找到了 *下一个最大值*。将这些出栈后，需要将当前元素入栈。

遍历到某个元素时，有几种情况：

1. 栈空的，需要push当前元素；
   1. 栈不空，并且当前元素小于等于栈顶，需要push当前元素；
   2. 栈不空，并且当前元素大于栈顶，需要：
      - 循环，pop，直到栈空，或者当前元素小于等于栈顶
      - 将当前元素push

可以发现不管怎样都要将当前元素入栈。所以简化：

```
if 栈不空 and 当前元素大于栈顶:
	while 栈不空 and 当前元素大于栈顶:
		stack.pop()

stack.push()
```

但是要求返回结果，就要有一个记录结果的list。在每次遍历时默认`res.append(0)`。

 此外，在遍历列表的时候应该加一个计数器，统计当前序号。

> 一种错误的想法是，在链表遍历到下标 i 的时候，需要出栈；此时用另一个计数器统计出栈的个数，`res[i-0-1]，res[i-j-1]`这样。

可以在栈中同时记录入栈元素的值和下标。

也可以用另一个栈单独记录，两个栈同时 push pop。

> 在 Python 中，似乎一个栈储存（值，下标）这个元组消耗内存更大。



## [1023. 驼峰式匹配](https://leetcode.cn/problems/camelcase-matching/)

![](https://i.imgur.com/YTLaion.png)

我选择对于`pat`的每一个作为主循环，逻辑还好写，但是代码比较长；

答案是用`query`做主循环。

## [1026. 节点与其祖先之间的最大差值](https://leetcode.cn/problems/maximum-difference-between-node-and-ancestor/)

==TODO==

## [1039. #DP #DFS #递归 #记忆化搜索 多边形三角剖分的最低得分](https://leetcode.cn/problems/minimum-score-triangulation-of-polygon/)

![](https://i.imgur.com/rUYKDBm.png)

> 学习教程：[区间 DP：最长回文子序列 最优三角剖分【基础算法精讲 22】](https://www.bilibili.com/video/BV1Gs4y1E7EU)
>
> 主要在于这个思想：不要想着怎么划分三角形，而是要先想到**分而治之**，用递归，再把递归改成动态规划。如下图所示：
>
> ![](https://i.imgur.com/nQAtjSN.png)

### 递归

按照上图：

1. 定义一个递归函数`dfs(i, j)`，含义是以 `i-j` 下标为一条边的多边形，多边形的其他顶点在 i 顺时针 到 j 中；
2. 定义顺时针为方向；
3. 这个函数中枚举夹在中间的 k ，`dfs(i,j) = dfs(i,k) + dfs(k,j) + v[i] * v[j] * v[k]`
4. 对于上一步中的循环，取其中最小值
5. 递归
6. 递归退出条件：题中说了数据长度至少为 3，也就是退出条件可以定义为两个参数相邻；
7. 递归返回的值：`dfs(0, len(values)-1)`

```python
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:

        @cache
        def dfs(i, j):
            if j - 1 - i == 0:
                return 0
            min_value = inf

            for k in range(i + 1, j):
                min_value = min(min_value, dfs(i, k) + dfs(k, j) + values[i] * values[j] * values[k])
            return min_value


        return dfs(0, len(values)-1)
```

> 在这个过程中，会有很多重复求解的函数，所以加入`@cache`可以实现记忆化搜索，加快速度。



### 动态规划

**根据递归，改成动态规划。**

1. `dp[i][j] = dfs(i,j)`，含义是一样的
2. DP 递推公式：`dp[i][j] = max(dp[i][k] + dp[k][j] + [i][j][k]), i+1 <= k <= j`
3. 思考循环方式：
   1. `[i][j]`的状态由`[i][k]`转移，所以 j 正向循环
   2. `[i][j]`也由`[k][j]`转移，所以 i 逆向循环
4. 第一层循环 i 起始条件应该为倒数第三个；第二层循环 j 起始条件应为倒数第一个；第三层循环 k 为 i 和 j 之间的正向循环



```python
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:

        n = len(values)
        dp = [[0]*n for _ in range(n)]

        for i in range(n-3, -1, -1):
            for j in range(i+2, n):
                res = inf
                for k in range(i+1, j):
                    res = min(res, dp[i][k] + dp[k][j] + values[i]*values[j]*values[k])
                dp[i][j] = res

        return dp[0][n-1]
```





## [1040. 移动石子直到连续 II](https://leetcode.cn/problems/moving-stones-until-consecutive-ii/)

==TODO==

## [1041. 困于环中的机器人](https://leetcode.cn/problems/robot-bounded-in-circle/)

代码很简单，关键是思考**总结果**：

- 回到原点：这时不同朝向就相当于总的结果是原地转圈，总会回到起始状态（面朝北）;
- 不在原点：
  - 如果朝北：越走越远；
  - 其他方向：经过二次/四次一定回到起始方向

## [1042. 不邻接植花](https://leetcode.cn/problems/flower-planting-with-no-adjacent/)

这是一个图的题，但是没那么难。

![](https://i.imgur.com/ZB2lZcU.png)

1. 建立顶点之间的连接，没时间造轮子，直接用 adjacent graph;
2. 遍历每个顶点，在每个顶点里再遍历相邻顶点的颜色;
3. 去掉重复的颜色，在剩下的颜色里选一个，给当前顶点上色。



## [1043. 分隔数组以得到最大和](https://leetcode.cn/problems/partition-array-for-maximum-sum/)

这个题一看就是，比较复杂，应该用分治思想来解决。

### 第一步：递归

假设存在一个函数`func(list)`，递归运算这个函数，在这其中利用分治思想，返回一个最大值：

1. 定义结束条件：如果list长度小于等于k，那就不需要分治，直接返回长度 x 最大值；
2. 定义递归公式：
   1. 将list分成两部分，在循环中使得一侧的长度依次为1，2....k
   2. 循环控制的一侧（可能是较小的一侧），直接计算最大值
   3. 循环控制的另一侧，递归调用函数
   4. 在循环中，更新一个最大值
3. 返回最大值

> 这一步虽然能运行，但是超时了。单纯递归必然超时，必须结合记忆化搜索，避免重复计算函数才行。

### 第二步：递归+记忆化搜索

我们必须把上一步的函数参数：列表，改成hashable的参数。比如我可以用`func(i)`代表列表的前`i`个元素计算结果。

将第一步代码改写，结合记忆化搜索，可以成功提交。

### 第三步：递归 -> 动态规划

递归都能改成动态规划。

把递归函数`func(i)`改写成`dp[i]`数组，内容一样。`dp[0] = 0`。

先把初始条件写了，包括：

1. `dp[0] = 0`
2. `dp[i<=k] = i * max(list[:i])`

状态转移公式和之前的一样，循环取最大值。



### 第四步：动态规划，但是减少空间复杂度

注意到动态规划中，在第二层循环的循环个数只有 k 个，所以可以减少 dp 数组长度。

> 有点难，放弃，懒得想。

## [1054. 距离相等的条形码](https://leetcode.cn/problems/distant-barcodes/)

==TODO==



## [1072. 按列翻转得到最大值等行数](https://leetcode.cn/problems/flip-columns-for-maximum-number-of-equal-rows/)

> 可能是一个智商测试题。

如果若干个行，经过列反转后一样，则可能有两种情况：



```
1 1 1 1       1 1 1 1
1 1 1 1  -->  0 0 0 0  -->  这些行之间只有两种，是相反的
0 0 0 0       0 0 0 0 

1 0 1 1       1 1 1 1
1 0 1 1  -->  1 1 1 
0 1 0 0 

```



## [1079. 活字印刷](https://leetcode.cn/problems/letter-tile-possibilities/)

### 难点1: 想到这是DP

假如有一个 `AABCC`，要组成长度为5的字符串，该怎么做呢？

一种分治的思想是，先在5个位置上填充2个C，这样问题就变成了剩下的'AAB'如何填充长度为3的序列。

### 难点2：实现DP

函数的输入，告诉了我们有几种元素，每种元素出现的个数。所以可以用Counter统计。

`dp[i][j]`的定义：前`i`种元素，构成长度为`j`的字符串，有多少种可能。而递推公式可以看出，只和`dp[i-1][]`有关。

假设第i种元素有`c`个，并且我们可以选中其中的若干个（使用的定义为k），`dp[i][j] = dp[i-1][j-k] * C^k_j`

```
0 <= k <= c
j-k >= 0, k <= j
0 <= k <= min(c, j)
```

### 难点3：DP边界和数学基础

大C(combination)函数，`math.comb(n, k)`，代表了无顺序，从n个元素中选择k个元素的可能性。

```
C(n, 0) = 1, C(0, 0) = 1

C(0, n) = 0
```

将DP定义为`[1+种类][1+总长度]`的二维数组。初始值全为0，因为在长度不够的情况下就是0；对于`dp[i][0] = 1`，这是数学定义。

### dp写法

``` python
cnt = Counter(tiles).values()
max_div = len(cnt)
max_len = len(tiles)

dp = [[0] * (1+max_len) for _ in range(1+max_div)]
dp[0][0] = 1
curr_len = 0
for i, v in enumerate(cnt, 1):
    curr_len += v
    dp[i][0] = 1
    for j in range(1, curr_len+1):
        for k in range(min(v, j)+1):
            dp[i][j] += dp[i-1][j-k] * comb(j, k)
            
return sum(dp[-1][1:])

```

### DP空间优化

递推公式里，只和`dp[i-1][j]`有关，因此可以减少一层

``` python
cnt = Counter(tiles).values()
max_div = len(cnt)
max_len = len(tiles)

dp = [0] * (1+max_len)

curr_len = 0
for v in cnt:
    curr_len += v
    dp[0] = 1
    for j in range(curr_len, 0, -1):
        for k in range(1, min(v, j)+1):
            dp[i][j] += dp[i-1][j-k] * comb(j, k)
            
return sum(dp[1:])

```

## [1090. 受标签影响的最大值](https://leetcode.cn/problems/largest-values-from-labels/)

思想：GA，按照values大小，选择值作为答案。如果选择了某个值，就给label使用次数+1，使用次数达到限制就跳过。

创造一个index list，根据values[i]排序，根据排序后的index，values[index]就是从大到小的顺序，labels[index] 就是对应的tag。

``` python
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        dict_label_counter = {_: 0 for _ in labels}
        index = list(range(len(values)))
        index.sort(key=lambda x: -values[x])

        res = 0
        cnt = 0

        for i in index:
            if dict_label_counter[labels[i]] < useLimit:
                cnt += 1
                dict_label_counter[labels[i]] += 1
                res += values[i]

            if cnt == numWanted:
                return res
        return res
```







## [1335. 工作计划的最低难度](https://leetcode.cn/problems/minimum-difficulty-of-a-job-schedule/)

- 如果任务数量和天数一样，返回总和
- 如果天数为 1，返回最大值

### Recursion

比较容易想，i 天做完 j 个任务，可以转化为 i-1 天做完 j-k 个，再加上这 k 个任务中的最大值。

递归的停止条件是：如果 i == j，就返回这些任务的和。

这里应该满足：

- j-k >= i-1, k <= j+1-i
- k >= 1

在循环 k 的过程中，不断更新这 k 个任务的最大值。

### DP, 2dimension

把递归改成dp，很容易。建议是`dp[day][task]`，因为可以让`dp[0] = max_accumulate`

### DP, 1dimension

注意到 `dp[i][j]`只由`dp[i-1][j-k]`转移而来，所以可以变成`dp[j]`。

- i 正向循环
- j 逆向循环
- 每个`dp[j]`从 inf 开始重新计算
- k 逆向循环

### mono



## [1147. 段式回文](https://leetcode.cn/problems/longest-chunked-palindrome-decomposition/)

![](https://i.imgur.com/UrWfAaP.png)

可以用双指针，但是也可以不用——不用双指针就是写起来方便一些。

```python
class Solution:
    def longestDecomposition(self, text: str) -> int:
        res = 1  # 初始值

        while True:

            if len(text) <= 1:  # 退出条件
                break
            
            match = 0  # 是否在首尾匹配到有回文字符串
            for i in range(len(text) // 2):  # 左指针不超过中间

                if text[i] == text[-1] and text[:i + 1] == text[-i - 1:]:  # 匹配到了
                    match = 1
                    text = text[i + 1:-i - 1]
                    res += 2 if len(text) else 1

                    break

            if not match:
                break

        return res
```

## [1187. 使数组严格递增](https://leetcode.cn/problems/make-array-strictly-increasing/)

==TODO==







## [1330. 翻转子数组得到最大的数组值](https://leetcode.cn/problems/reverse-subarray-to-maximize-array-value/)

==TODO==



