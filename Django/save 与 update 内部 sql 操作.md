原文：
https://www.jianshu.com/p/1f00a13d7267

Python框架Django有着诸多优点，它提供的models可以让开发者方便地操作数据库，但正是由于对上层的良好的封装，使得提升数据库操作性能必须要清楚地知道Django的数据库操作到底执行了哪些SQL语句。

例如数据更新操作，对单条记录，可以使用save或者是update两种方式

在Django工程下的settings.py下将log设置为DEBUG，即可查看save和update分别执行了哪些SQL语句

如有一张表名叫做 **Example**

## 使用save:
```py
    k = Example.objects.get(id=481)
    k.total_calories = 12
    k.save()
```
执行的SQL语句如下所示：
```sql
SELECT (1) AS `a` FROM `Example` 
WHERE `Example`.`id` = 481  LIMIT 1; args=(481,)
UPDATE `Example` 
SET 
    `user_id` = asdfasdf, 
    `event_id` = -1, 
    `join_type` = 0, 
    `name` = , `phone` = , 
    `email` = , 
    `company_name` = , 
    `address` = , 
    `if_type` = 0, 
    `code` = , 
    `location` = , 
    `total_days` = 0, 
    `total_length` = 0, 
    `total_calories` = 12, 
    `comments` = , 
    `reserved_1` = , 
    `reserved_2` = , 
    `reserved_3` = , 
    `reserved_4` = , 
    `reserved_5` = , 
    `create_datetime` = 2015-02-02 17:43:53 
WHERE `Example`.`id` = 481 ; 
args=(u'asdfasdf', -1, 0, u'', u'', u'', u'', u'', 0, u'', u'', 0, 0, 12, u'', u'', u'', u'', u'', u'', u'2015-02-02 17:43:53', 481)
```
首先要查询k这条记录，然后save()的时候提交更新的内容，发现更新的时候把Example中的有字段都SET赋值的一次

## 使用update
```py
Example.objects.filter(id=481).update(total_calories = 10)
```
执行的SQL语句是：
```sql
UPDATE `Example` 
SET `total_calories` = 10 
WHERE (`Example`.`user_id` = asdfasdf AND `Example`.`id` = 481 ); 
args=(10, u'asdfasdf', 481)
```
这条SQL语句简短而且执行速度要优于使用save的速度。

- 从SQL的执行情况来看,使用upate是要优于save方式的。
- 从使用情境上看，update更加适用于批量数据更新，而save则更适合当然也只适合做单条记录的数据更新操作了。
