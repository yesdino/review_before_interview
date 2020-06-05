## TortoiseSVN

### Merge

键主干中 project 文件夹，选择 `TortoiseSVN->Merge` ，这时会弹出一个 **`Merge type`** 让你选（ TortoiseSVN1.9.5 这个版本只有两个选项，网上有些博文有三个选项）， Merge type 的选择还是很有讲究，并且也是很容易搞错的，下面会具体来说说：

![img](https://images2017.cnblogs.com/blog/991670/201707/991670-20170726140612593-1347989149.png)


#### ①、**`Merge a range of revisions`**

我们先来说说“ Merge a range of revisions ”这个选项： 
我们选中这个选项，然后点击“ Next ”，会看到如下界面，
![img](https://images2017.cnblogs.com/blog/991670/201707/991670-20170726144312687-552715722.png)

- **`URL to merge from`**
因为我们是要将分支（ branch ）合并到主干（ trunk ），
所以这边 `URL to merge from` 选项要选择服务器上面需要合并到主干（ trunk ）的分支（ branch ）地址
（注：前面有提过，合并是合并到本地的 working copy ，所以一般合并之前，最好将本地 working copy 代码先更新一遍，有冲突的解决冲突，并且将未提交的代码提交，以防在合并之后，未提交的代码丢失），
<br>

- **`Revision range to merge`**
<br>

    - 1）**`all revisions`**
    当选择 all revisions 进行 merge 的时候， TortoiseSVN 做了 `diff and apply` 操作。 
    `diff` 是比较 URL to merge from 指定的工程 **最新一个版本和最初的一个版本的差异，**
        ```py
        假设最新版本是 r-last ，最初的版本 r-first ， r-last 相对 r-first 而言，增加了文件 a ，修改了文件 b ，
        那么在合并的时候，就将“增加文件 a ，修改文件 b ”的操作应用在本地的 working copy 上面去，这就完成了合并；
        ```

    - 2）**`specific range`**
    假设选择的是 specific range ，那么用户可以 **选择一个版本范围** ，也可以单独指定一个版本或者<u>不填写任何值（此时相当于选 all revisions ）</u>，
        ```py
        假设用户指定了版本 r1-r3 ，其中 r1 新增了文件 a ， r2 新增了文件 b ， r3 删除了文件 c ，
        那么在合并的时候 TortoiseSVN 就会将“新增文件 a ，新增文件 b ，删除文件 c ”应用于本地的 working copy ，这样就完成了合并 
        ```

    - 3）**`Reverse merge`**
    （ ps ：这边还有一个 Reverse merge 复选框，恢复之前的合并。假设我们刚刚做的 merge 有问题，需要将本地的 working copy 恢复成 merge 之前的，那么就需要将之前应用于本地 working copy 的操作全部回退，操作和 merge 基本一样，只是最后，需要复选这个 Reverse merge 复选框）

<br>

上步选择了`Revision range to merge`之后，点击“Next”，进入如下界面，这时我们就可以看到如下界面：

![img](https://images2017.cnblogs.com/blog/991670/201707/991670-20170726161944890-519944457.png)


全部使用默认的选项，然后在点击 **`Merge`** 之前，可以先点击 **`Test merge`** 按钮，测试一下 merge 之后的效果：



#### ②、**`Merge two different trees`**

我们再来说说这个“ Merge two different trees ”，从它自己选项的解释来看，是 **<u>将两个不同的分支（ branch ）合并到本地 working copy 中</u>**，
当然，我们也可以用这个选项将分支（ branch ）修改的内容合并回主干（ trunk ）。选择 Merge two different trees ，点击 Next。

上步之后，会出现如下对话框
![img](img/TortoiseSVN/Merge_two_different_trees.png)

**注意，我们现在是将分支（ branch ）合并回主干（ trunk ）**，

这个时候，我相信很多人想当然的认为 `From` 处填写的应该是分支（ branch ）的 URL ，而 `To` ，应该是主干（ trunk ）的 URL ，因为是从分支（ branch ）到主干（ trunk ）啊，然后事实并非如此。

之前在创建分支（ branch ）这一节，有让读者记住拉取分支（ branch ）时，主干（ trunk ）的版本号，当时主干（ trunk ）的版本号是 2 ，
- 所以 **`From`** 处的 URL 应该写主干（ trunk ）的 URL ， Revision 应该选 2 （其实 trunk revision 为 2 的版本，其实<u>也就是 branch 的第一个版本</u>，所以这边 From 可以选择主干拉取分支的版本，也可以选取分支最开始的版本），
- 而 **`To`** 处的 URL 应该选分支的 URL ， Revision 选 HEAD Revision ，也就是<u>选最新的分支版本</u>。

**现在就来说说为什么要这样填写：**

此处进行 merge 的时候，进行的操作也是 `diff and apply` ，
将 `To` 处 URL 和 revision 指定的某个版本，与 `From` 处 URL 和 Revision 指定的某个版本进行对比，
对比是有顺序的，这个怎么理解呢？
比如现在 To 处的为工程 project1 ， From 处的为工程 project ，如果 project1 相对于 project 而言，有文件 a ，没有文件 b ，换句话说 project1 相对于 project 而言，“新增了 a ，删除了 b ”，那么此处 merge 的结果就是会将“新增 a ，删除 b ”的操作应用于本地 working copy 的工程，那为什么 From 处的 project 不能指定为最新的 Revision 呢，既 HEAD Revision ？试想一下，假如主干（ trunk ）在拉取了分支（ branch ）之后，主干（ trunk ）和分支（ branch ）都有在并行开发，那么必然主干（ trunk ）上会有新增的功能，这样就会有新增的代码，这些代码在分支（ trunk ）上并不存在，在 To 和 From 比较过程中，就会出现“删除 xxx ”的操作，这在 merge 过程中会应用在本地 working copy 中，本来这个“ xxx ”是主干新功能的代码，在将分支合并过来的时候，不应该删除，所以不能用主干最新的版本和分支最新的版本做对比，应该是将当时拉取分支的时候的主干版本和当前最新的分支版本进行对比，应用到本地 working copy 中才对，所以这边的 From 必须选取当时拉取当前分支的主干版本，不然主干上面新增的代码会丢失，之前我对 From 和 To 的顺序，以及 revision 的选取也是迷糊了大半天，我希望对读者而言，我这边已经说清楚了 如果还有什么不清楚的欢迎加群交流


### resolve conflic

[source](https://stackoverflow.com/questions/7679113/differences-between-svn-merge-left-right-working-files-after-conflicts)

有两个分支`A` `B`，最新的 revision (HEAD) 分别为 `A`:`(9)`，`B`：`(6)`

当
```py
cd B; 
svn merge -r 5:8 ^/braches/A
```

SVN 将提交  A 分支上 `(5)`~`(8)` 的改动到分支 B 的最前面

（换言之，`(7)` 和 `(8)` 的改动记录都将提交到分支 B 上）

```
common
ancestor      left     right
(1)━━┱───(3)──(5)──(7)──(8)──(9)  # branch A
     ┃         └┄┄┄┄┬┄┄┄┄┘
     ┃              ↓
     ┗━(2)━━(4)━━(6)              # branch B
               working
```

假设一些 lines 在分支 A 的`(3)`中被修改，在分支 B 的 `(4)` 同样的源 lines 也被修改且修改处不同

如果在 `(5)`~`(8)` 版本迭代的过程中没有涉及上面的 lines 的改动，那不没有问题

但如果在 `(5)`~`(8)` 迭代的过程同样修改了 `(3)` `(4)` 修改的行，将会产生冲突，这时就不会自动做合并了，因为 SVN 无法判断要保留哪些，会生成下列几个 file：

- `file.working`：分支 B `(6)`，既被合并的分支最新的版本
- `file.merge-left`：分支 A `(5)`，既将要合并的分支选择的最前面的版本
- `file.merge-right`：分支 A `(8)`，既将要合并的分支选择的最后面的版本

如果你手动编辑 conflict 冲突文件，你有以下几个选择：

保留 `working` (你被合并的版本)，保留 `right`(合并过来的版本) 或者 手动做合并。
（`left` 本身并不怎么有用，在文件中保留 left (分支的旧版本) 是没有意义的。
然而，它对于工具是有用的。`left` →`right`为更改集。）

例如：

```
<<<<<<< .working

    life_universe_and_everything = 13

||||||| .merge-left.r5

    life_universe_and_everything = "13"

=======

    life_universe_and_everything = "42"

>>>>>>> .merge-right.r8
```

在分支 A 中，`"13"(str)`  modify 为 `"42"(str)`

在分支 B 中为 `13(int)`

当然，你手动合并解决冲突的时候可能会想要`42(int)`



<u></u>

<br>

<br><br><br><br><br><br><br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br>


![img]()



