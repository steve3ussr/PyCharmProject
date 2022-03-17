也不知道该看啥，就做了 [leetcode cn的最火的一百题](https://leetcode-cn.com/problem-list/2cktkvj/) 。

# 1 two-sum 
给定一个整数数组 nums和一个整数目标值 target，
请你在该数组中找出 和为目标值 target的那两个整数，并返回它们的数组下标。
你可以按任意顺序返回答案。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

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


# lengthOfLongestSubstring

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


