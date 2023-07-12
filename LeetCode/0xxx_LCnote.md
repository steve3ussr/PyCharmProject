## [15. 三数之和](https://leetcode.cn/problems/3sum/)

双指针的思路是对的，但是缺少细节。

最内层循环，建议使用双指针来操作。

以下思路可以解决本题，还可以解决[18. 四数之和](https://leetcode.cn/problems/4sum)等问题。

1. 除了最里面两层用双指针，剩下的都是普通循环
2. 为了避免出现重复答案，要进行剪枝操作
3. 普通循环剪枝：
   1. 和上1次循环的数字相同，continue
   2. 往后面连续几个元素相加（和最小的情况），> target，说明应该break
   3. 当前元素，加上序列末尾的几个元素（和最大的情况），< target，说明应该continue
4. 双指针：
   1. 小于或者大于target，移动指针
   2. 如果等于的话，添加到答案里
   3. 双指针的剪枝：为了避免出现重复元素，例如`[-4, 1, 1, 1, 2, 2, 3, 3, 3]`，应该让两个指针移动到不等于当前元素的位置。例如当前指针分别是1，-1，则应该都移动到指向2的位置。

## [19. 删除链表的倒数第 N 个结点](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/)

让快指针先走n步，再两个一起走。

这样的话，快指针停下的时候，慢指针指向prev。



## [24. 两两交换链表中的节点](https://leetcode.cn/problems/swap-nodes-in-pairs/)

没什么难的，prev, curr, curr.next之间交换的问题。



## [27. 移除元素](https://leetcode.cn/problems/remove-element/)

双指针问题。

![](https://code-thinking.cdn.bcebos.com/gifs/27.%E7%A7%BB%E9%99%A4%E5%85%83%E7%B4%A0-%E5%8F%8C%E6%8C%87%E9%92%88%E6%B3%95.gif)

- 如果传统的移除元素，这需要O(n2)
- 快指针表示当前遍历到原始数组的哪个位置
- 慢指针表示在**移除元素**后的数组里，快指针所在的元素应该在什么位置。



## [28. 找出字符串中第一个匹配项的下标](https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/)

可用的解法：

1. 暴力解法，O(m x n)
2. import re，你就说开发效率高不高吧
3. 典中典之KMP，O(m+n)
4. 非典中典之sunny == TODO ==

### KMP

> 参考文献：
>
> 

#### 思路

传统的暴力解法，如果target和pattern匹配不上，那target的指针就向后移动一位。这个过程中会损失信息，比如下例：

``` 
a a b a a  b  a a f
a a b a a *f*
```

如果匹配到b-f后，target就从index 1再开始，是低效的，因为两个字符串实际上都匹配过aab——所以可以target指向b，pattern指向b后面的a，继续匹配。

为了达成这个，就需要看一看pattern中有多少自相重复的部分。

定义前缀：`a, aa, aab, aaba, aabaa`，是不包含最后一个字符的其他序列

定义后缀：`f, af, aaf, baaf, abaaf`，就这个意思。

定义前缀表`next`：`next[x]`代表从`pattern[0]`到`pattern[x-1]`的序列，公共子序列的长度。比如`next[5]=2`。

```
a a b a a f
0 1 0 1 2 0
```

需要这个东西是因为，假如在 f 发现不匹配，就看 f 前面的序列中最长的公共前后缀，然后跳转位置。f 前面最长的是a 对应的 2——2是长度（aa），也是跳转的下标。

#### 前缀表求解

思路是这样的：如果已知`next[0] .. next[x-1]`，如何求解`next[x]`?

如果`list[x] == list[next[x-1]]`，说明形成了一个公共前后缀，数值+1，例如：

```
a a b a a b
0 1 0 1 2 ?

list[5] == list[next[5-1]] == list[2], ? = list[2]+1 = 3
```

如果不相等呢？

我们还是需要减少重复匹配。

``` 
a a f a c a a f a f
0 1 0 1 0 1 2 3 4 ?   f != c

(aafa) c (aafa) f
  A         B
```

我们希望AB这两个子序列能有公共前后缀，这样就不用重新匹配。事实上，f 前一位的 next数值表示前面存在两个一摸一样的序列（A和B）。

如果再去找A的最长子序列，发现是1。所以是

```
(aafa) c (aafa) f
 !           !
```

找到重复的元素了，所以对于next[f]，最长的公共前后缀是af。

---

初始化：第一位没有意义，因为按照前缀后缀定义，第一位没有前后缀。第一个求解的下标从 1 开始。

now表示下一个要对比的元素/在next[x]之前的序列的最大长度。

``` python
def get_next(pattern):
    next = [0]
    x = 1
    now = next[x-1]
    
    while x < len(pattern):
        if pattern[x] == pattern[now]:
            next.append(now+1)
            now += 1
            x += 1
            
        elif now:  # now > 0
            now = next[now-1]
            
        else:
            next.append(0)
            x += 1
    return next
```

#### 主匹配过程

> 设主串名为text，子串为pattern，这里同样需要i和j指针，i对应主串位置初始为0，j对应字串位置初始为0，同时对主串和字串进行遍历操作，分为以下两种情况。
>
> 1.当text[i] == pattern[j]，i与j加一继续相同判断直到j到达pattern末尾匹配完毕，返回i - j，程序结束。
>
> 2.当text[i] != pattern[j]，此时需要用到next数组，j-1并查找对应next数组值，回退到该值位置，重新进行判断，相同则继续遍历直到j遍历到末尾，不相同继续回退到next[j-1]位置，这里需要留意，如果此时j = 0且两字符不相等，我们需要跳过当前text[i]再执行上述判断，如果i到达末尾说明text里面不包含pattern子串，返回-1，结束程序。

两个指针分别指向两个字符串。指向target的指针可以一次性循环到头，只需要根据前缀表，变化 pattern 指针（**i**）。在这个过程中，有几种情况：

1. i = 0，这时候匹配正常，就前进；不正常也不能回退（因为我们的next[0] = 0）
2. i > 0，匹配正常前进；匹配不正常就回退，直到 i=0，或者匹配上了
3. i = length(pattern)可以返回

所以循环里的逻辑有几种：

1. 应该回退的时候尽量回退，**直到不能回退或者匹配成功（所以这个逻辑必须放在2前面）**
2. 判断当前能不能匹配上，能的话就前进
3. 是否pattern全匹配完了（这个逻辑看起来可以放在最前面，也可以放在最后面，总之应该紧挨着2——但如果完全匹配的时候，两个指针都指向末尾，比如aaab & aab；这时候 指向主字符串的指针不会再前进，不会再循环，也就不会再经过这个逻辑。所以应该放在循环末尾）

如果循环里没有return，那就return -1



## [34. 在排序数组中查找元素的第一个和最后一个位置](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/)

重要的参考文献：[【二分查找【基础算法精讲 04】](https://www.bilibili.com/video/BV1AP41137w7)

```python
if nums[mid] < target:
	lo = mid + 1
elif nums[mid] > target:
	hi = mid - 1
```

这个二分查找意味着，有两件事情是不变的：

- `nums[lo-1] < target`
- `nums[hi+1] > target`

对于这个问题，寻找左边界的时候需要hi尽可能往左移动，所以要[mid]>=target；寻找右边界的时候差不多。

最终情况：lo=mid=hi

一下内容用寻找左边界示范：







## [35. 搜索插入位置](https://leetcode.cn/problems/search-insert-position/)

仔细想一想，最后应该return left。



## [59. 螺旋矩阵 II](https://leetcode.cn/problems/spiral-matrix-ii/)

核心是找个例子多想。

另外要保持左闭右开，或者其他原则，不能总变，如图所示：

![](https://code-thinking-1253855093.file.myqcloud.com/pics/20220922102236.png)



## [69. x 的平方根 ](https://leetcode.cn/problems/sqrtx/)

老套路，需要找到最大的，小于等于目标值的一个值。



## [76. 最小覆盖子串](https://leetcode.cn/problems/minimum-window-substring/)

有点难。这个题的本质是找一个最短的子序列。通常的套路是：

```python
lo = 0
for hi, v_hi in enumerate(data):
    v_hi 加入窗口
    while 满足条件：
    	缩短前指针
        更新结果
    
```

```
lo = 0
for hi, v_hi in enumerate(data):
    v_hi 加入窗口
    
    flag = False
    while 满足条件：
    	flag = True
    	缩短前指针
    	
    更新结果 if flag
    
```

对这道题来说，可以这样做：

- 缩短前指针的条件是：`hashmap[s[lo]]`的数量比要求的多，移除多余的元素。
- 在循环一开始加入的时候，判断一下新加入的元素是否在需求之内——当前窗口，能cover住多少需求
- 如果刚好能满足需求，说明这是一个局部最优解，才能更新答案

## [142. 环形链表 II](https://leetcode.cn/problems/linked-list-cycle-ii/)

参考文献：[代码随想录——环形列表II ](https://www.programmercarl.com/0142.%E7%8E%AF%E5%BD%A2%E9%93%BE%E8%A1%A8II.html#%E6%80%9D%E8%B7%AF)

第一种想法，用空间换时间，通过记录所有访问过的节点，找到相交的点。

第二种想法，相对复杂一些：

- 快慢指针，相遇的节点记录一下；
- 相遇的节点和头节点同时向后遍历，相遇的点就是相交点。
- 具体过程和数学证明见参考文献。
- 虽然空间复杂度为O(1)，时间复杂度也一样，但是可能花费时间要长一些。

## [202. 快乐数](https://leetcode.cn/problems/happy-number/)

比较简单。快乐数的计算应该用`%//`计算。





## [203. 移除链表元素](https://leetcode.cn/problems/remove-linked-list-elements/)

需要两个指针，一个last，一个curr。

但对于第一个元素，没有last，所以可以创建一个fake head ListNode对象，增加一个head。

curr一直遍历：

- curr值不等于目标：curr移动到下一个，last移动到下一个
- curr值等于目标，需要被移除：last.next指向curr.next，last本身不动；curr移动到下一个



## [206. 反转链表](https://leetcode.cn/problems/reverse-linked-list/)

增加一个fake head

用三个指针来改变



## [209. 长度最小的子数组](https://leetcode.cn/problems/minimum-size-subarray-sum/)

滑动窗口。

- 当前长度够，就更新长度，把低指针向前移动
- 当前长度不够，就gao



## [239. 滑动窗口最大值](https://leetcode.cn/problems/sliding-window-maximum/)

关键是如何获得窗口内的最大值。我想到了最大堆，但是如果窗口里的最大值在移动的过程中出去了，最大堆好像很难移除离开窗口元素。

考虑到这一点：`[1,2,3,0,0]`这个窗口，在移动前两次的过程中，和前面的12没有关系，因为这里的最大值是3。

窗口的每一个数，他前面比他小的数字都不可能是最大值——所以可以构建一个（非严格）单调递减的序列，这就需要这个序列满足：

1. 窗口移动新增一个元素时，像stack一样移除序列里比他小的元素，再新增元素；
2. 窗口移动减少一个元素时，检查序列开头index越界的元素，pop from front；

以上这两点，可以用deque来实现。



## [283. 移动零](https://leetcode.cn/problems/move-zeroes/)

![](https://pic.leetcode-cn.com/36d1ac5d689101cbf9947465e94753c626eab7fcb736ae2175f5d87ebc85fdf0-283_2.gif)

相比之下多了个交换的过程。重点在于理解性质。

## [300. 最长递增子序列](https://leetcode.cn/problems/longest-increasing-subsequence/)

### 普通思路

定义dp[i]为，以nums[i]结尾的最长子序列长度。

初始值为1，就是假设前面的元素都比nums[i]大。

对dp[i]来说，dp[i] = dp[j]+1，其中j为i前面的元素：

- 并且nums[j]<nums[i]，那就加1，也就是说组成了一个更长的递增子序列——这一步得去最大值
- 不然就什么都不干，因为不能组成更长的

当然，得取最大的dp[j]

### [高级思路](https://www.bilibili.com/video/BV1ub411Q7sB?t=356.5)

交换DP的值和下标：

- dp[i]代表以nums[i]结尾的最长子序列长度值
- g[i]代表长度为i的子序列，最小的末位值

```
data = [1,6,7,2,4,5,3]
1, res = [1]
6, res = [1,6]
7, res = [1,6,7]
2, res = [1,2,7]
4, res = [1,2,4]
5, res = [1,2,4,5]
3, res = [1,2,3,5]
```

这是贪心的。例如[1,6,2,4]，长度为2的最长子序列，可以是16，也可以是12——但只有是12的时候，才能扩展到后面的4。

- 在res中，找到第一个大于v的下标：
  - 在res下标里就替换
  - 在列表范围外就扩展



## [367. 有效的完全平方数](https://leetcode.cn/problems/valid-perfect-square/)

很简单。

## [383. 赎金信](https://leetcode.cn/problems/ransom-note/)

很简单

## [454. 四数相加 II](https://leetcode.cn/problems/4sum-ii/)

- 对前两个列表，做一个双重循环，获得 和-下标的哈希表；
- 对后两个列表也这样操作，建立哈希表；
- 遍历其中一个哈希表，看看能不能在另一个哈希表里找到对应的元素，并获得下标种类的乘积作为答案。

**但这么做有问题：**

1. 我们最后只需要知道个数，所以不需要记录具体的下标，只要记住个数：可以用Counter或者defaultdict(int)
2. 不需要建立第二个哈希表，只需要在做第二个双重循环的时候，查找对应的键值



## [459. 重复的子字符串](https://leetcode.cn/problems/repeated-substring-pattern/)

关键思路：如果一个字符串是重复的，比如`abaaba`，那将这个字符串x2，得到`abaabaabaaba`，其中必然存在这个字符串本身。所以如果`s in s+s`，就是真的——**前提是对s+s掐头去尾，不然就会找到自己。**

可以用builtin in/find，也可以用KMP。

**re 很慢！**



## [496. 下一个更大元素 I](https://leetcode.cn/problems/next-greater-element-i/)

典型的单调栈问题，一方面用hashmap建立两个数组的联系，另一方面对于`nums2`使用单调栈（允许单调递减，或者相等）。



## [503. 下一个更大元素 II](https://leetcode.cn/problems/next-greater-element-ii/)

可以把原始数据复制一遍，也可以取余。

``` python
def func(nums: list[int]) -> list[int]:
    n = len(nums)
    stk = []
    ans = [-1] * n

    for i in range(2*n-1):
        j = i % n
        while stk and nums[stk[-1]] < nums[j]:
            ans[stk.pop()] = nums[j]
        stk.append(j)

        return ans
```



## [541. 反转字符串 II](https://leetcode.cn/problems/reverse-string-ii/)

**热知识：Python Slice 不会 Raise IndexError，所以可以放心大胆的越界。**

``` python
s = list(s)
for i in range(0, len(s), 2*k):
    s[i:i+k] = reversed(s[i:i+k])
return "".join(s)
```



## [704. 二分查找](https://leetcode.cn/problems/binary-search/)

用双指针限定范围。确定中间值，然后根据target的位置，选择左指针`mid+1`，或者右指针`mid-1`。

极限情况下，左右指针只差一位。这时候mid=left：

- k=mid=left，返回
- k < mid，退出循环return -1
- k > mid，left=right=mid，再循环

> 最极端，left=right=mid:
>
> - 相等，那就return
> - k > mid，left = right+1，应该推出
> - k < mid，right = left-1，应该推出

可以发现退出循环条件至少是left < right。

left=right，也可以，所以选择left<=right

## [707. 设计链表](https://leetcode.cn/problems/design-linked-list/)

最快的方式肯定还是DuLNode，毋庸置疑。

但如果用平凡的实现，可能要考虑的情况比较多；最好的做法是定义dumm head and tail，这样思考特殊情况不用太多。

另外这里很多api都涉及一个问题：is index valid?所以可以把这个单独成一个方法`self.-get-node`，valid则返回node，否则None。



## [844. 比较含退格的字符串](https://leetcode.cn/problems/backspace-string-compare/)

可以用stack，但是，不是最好的方法。

**最节省资源的方式：逆序寻找，但代码真的很丑**

## [904. 水果成篮](https://leetcode.cn/problems/fruit-into-baskets/)

本质是寻找一个最长子序列。

``` python
lo = 0
for hi, v_hi in enumerate(data):
    v_hi 加入窗口
    
    while 不满足条件：
    	缩短前指针，直至满足条件
        
    更新结果
```





## [977. 有序数组的平方](https://leetcode.cn/problems/squares-of-a-sorted-array/)

两周简单情况，不用说。

先找到第一个大于等于0的数字，以此为分界线，一边小于0，另一边大于等于0.

然后向两边分别找。



















​	
