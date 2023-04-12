# 1xxx_LCnote

> LeetCode笔记：id号2000-3000的题目

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



## [1041. 困于环中的机器人](https://leetcode.cn/problems/robot-bounded-in-circle/)

代码很简单，关键是思考**总结果**：

- 回到原点：这时不同朝向就相当于总的结果是原地转圈，总会回到起始状态（面朝北）;
- 不在原点：
  - 如果朝北：越走越远；
  - 其他方向：经过二次/四次一定回到起始方向







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