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



















