[toc]

---

# RESTful

## 什么是 RESTful

- **表现层 状态转移**，有 HTTP 协议的主要设计者 Roy Fielding 提出
- **资源**（Resource），**表现层**（Representation），**状态转移**（State Transfer）
- 是一种以资源为中心的 web 软件架构风格，可以用 Ajax 和 Restful web 服务构建应用


## 资源 表现层 状态转移

- (Resource)        资源    : 使用 url 指向一个实体
- (Representation)  表现层  : 资源的表现形式。比如图片、HTML 文本等
- (State Transfer)  状态转移: get, post, delete, put HTTP 动词来操作资源，实现资源状态的改变



## RESTful 的准则

- <u>**所有事物抽象为资源**</u>，资源对应唯一的标识
- 资源通过接口进行操作实现状态转移，操作本身是<u>**无状态的**</u>
- 对资源的操作不会改变资源的标识


## RESTful 风格 API

- 通过 HTTP `get/post/delete/put` 来 获取/新建/删除/更新
- 一般使用 json 格式返回数据
- 一般 web 框架都有相应的插件支持 RESTful API


## 如何设计 RESTful API


![how_to_design_restful_api](https://github.com/yesdino/img_upload/blob/master/imooc_study/hash/how_to_design_restful_api.png?raw=true)


## 示例
![tornado_restful_api](https://github.com/yesdino/img_upload/blob/master/imooc_study/hash/tornado_restful_api.png?raw=true)


