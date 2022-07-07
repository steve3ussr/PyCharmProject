# 前言

使用Git+PyCharm

因为现在用不上其实，就随便看一看

[ref1](https://www.cnblogs.com/jsdy/p/12322172.html#_label1)

[ref2_recom](https://majinjian.blog.csdn.net/article/details/122824860?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.665878&depth_1-utm_source=distribute.pc_relevant_t0.665878&utm_relevant_index=1)

# Git的工作原理图

![](https://img2018.cnblogs.com/i-beta/1724937/202002/1724937-20200217155304678-492462344.png)

这里的remote是github上的repo，repo是本地文件夹里的隐藏.git文件夹

# 基本操作命令

- `cd ..` 返回上一级

- `git add .` 是添加所有当前目录的所有文件

- `git commit -m “注释”` 和服务器的代码合并（放到本地仓库）

- `git push` 提交

---

- `git pull` 拉取远程代码（替代本地repo）

---

- `git branch -b "name"` 新建分支
- `git branch -set-upstream-to = origin/master "new_branch"` 将本地分支和远程服务器关联，将本地新建的分支new_branch分到服务器的origin/master的分支下
- ``
- ``
- ``
- ``

# 更新被拒绝

[https://www.cnblogs.com/jzxy/articles/14808893.html](https://www.cnblogs.com/jzxy/articles/14808893.html)

# 本地和远程仓库有冲突

可将本地的存放起来：`git stash`








