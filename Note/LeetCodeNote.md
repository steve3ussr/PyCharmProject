也不知道该看啥，就做了 [leetcode cn的最火的一百题](https://leetcode-cn.com/problem-list/2cktkvj/) 。

# 1 two-sum 
给定一个整数数组 nums和一个整数目标值 target，
请你在该数组中找出 和为目标值 target的那两个整数，并返回它们的数组下标。
你可以按任意顺序返回答案。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

这题本身没什么难度，两次遍历就行，遇到符合条件的就return。但是这是一个时间复杂度为$O(n^2)$的方法，因为两次遍历需要$\frac{n(n+1)}{2}。

为了减小时间复杂度，我的想法是：
1. List - target/2, T(n) = n
2. abs(List), T(n) = 2n
3. sort, O(n) = O(nlogn), 比如归并，build-in sorted使用的Timsort
4. 对每个元素，判断它和下一个元素是否相同，return k, T(n) = 3n + T(sort) **问题一**
5. abs(i - target/2) = k, 对此能找到两个原始的i值;
6. 两次遍历分别查找对应两个i值的index, T(n) = 5n + T(sort)

问题一：假如输入列表中有两个3，但答案不是两个3，那这里有可能会返回3对应的值(5中提到)，查找index时就会报错；
       所以再后面做了校验，

看评论区里一个比较好的方法是用**Hash Table**，但是我不知道这是啥。尽管如此，我的运行时间也在最快的那一批里。
但Hashmap确实香。

# 2 addTwoNumbers

题目描述：



我觉得最大的问题是我已经忘了链表怎么操作了。

思路：
1. 正常情况下：l1 = l1.next
2. 如果l1是最后一个，那next之后就是None
3. 外循环用l1 l2是否为None判断是否结束
4. 如果l1已经是None，那在取值时就返回0

![](https://i.imgur.com/Lhsm4Wn.png)


# 3 lengthOfLongestSubstring

![](https://i.imgur.com/u98iTeq.png)

1. 用hashmap加快速度，减少一个O(n)；
2. win和start代表窗口长度和起始点
3. case1： 新元素不在map中，win++
4. case2：新元素在map中，查找map中重复元素的index
   - 在index >= start的情况下：
     - 减小win
     - 改变start
5. 这两个case必然改变win，在每次循环后取softmax
6. 这两个case之后必然改变map，不管是增加还是修改键值

# 4 findMedianSortedArrays

1. 问题转化为寻找第k小的元素，k>=1
2. 分三种exit情况：列表为空，或者k==1时返回第一个元素的最小值
3. 比较两个列表的第k//2个值，小的一方可排除前k//2个值
4. 3中有可能指针越界，但总的来说要让两个列表中待排除的元素数量a和b之和为k，所以让其中一个为最大值
5. 操他妈的，为什么python build in 的sort最快

# 5 longestPalindrome

![](https://i.imgur.com/N4pCh2H.png)

思路：

1. 从中心向两边推；
2. 记录两边一样的最大臂长
3. 注意：aba和abba是两种情况，因为中心不一定是整数
4. range只能生成整数数列

但是： 这样时间复杂度较大，空间复杂度小

改进：
1. 有left和right两个变量，条件合适的话分别外扩；
2. 对每个i，l，r init 分别为ii和ii+1，代表'aba'和'abba'两种情况

# 6 convert(Z形变换)

![](https://i.imgur.com/AsniBx9.png)

***这是我第一次不看答案就能写出来，而且首次提交就通过的题！*

思路：
1. 结果首先是一个列表，根据行数，分为多个空字符串；
2. k = 2r-2，因为这是一个周期；
3. 按照index的mod k来判断添加到哪个字符串里；
4. 假如r=4，则k=6，一个周期里的数字应该分别放到0,1,2,3,2,1个字符串里，通过判断改变值；
5. `str += v`可以拼接;
6. `''.join(list)`可以把列表里的字符串拼在一起

# 7 reverse

因为限制环境中只能有32位的数字，我的思路是：
1. 先把ans做成str，最后来个int，用try-except改变return的值；
2. 但是py里没有限制，所以用值来判断ans，改变输出——这样其实有问题

正确方法：
1. 通过简单的数学步骤，确定只要imin<=ans<=imax就行，简单的不等式变换；
2. `imin = min//10 + 1`;
3. `imax = max // 10`;

# 10 isMatch 正则匹配

从这个题开始，我才正式看了动态规划是什么，感觉动态规划可以解决很多复杂问题，但是想起来比较难。

动态规划 Dynamic Programming: 
1. 定义一个一维数组，或者二维数组，如`dp[i][j]`,赋予一个物理意义：，**最优解**；
2. 找到状态转移方程，比如`dp[i] = dp[i-1] + dp[i-2]`;
3. 给定边界条件，比如`dp[0] = 1`

对这个题来说，难点在于想到各种情况。

可以，也可以不做：把正则表达式里，带不带星号的拆分开，因为带星号和不带星号完全不一样；

我拆开了，因为这样比较好想后面的过程。

`dp[i][j] = bool`，i为字符串长度，j为正则表达式长度，这是物理意义。

1. 如果`p[j]`是普通的，不带星号的话，是`dp[i][j] = dp[i-1][j-1] and T/F`；
这个TF取决于`s[i]p[j]`是否一样； 
2. 如果`p[j]`是带星号的话：
   1. 比如`a, ab*`这种情况，因为`*`可以匹配0个字符，所以这时候是**无匹配**状态，`dp[i][j]=dp[i][j-1]`;
   2. 若果是`abbb,ab*`，属于**有匹配**状态，`dp[i][j]=dp[i-1][j]`;
   3. 上一条最终会变成`a, ab*`;
   4. 但这样有问题，比如`a, ab*a*`, 就会转移到`[], ab*`，最终为False；
   5. 所以应该加上一个`or dp[i][j]=dp[i][j-1]`，因为`a, ab*a*`和`a, ab*`的状态是一样的；
3. 初值的话，因为有i-1，j-1，所以ij定为字符串长度，设要查找的是`dp[m][n]`；
   1. `dp[0][0] == True`;
   2. `dp[0][any] == unkonwn`;
   3. `dp[any][0] == False`;不给正则相当于没法匹配；
   4. `dp[1,2...][1,2...] == Unkonwn`.
4. 循环的话，从m=0,1,2... n=1,2...循环，因为第一列已经确定了。
5. 如何确定是否匹配呢？这个应该能想出来。

难呐，真他妈难。

# 11 maxArea

第二次双指针问题，上一次是滑动窗口，但是我没学双指针。

双指针可分为三种：

1. 快慢指针，快的步进2，慢的步进1，相遇结束，感觉多用于链表；
2. 碰撞指针，左右指针从两头移动，相遇结束，常用于有序数组（但这个题无序也能用）；
   1. 如果是无序的，也可以先排序；
   2. 可以解决2数之和问题；
   3. 3数之和可以变成1个数，和2数之和问题；
3. 滑动窗口，一般是对窗口内的元素进行计算，比如字符串匹配。

思路：
1. 最大体积由左指针和右指针确定，其中一长一短；
2. 如果移动长的一个，那么由于水的高度由短板决定，所以：
   1. 双指针距离一定减小；
   2. 高度一定减小，可能为原先的短板，也可能是更短的；
3. 如果移动短的一个：
   1. 双指针距离一定减小；
   2. 高度可能不变，可能增长，可能减小；
4. 所以**唯一的可能性在移动短的一个**。

操作很简单，循环条件为指针不重合，比较体积。

# 15 threeSum 三数之和

双指针的思路是对的，但是缺少细节。

双指针解决两数之和twoSum：
1. sort排序先；
2. 左指针和右指针在两侧；
3. 求和，看和target的关系：
   1. 如果小于target，说明需要增大，移动左指针；
   2. 如果大于target，说明需要减小，移动右指针；
4. 循环条件：左指针小于右指针，**不是等于，因为偶数个数列会错过**。

解决三数之和threeSum：
1. 外层循环：固定第一个数；
2. 转化为twoSum；

需要注意的点：

1. 外层循环（第一个值）大于0就不用找了；
2. 第一个值和上一组符合条件的第一个数值一样也不用找了，会重复，比如[-3, -3, 1, 2]；
3. 双指针符合target的话，如果分别和第二个、第三个数值一样，continue，如[-3, 0， 0, 1, 2, 3， 3]，并且应该同时移动；
4. 其他的都是满足条件的。

# 17 letterCombinations

这个题没什么可以简化时间复杂度的方法，就是遍历，比如'23'对应O(3x3), '27'对应O(3x4)。

但是遍历也是要讲究方法的，这里用的叫回溯（backtrack）
2 -> abc
3 -> def
![](https://i.imgur.com/mT7S04z.png)

在这里维护一个字符串，如果到了最后一个节点，比如已经是'ad'了，就把'ad'添加到结果，然后回溯到上一个节点，变成'a'。

在这个过程中，字符串的变化是：
1. ''
2. 'a' (这里进入abc的循环,并且往更深处寻找)
3. 'ad' (进入def的循环)
4. 'a' (上一步中已经到头了，，添加到结果，回溯)
5. 'ae' 'a'
6. 'af' 'a'
7. '' (回溯到上一个节点)
8. 'b' 

TIPS：
- `itertools.product()` 可以用一行搞定这个问题； 
- `*` 的作用是拆包，比如`*tuple`
- 

# 19 removeNthFromEnd

要删除的节点有两种情况：
1. 在开头增加一个哑指针；
2. 直接返回head.next

具体的做法有：
1. 遍历两次，第一次找到要删除的index，第二次删除；
2. 遍历一次，但是双指针，先让一个指针在[0]，另一个指针[n-1]，当[n-1].next为None就删除慢指针；
3. 既然是倒数，那可以用stack；

我选择2

# 20 isValid

简单题，Stack

# 21 mergeTwoLists

合并两个正序链表：（非递减）

`1 -> 2 -> 2 -> 4`

# 239 maxSlidingWindow

## 方法一：维护一个最大二叉堆

> python自带了二叉堆，但是是最小堆

1. 将前k个元素buildHeap；
2. findMax；
3. 移动窗口，将新元素insert：
   1. 如果max不在窗口中：delMax；
   2. 如果max在窗口中，继续

移动窗口是$O(n)$，插入和删除都是$O(logn)$，所以总的来说是$O(nlogn)$。



## 方法二：单调队列（双端队列deque的一种）

假设现在的窗口为`[1, 2, 10, 3, 5, 7]`：

1. 假设list中后面的都是0，那么只要10还在，最大值就是10，所以前面的1和2其实没有用，可以不要；
2. 假设list中后面的都是0，并且移动到了`[3, 5, 7, 0, 0, 0]`，此时最大值是7，前面的3和5又没用了；
3. 假设下一个是11，那么`[2, 10, 3, 5, 7, 11]`，有了新的最大值，那么前面的都没用了；
4. 所以在最大值的左侧的都是没用的；
5. 那在最大值的右侧呢？也不是全都有用，比如第2点中提到的，在**最大值后面的部分中的最大值**的前面元素也没用；
6. 所以窗口中构成了一个单调递减的数列；
7. 如果两个相邻的元素相等，*那么其实可以只留下最后一个重复的（还没想清楚）*，这就构成了一个**严格单调递减**的序列；

假设我现在有了一个序列`[10, 8, 6]`：

1. 假如下一个数字是11：那应该把前面的都去掉，变成`[11]`；

2. 假如是9，那应该变成`[10, 9]`；

3. 假如是4，应该变成`[10, 8,  6,  4]`；

4. 思路：

   1. 比较这个newEle，和队伍末尾，如果newEle更大，就pop；

   2. 直到newEle比队伍末尾的要小，那就append；

      > 要在末尾pop和append



假设现在的窗口实际上是`[1, 2, 10, 3, 8, 6]`，但按照之前说的变成了`[10, 8, 6]`，那我怎么知道什么时候窗口离开10呢？

 1. 可以只储存index，val在比较的时候现查；

 2. 如果队首的index是`f`，实际窗口在`[i]`到`[i+k]`，只要`f >= i`就行，否则就得popleft

    > 要在开端pop

以上说的，非常适合用deque，两头都能进出。



## 感想

用自带的deque，比手动用list实现deque，或者自己写一个class Deque都要快得多。内置函数的优化真的强。

自己写的：

```python
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int):
        q = []
        ans = []

        def monoAppend(new):
            while q and nums[new] >= nums[q[-1]]:
                q.pop()
            q.append(new)

        for i in range(k):
            monoAppend(i)
        ans.append(nums[q[0]])

        for i in range(k, len(nums)):
            monoAppend(i)
            while q[0] < i-k+1:
                q.pop(0)
            ans.append(nums[q[0]])

        return ans

if __name__ == '__main__':
    test_list = [1, 3, 10, 4, 8, 6, 7, 8, 9, 0]
    res = Solution().maxSlidingWindow(test_list, 3)
    print(res)
```

用自带的py deque：

```python
import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = collections.deque()
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)

        ans = [nums[q[0]]]
        for i in range(k, n):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            while q[0] <= i - k:
                q.popleft()
            ans.append(nums[q[0]])

        return ans
```

# 697 findShortestSubArray

第一次遍历：创建一个dict，k: 数值，v:[出现次数，起始index，结束index]

第二次遍历，遍历dict，把次数变成负的，然后把[1]变成长度，[2]就pop掉

现在出现次数最多的，[0]是最小的负数
在这些出现次数做多的里面，[1] e.g. length 我们要的就是最小的
然后python min有特殊的性质，所以min(dict.values())[1]就是次数

正常应该是先找次数最多的，确定最大次数，再在次数最多的里面找长度最小的，但是用内置的min肯定更快















