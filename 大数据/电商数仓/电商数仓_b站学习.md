# 目录

[toc]

---

[link](https://www.bilibili.com/video/BV1df4y1U79z?from=search&seid=15154304885674956173)



# 第1章 数据仓库概念

**业务数据**：

就是各行业 **在处理事务过程中产生的数据**。
比如 <u>用户在电商网站中登录、下单、支付等过程中产生的数据</u>就是业务数据。
业务数据通常存储在 MYSQL、 Oracle等数据库中。
[link](https://www.bilibili.com/video/BV1df4y1U79z?p=2)


**用户行为数据**：

用户在使用产品过程中，**与客户端产品交互过程中产生的数据**，
比如页面浏览、点击、停留、评论、点赞、收藏等。<u></u>
用户行为数据通常存储在日志文件中。
（**反应用户心理变化的数据**，比如对某一商品的喜爱程度，得到这些数据可以后续做相关的推荐）
[00:39 看 url 中的参数解析，淘宝是如何抓取用户行为数据的](https://www.bilibili.com/video/BV1df4y1U79z?p=2)

<img width=900 src='https://upload-images.jianshu.io/upload_images/11876740-a4b33722b6472a1e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240'>

上面抓取的是 **半结构化数据**，存储在日志文件中，
后面会将半结构数据转换成结构化数据，放在 MySQL 中存储或放在 hive 数仓中进行正常解析 

网站为了获取与用户行为相关的半结构化数据，可以在网站中 **埋点**                                                                                                                     


## 数据仓库
数据仓库(Data Warehouse)，是**为企业制定决策，提供数据支持**的。
可以帮助企业，改进业务流程、提高产品质量等。


### ① 数据来源

- 获取数仓数据来源的方式主要是爬虫
- 获取的数据主要有两种：用户行为数据、业务数据
    - 用户行为数据通常以文件形式存储在日志服务器
    - 业务数据通常以数据表形式存储在 javae 后台的 MySQL 数据库中  

<img width=150 src='https://upload-images.jianshu.io/upload_images/11876740-8a6fb31c196bcfc0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240'>






### ② 中间处理







### ③ 输出用处






[看到 02：40](https://www.bilibili.com/video/BV1df4y1U79z?p=3)






<u></u>

<br>
<br>
<br>
<br>
<br>
<br>









