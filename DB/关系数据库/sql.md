# 目录
[toc]

---

[转载！出处](https://www.jb51.net/article/82441.htm)

<!-- # MySQL 处理插入过程中的主键唯一键重复值的解决方法 -->

本篇文章主要介绍在插入数据到表中遇到键重复避免插入重复值的处理方法，
主要涉及到 `IGNORE`, `ON DUPLICATE KEY UPDATE`, `REPLACE` ；
接下来就分别看看这三种方式的处理办法。


## `IGNORE`

使用 **`ignore`** 当插入的值遇到主键 (`PRIMARY KEY`) 或者唯一键 (`UNIQUE KEY`) 重复时
自动忽略重复的记录行，不影响后面的记录行的插入。

- 创建测试表 `Tignore`
```sql
CREATE TABLE Tignore
(
    ID INT NOT NULL PRIMARY KEY ,
    NAME1 INT
)
default charset=utf8; 
```
- 正常插入

如果插入的记录中存在键重复会报错，整个语句都会执行失败

![img](https://img.jbzj.com/file_images/article/201604/2016041509271113.png)

- **`ignore`** 插入

如果插入的记录中存在重复值会 **==忽略==重复值的该记录行**，不影响其它行的插入。

![img](https://img.jbzj.com/file_images/article/201604/2016041509271114.png)

<br>

## `REPLACE`

使用 **`replace`** 当插入的记录遇到主键或者唯一键重复时，
先删除表中重复的记录行再插入。


- 创建测试表 `Treplace`
```sql
DROP TABLE IF EXISTS Treplace;
CREATE TABLE Treplace
(
    ID INT NOT NULL PRIMARY KEY ,
    NAME1 INT
)
default charset=utf8; 
```

- **`replace`** 插入

```
REPLACE INTO Treplace() VALUES(1,1), (1,2), (2,2);
```
![img](https://img.jbzj.com/file_images/article/201604/2016041509271115.png)
从输出的信息可以看到是4行受影响，说明它是先插入了（1,1）然后又删除了（1,1）

<br>


## `ON DUPLICATE KEY UPDATE`

当插入的记录遇到主键或者唯一键重复时，会执行后面定义的 UPDATE 操作。
相当于先执行 Insert 操作，再根据主键或者唯一键执行 update 操作。

- 创建测试表

    ```sql
    DROP TABLE IF EXISTS Tupdate;
    CREATE TABLE Tupdate
    (
        ID INT NOT NULL PRIMARY KEY ,   -- 主键 ID
        NAME1 INT UNIQUE KEY            -- 唯一键 NAME1
    )
    default charset=utf8;
    ```

- 使用 `ON DUPLICATE KEY UPDATE` 插入
```sql
INSERT INTO Tupdate() VALUES(1,1),(1,2) ON DUPLICATE KEY UPDATE NAME1=NAME1+1;
INSERT INTO Tupdate() VALUES(1,1),(1,2) ON DUPLICATE KEY UPDATE NAME1=VALUES(NAME1)+1; 
```
```sql
-- 第一条语句相当于执行:
INSERT INTO Tupdate() VALUES(1,1)
UPDATE Tupdate
SET NAME1=NAME1+1
WHERE ID=1;

-- 第二条语句相当于执行：
INSERT INTO Tupdate() VALUES(1,1)
UPDATE Tupdate
SET NAME1=2+1
WHERE ID=1; 
```
![img](https://img.jbzj.com/file_images/article/201604/2016041509271116.png)
在 `ON DUPLICATE KEY UPDATE` 后面使用 `VALUES` 指的就是插入的记录的值，
而不使用 `VALUES` 指的是表的自身值。

注意： 
`ON DUPLICATE KEY UPDATE` 的后面执行的 **`UPDATE`** 更新的记录是 **`WHERE`** <u>当 **重复的主键** 或者 **唯一键的 ID** 出现重复时</u>，
这点非常重要。
比如下面这种情况：
```sql
INSERT INTO Tupdate() VALUES(1,1),(2,1) ON DUPLICATE KEY UPDATE NAME1=VALUES(ID)+1; 
```
```sql
-- 唯一键 NAME1 重复但是主键不重复，执行的语句是这样的：
INSERT INTO Tupdate() VALUES(1,1)
UPDATE Tupdate
SET NAME1=2+1
WHERE ID=1; 
```
![img](https://img.jbzj.com/file_images/article/201604/2016041509271117.png)

## 总结

上面的三种处理重复值的方法都支持标准的 INSERT 语法，包括：
**`INSERT INTO ... VALUES`**, 
**`INSERT INTO .... SET`** ,
**`INSERT INTO ..... SELECT`** 。


关于 MySQL 处理插入过程中的主键唯一键重复值的解决方法小编就给大家介绍这么多，希望对大家有所帮助




<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>