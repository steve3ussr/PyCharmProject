> 这是一个二叉树专题。

## 二叉树的遍历

1. 基本概念：前序遍历，中序遍历，后序遍历。三个节点里先左后右，遍历名字里说的是父节点的位置。前序（**父**左右），中序（左**父**右），后序（左右**父**）4
2. 可以有两种方法，递归（简单）和遍历（难）

### 递归

比较简单的方法是使用递归，通过一个递归函数。在递归函数里按照顺序做3件事情：递归左节点、添加父节点的数据到结果里，递归右节点。

如果一个节点没有任何子节点，那在添加了这个叶子节点的值之后就不会进行任何操作。

例子：中序遍历

```python
def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res = []
    if not root:
        return res

    def f(node):
        # 左节点
        if node.left:
            f(node.left)
        
        # 父节点
        res.append(node.val)
        
        # 右节点
        if node.right:
            f(node.right)

    f(root)
    return res
```

### 迭代（通过stack）

#### 前序遍历

初始时只有一个root。每次如果stack里有东西就循环：

1. 将pop的节点添加到答案里（前序）
2. pop一个节点，如果有的话，先添加右节点，再添加左节点（出栈的时候就是先左后右）

```python
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        stack = deque([root])

        while stack:
            node = stack.pop()
            res.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
        return res
```

#### 后序遍历

显而易见，后序遍历和前序遍历的结果完全相反。所以只需要`return res[::-1]`

#### 中序遍历

不能向之前一样，用stack来控制访问了。用一个指针和stack来访问。

1. 先走到最左侧位置；在过程中将路上的父节点都保留下来
2. 

```python
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        stack = []  # 不能提前将root结点加入stack中，代表还没有探索完成的节点
        result = []
        cur = root  # curr是下一个待处理的节点
        while cur or stack:  # stack空，说明全访问完了/刚开始/访问完root的左部分
            # 先迭代访问最底层的左子树结点
            if cur:     
                stack.append(cur)
                cur = cur.left		
            # 到达最左结点后处理栈顶结点    
            else:		
                cur = stack.pop()
                result.append(cur.val)
                # 取栈顶元素右结点
                cur = cur.right	
        return result
```

循环里的迭代访问左，我理解；

迭代访问右里包括两种情况：

- curr是一个left，那么会返回到上一层，并继续探索右子树；
- curr是一个right，说明对某个节点的右子树也访问完了，返回上一层，并继续探索右子树；

总的来说，curr为None说明肯定是某个节点的左子树全访问完了

#### 一个方便的迭代方法

> https://leetcode.cn/problems/binary-tree-inorder-traversal/solutions/25220/yan-se-biao-ji-fa-yi-chong-tong-yong-qie-jian-ming/

```python
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        stack = [root]

        while stack:
            node = stack.pop()
            if node is None:
                continue
            if isinstance(node, TreeNode):
                stack.append(node.right)
                stack.append(node.val)
                stack.append(node.left)
            else:
                res.append(node)
                
        return res
```

只需要按照前中后的**倒序**，调整三行入栈的位置就好了。我认为这个方法直观又好记。





## 二叉树的层序遍历/BFS

用deque是很方便的。模板题目：[102. 二叉树的层序遍历](https://leetcode.cn/problems/binary-tree-level-order-traversal/)

```python
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    
    	res = []
        if not root:
            return res

        lst = deque([root])
        
        while lst:
            tmp = []
            for i in range(len(lst)):
                node = lst.popleft()
                tmp.append(node.val)

                if node.left:
                    lst.append(node.left)
                if node.right:
                    lst.append(node.right)


            res.append(tmp)
        return res
```

高级题目：

- [101. 对称二叉树](https://leetcode.cn/problems/symmetric-tree/)
- 



## 二叉树的DFS

