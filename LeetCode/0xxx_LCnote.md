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

