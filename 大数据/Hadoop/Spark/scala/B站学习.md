[toc]

---

[link](https://www.bilibili.com/video/av33997956/?p=1)

# scala

spark 底层源码就是 scala 写的


## java 与 Scala 对比：

- java 是基于 JVM 的语言，Scala 也是基于 JVM 的语言。也就是说他们的文件要执行必须要先编译成 `.class` 文件才能在 JVM 上运行
<br>
- java 是面向对象的语言，可以将对象当做参数传来传去
  scala 是 **==面向对象+面向函数==** 的语言，还可以将函数传来传去



## scala 6 个特征

[link](https://www.bilibili.com/video/av33997956/?p=1)
- **可以与 Java 无缝整合**。Scala 和 Java 都可以在 JVM 中运行，因为他们都要先编译成 .class
- **scala 可以与 Java 互相调用**。（不过不可以两种语言混合写在一个文件中
- **自动进行类型推断**。定义变量 var 或常亮 val 的时候可以不用生命类型，语言会根据初始值确定类型。
- **支持并发与分布式**。其中有个 actor 通信模型，可以实现节点与节点之间的信息传递
- **Traits 特质特性**。结合了 java 中的抽象类和接口的所有特性。可以理解为是 scala 中的接口
- **模式匹配**。switch...case 方式的匹配，既可以匹配值，也可以匹配类型
- **高阶函数**。可以将函数作为参数传递


## 数据类型

注意一点，
Java 中有的数据类型，Scala 中也会一定会有，而且位数相同

数据类型 描述
- **`Byte`** 8bit 的有符号数字，范围在 -128--127
- **`Short`** 16bit 有符号数字，范围在 -32768--32767
- **`Int`** 32bit 有符号数字，范围 -2147483648 到 2147483647
- **`Short`** 64bit 有符号数字，范围 -9223372036854775808 到 922372036854775807
- **`Float`** 32 bit IEEE754 单精度浮点数
- **`Double`** 64 bit IEEE754 双精度浮点数
- **`Char`** 16 bit Unicode 字符。范围 U+0000 到 U+FFFF
- **`String`** 字符串
- **`Boolean`** 布尔类型
<br>
- **`Unit`** 表示无值，和其他语言中 **void** 等同
- **`Null`** 空值或者空引用
- **`Nothing`** 所有其他类型的子类型，表示没有值
- **`Any`** 所有类型的超类（父类），任何实例都属于 Any 类型
- **`Anyref`** 所有 **引用类型** 的超类（父类）
- **`Anyval`** 所有 **值类型** 的超类（父类）


**详解：**
**`Nothing`** 表所有类型的子类，类比 Java 所有类型的基类是 Object，
Nothing 是用于自动类型推断的，当 Scala 无法推断出当前的类型的时候，就给你返回一个 Nothing。
```scala
scala> val list = List()
list: List(Nothing) = List() 
```
Nothing 没有实例，不能实例化，只是用于类型推断。
所以不要 new Nothing 对象



Any 是所有类型的父类 
















