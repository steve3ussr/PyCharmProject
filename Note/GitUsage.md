# 前言

使用Git+PyCharm

因为现在用不上其实，就随便看一看

[ref1](https://www.cnblogs.com/jsdy/p/12322172.html#_label1)

[ref2_recom](https://majinjian.blog.csdn.net/article/details/122824860?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.665878&depth_1-utm_source=distribute.pc_relevant_t0.665878&utm_relevant_index=1)

# Git的工作原理图

![](https://i.imgur.com/Kg1YHaU.png)

这里的remote是github上的repo，repo是本地文件夹里的隐藏.git文件夹

---

假如现在新建了一个项目，需要10个人一起进行开发，那么怎么进行代码管理呢？最主流的方案就是用 git。

首先创建一个 remote repo，默认会创建一个主分支 master，一般这就是生产环境；

但是大家 dev 中的代码不能都放到 master 上，所以会有几个 remote dev branches，可能是根据每个人，或者每个模块，大家平时都是和这些 branches 交互；

只有项目上线，大家开发结束，经过 review 才会 merge 到 master 上；

---

一般每个人都会有若干个 branches 和他相关，所以在本地 repo 一般也会有若干个 local branches 一一对应；

当我刚加入项目组，我可以 fetch/clone 远程分支到本地分支；

假如我和其他人共同开发一个分支，我通过 pull(fetch + merge) 可以获取最新进展；

---

平时正在开发哪个 branch，就需要切换本地分支——workspace 的文件也会发生变化；

开发过一小步，可以 add 到暂存区，再 commit 到本地分支，push 到 远程分支；

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

# Ahead / Behind

如果本地分支落后, push时会报错: 

```
! [rejected] master -> master (fetch first)
error: 无法推送一些引用到 ‘git@github.com:shuailisha/git_share.git’
提示：更新被拒绝，因为远程版本库包含您本地尚不存在的提交。这通常是因为另外
提示：一个版本库已推送了相同的引用。再次推送前，您可能需要先合并远程变更
提示：（如 ‘git pull’）。
提示：详见 ‘git push –help’ 中的 ‘Note about fast-forwards’ 小节。
```

所以需要将远程分支先和本地分支合并: 使用`git pull`, 或者`git fetch origin + git merge origin/master`

# 本地和远程仓库有冲突

可将本地的存放起来：`git stash`

# 切换本地分支

`git checkout <another branch>`

# 关联本地分支和远程分支

查看本地分支: `git branch`

查看本地 + 远程分支: `git branch -a`

查看本地与远程分支关联: `git branch -vv`

为某个本地分支设定关联: `git --set-updtream-to=<remote branch> <branch> `; 例如`git --set-upstream-to=origin/remote_branch my_branch `

# 本地分支完蛋, 重新获取远程分支

先切换到其他本地分支: `git checkout other_branch`

删除完蛋的分支: `git branch -d shit_branch`

新建分支, 切换到这个分支, 同时从远程分支拉取: `git checkout -b new_branch origin/a_branch`; 这个操作也会自动将这两个分支关联起来

---

如果出现提示：

```
fatal: Cannot update paths and switch to branch 'dev2' at the same time.
Did you intend to checkout 'origin/dev2' which can not be resolved as commit?
```

表示拉取不成功。我们需要先执行

`git fetch`

然后再执行
`git checkout -b 本地分支名 origin/远程分支名
`

---

更新远程分支: `git fetch remote_repo remote_branch_name`

更新远程分支并在本地创建一个分支保存这个分支的所有数据`git fetch remote_repo remote_branch_name:local_branch_name`

或者`git stash`, `git pull`, `git stash clear`

# 删除分支

删除远程分支：`git push --delete origin <branch_name>`

删除本地分支：`git checkout -d <local_branch_name>`
