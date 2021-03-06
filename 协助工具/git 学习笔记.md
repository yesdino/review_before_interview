[toc]


---

参考：
https://www.cnblogs.com/simple1368/p/9084077.html

## git 服务器新建仓库
> git init --bare 仓库名.git


```
[git@localhost git]$ git init --bare hugin.git
Initialized empty Git repository in /home/git/git/hugin.git/
[git@localhost git]$ ls
hugin.git
[git@localhost git]$ pwd
/home/git/git
```

## 本地同步 git 服务器仓库


```
Z17023031@ZHS-W54001050 MINGW64 /e/code/SVN/Hugin/L11RackMonitor/trunk/sourcecode (master)
$ pwd
/e/code/SVN/Hugin/L11RackMonitor/trunk/sourcecode
```

### 1、 将本地目录变为 git 本地仓库

> git init
```
$ git init
Initialized empty Git repository in E:/code/SVN/Hugin/L11RackMonitor/trunk/sourcecode/.git/

$ ls
hugin/
```
- 设置忽略文件 .gitignore
```
$ touch .gitignore

$ ls
hugin/
```

### 2、 查看仓库文件状态
```
Z17023031@ZHS-W54001050 MINGW64 /e/code/SVN/Hugin/L11RackMonitor/trunk/sourcecode (master)
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        .gitignore
        hugin/

nothing added to commit but untracked files present (use "git add" to track)
```

### 3、 追踪除了忽略文件以外所有文件
```py
git add .
```

### 4、 将文件提交到本地仓库 （本地仓库可多次提交
```
git commit -m 'first commit'
```

git commit -m 'first commit. Base on server code'

### 5、 关联远程 git 仓库
> git remote add origin 远程库地址(用户@IP:git仓库目录路径)
```
$ git remote add origin git@IP:/home/git/git/hugin.git
```
$ git remote add origin git@IP:/home/git/git/tracking_management.git

### 6、 将本地 git 仓库改动全部同步到远程 git 仓库
> 第一次 push 的时候,加上 -u 参数,
Git 就会把本地的 master 分支和远程的 master 分支进行关联起来, 我们以后的 push 操作就不再需要加上 -u 参数了
```
$ git push -u origin master
git@IP's password:
Enumerating objects: 764, done.
Counting objects: 100% (764/764), done.
Delta compression using up to 8 threads
Compressing objects: 100% (735/735), done.
Writing objects: 100% (764/764), 2.71 MiB | 5.61 MiB/s, done.
Total 764 (delta 80), reused 0 (delta 0)
To IP:/home/git/git/hugin.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
```
注意：若远程 git 仓库为空，可直接做这一步

若远程 git 仓库不为空

### 7、远程库与本地同步合并
```
git pull --rebase origin master
```

### 8、克隆远程仓库内容
同步了远程之后想看看最新的内容有没有在上面，于是我在 git 远程仓库所在的服务器上的另一个目录进行克隆
```
[hugin@localhost test1]$ git clone git@127.0.0.1:/home/git/git/hugin.git
Cloning into 'hugin'...
git@127.0.0.1's password:
remote: Counting objects: 764, done.
remote: Compressing objects: 100% (655/655), done.
remote: Total 764 (delta 80), reused 764 (delta 80)
Receiving objects: 100% (764/764), 2.71 MiB | 0 bytes/s, done.
Resolving deltas: 100% (80/80), done.
[hugin@localhost test1]$ ls
hugin
```

git clone git@IP:/home/git/git/tracking_management.git

看了一下目录的内容，有成功同步


<u>**可以看到远程克隆的时候要输 git 用户密码，用来专门控制克隆权限。
所以一开始就要新建 git 用户专门用于控制远程 code 文件**</u>


## 提交本地修改

### 1、本地提交
```
git push -u origin master
```

### 2、异地更新

```
git pull
```

# ---------------------------------



## 本地库 and 远程库

[link](https://www.bilibili.com/video/av24441039?p=9)

- 本地库：自己电脑上的仓库（用于个人开发）
- 远程库：服务器上的仓库（用于部门内部团队协作开发）

![工作区暂存区本地仓库.png](https://upload-images.jianshu.io/upload_images/11876740-db8128c632460e1d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)




当然，远程库与远程库之间可以进行 **跨部门/跨公司** 的协作开发

![本地库and远程库.png](https://upload-images.jianshu.io/upload_images/11876740-1219078c265aac64.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)





<!-- ![本地库and远程库.png](https://upload-images.jianshu.io/upload_images/11876740-11b192d576a7a385.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240) -->


## 添加到追踪区 add

[link](https://www.cnblogs.com/grooovvve/p/9732491.html)

```py
git add [file1] [file2]
```
如果要同时添加多个文件
```py
# 可以添加同类型的所有文件
git add *.扩展名
```
添加 **新增**、**修改**、**删除** 的文件
```py
git add .
```
u 代表 updata，你更新你已经跟踪的文件；
如果你添加了新文件，那么你是不会主动跟踪，并提交的。
<u>**所以这条指令无法探测新增文件！**</u>
这条命令还是有用的，如果你只是把一些你不想add的文件放在目录而已，那就用这条命令去add已经建立跟踪的文件
```py
git add -u .
```

包括了前两项
```py
git add -A .
```

遇到不知道的，要懂得查help
```py
git add -h
```
```
usage: git add [<options>] [--] <pathspec>...

    -n, --dry-run         dry run
    -v, --verbose         be verbose

    -i, --interactive     交互式选择 interactive picking
    -p, --patch[=<patch-mode>]
                          选择大块交互 select hunks interactively
    -e, --edit            编辑当前的 diff 并提交 edit current diff and apply
    -f, --force           允许添加忽略文件 allow adding otherwise ignored files
    -u, --update          update 已经在追踪区的文件 update tracked files
    --renormalize         renormalize EOL of tracked files (implies -u)
    -N, --intent-to-add   record only the fact that the path will be added later
    -A, --all             add changes from all tracked and untracked files
    --ignore-removal      ignore paths removed in the working tree (same as --no-all)
    --refresh             don't add, only refresh the index
    --ignore-errors       just skip files which cannot be added because of errors
    --ignore-missing      check if - even missing - files are ignored in dry run
    --chmod (+|-)x        override the executable bit of the listed files
```

## 设置签名 config


[link](https://www.bilibili.com/video/av24441039?p=11)



**作用**：区分不同开发人员的身份
**辨析**：这里设置的签名和登录远程库（代码托管中心）的账号、密码没有任何关系命令

**级别优先级**：
- 就近原则：**项目级别 > 系统用户级别**，二者都有时采用项目级别的签名
- 如果只有系统用户级别的签名，就以系统用户级别的签名为准
- 二者都没有不允许

例如，下面是开发人员的信息：
用户名：`tom`
Emai地址：`goodMorning@atguigu.com`
- 项目级别/仓库级别：仅在 **当前本地库** 范围内有效
```py
git config user.name tom_pro
git config user.email goodMorning@atguigu.com
```
- 系统用户级别：登录当前 **操作系统** 的用户范围
```py
git config --global user.name tom_pro
git config --global goodMorning@atguigu.com
```

### config 信息保存位置

- 项目/仓库级别
```py
$ cat .git/config
```
```py
[core]
        repositoryformatversion = 0
        filemode = false
        bare = false
        logallrefupdates = true
        symlinks = false
        ignorecase = true
[remote "origin"]
        url = https://github.com/yesdino/review_before_interview.git
        fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
        remote = origin
        merge = refs/heads/master
[gui]
        wmstate = normal
        geometry = 818x435+104+104 175 196
[user]
        email = 915678808@qq.com
        name = dino_comp
```

- 系统用户级别

<img width="500" src="https://upload-images.jianshu.io/upload_images/11876740-f0ff19e11f8d5123.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240"></img>



<!-- ![设置签名.png](https://upload-images.jianshu.io/upload_images/11876740-ebe5b24fff2763bb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240) -->


<br>



## 查看历史记录 log

```py
# 完整 log 信息
git log

# 一行 log（完整哈希值）
git log --pretty==oneline

# 一行 log（缩略哈希值）
git lof --onelone

# 版本 log 信息
git reflog
```

<!-- <img width="500" src="https://upload-images.jianshu.io/upload_images/11876740-b2ba89d8377aab01.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240"></img> -->





## 版本切换 reset

先打出所有版本信息：

```py
git reflog
```
<img width="550" src="https://upload-images.jianshu.io/upload_images/11876740-752c97cb5581f3e0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240"></img>

- 前面的黄色部分数字表示这个历史版本的==索引值==
- ==**HEAD**== 指针指向当前远程仓库中的 master 分支所在的版本

当我们想要回到某一个历史版本的时候，使用下面指令：

```py
git reset --hard 版本索引值
```

reset 回到历史版本指令有3个不同的参数：
`--hard`、`-soft`、`--mixed`

3者的区别为

![git_reset参数区别.png](https://upload-images.jianshu.io/upload_images/11876740-d4e8d765006ea7a5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

注意上面的概念里面：
- **本地库** ：git 本地仓库（注意不是远程仓库 git本地不但有暂存区还有本地仓库）
- **暂存区** ：本地追踪文件区
- **工作区** ：就是我们电脑上的文件夹


## 比较版本差异 diff

[link](https://www.bilibili.com/video/av24441039?p=23)

用 diff 指令：

```py
git diff [filename]
```

![git_diff比较文件差异.png](https://upload-images.jianshu.io/upload_images/11876740-c68485358a78bf19.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)





## 分支 branch

### 查看当前所有分支

查看当前所有分支，并显示当前所在的分支（==绿色的==）
```py
git branch -v
```

![查看分支.png](https://upload-images.jianshu.io/upload_images/11876740-b82c3d58318a5099.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


### 新建分支

```py
git branch [分支名]
```

![新建分支.png](https://upload-images.jianshu.io/upload_images/11876740-7d0a5a8a93337806.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 切换分支

```py
git checkout [分支名]
```

![切换分支.png](https://upload-images.jianshu.io/upload_images/11876740-1528acf1555f2e3b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 合并分支

第一步：切换到接受修改的分支（被合并，增加新内容）上
```py
git checkout [被合并分支名]
```

第二步：执行 merge 命令
```py
git merge [有新内容分支名]
```

<!-- ![合并分支.png](https://upload-images.jianshu.io/upload_images/11876740-d4d61cf27da5d358.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240) -->

![合并分支2.png](https://upload-images.jianshu.io/upload_images/11876740-03fc1b2d0aaffe61.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 解决合并冲突


[link](https://www.bilibili.com/video/av24441039?p=25)


解决冲突

**冲突的表现**：

<img width="400" src="https://upload-images.jianshu.io/upload_images/11876740-f16de71a6c6cd68d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240"></img>

**冲突的解决**：
①：编辑文件，删除特殊符号
②：把文件修改到满意的程度，保存退出
③： `git add [文件名]`
④： `git commit -m "日志信息"`（注意：此时 `commit` 一定不能带具体文件名

<!-- ![解决冲突.png](https://upload-images.jianshu.io/upload_images/11876740-30cef31cf2ca9d2f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240) -->


![合并分支2.png](https://upload-images.jianshu.io/upload_images/11876740-bd18e4e60ec3a86c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


## 仓库别名 remote

使用 **remote** 指令建立本地与远程git仓库的映射关系，下次对远程仓库进行操作时直接 **==用别名代替远程仓库名==**

查看当前有的别名
```
git remote -v
```
新增别名

```
git remote add [自己定的别名] [远程git仓库地址]
```


![仓库别名.png](https://upload-images.jianshu.io/upload_images/11876740-e572abe5ee3de962.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


## 克隆 clone

```py
git clone [远程地址]
```
效果：
- 完整的把远程库下载到本地
- 创建 origin远程地址别名
- 初始化本地库

<!-- ![clone命令.png](https://upload-images.jianshu.io/upload_images/11876740-8acda7f4471ef367.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240) -->



## 推送到远程仓库 push
 
注意很重要的一点：<br>
==你要往远程仓库里面推送，一定要在你的本地仓库的版本是最新的远程仓库版本的基础上==（这点自己在项目实战上也体会）。

**如果你的本地仓库版本已经落后于当前远程仓库的最新版本了，一定要先 pull 再修改或者 push**
```
git push [别名] [分支]
```
接着会开始提示需要输入账号密码

- 如果是创建远程.git仓库的那个账号密码，代表身份是远程.git 仓库的拥有者，可以直接推送
- 如果 **不是** 创建远程.git仓库的那个账号密码，需要远程仓库的拥有者进行一项操作：添加这个用户为这个远程仓库的协作开发人员，邀请其对远程.git仓库进行修改（[link](https://www.bilibili.com/video/av24441039?p=37)只讲了 github 的同意操作，私人服务器没讲，自己度娘吧）


## 拉取 fetch/merge or pull

①.先拉取确定一下更新内容再合并

先拉取
```
git fetch [别名] [分支名]
```
去拉取更新的分支确认一下
```
git checkout [别名]/[分支名]
```
确认完了回到原来那个分支，合并

```
git merge [别名]/[分支名]
```



![fetch_pull.png](https://upload-images.jianshu.io/upload_images/11876740-19128814ecf8d17e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


②.直接拉取并合并

```
git pull [别名] [分支名]
```


## push request 

[link](https://www.bilibili.com/video/av24441039?p=40) 以 github push request 做演示，自己搭的服务器的话原理相同 怎么操作度娘吧。

目前用不到，暂时不研究。


![本地库and远程库.png](https://upload-images.jianshu.io/upload_images/11876740-11b192d576a7a385.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)