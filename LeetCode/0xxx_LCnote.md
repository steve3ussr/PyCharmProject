## [300. 最长递增子序列](https://leetcode.cn/problems/longest-increasing-subsequence/)

### 普通思路

定义dp[i]为，以nums[i]结尾的最长子序列长度。

初始值为1，就是假设前面的元素都比nums[i]大。

对dp[i]来说，dp[i] = dp[j]+1，其中j为i前面的元素，并且nums[j]<nums[i]，也就是说组成了一个最长的递增子序列。

当然，得取最大的dp[j]

### [高级思路](https://www.bilibili.com/video/BV1ub411Q7sB?t=356.5)

太难了，写不出来