[toc]

---

# Java Object 类

Java **==Object 类是所有类的父类==**，也就是说 Java 的所有类都继承了 Object，
**==子类可以使用 Object 的所有方法==**。

<img style="width:600px" src="https://www.runoob.com/wp-content/uploads/2020/10/classes-object.gif"></img>



Object 类位于 **`java.lang`** 包中，编译时会自动导入，
<u>我们创建一个类时，如果没有明确继承一个父类，那么它就会自动继承 Object，成为 Object 的子类。</u>

Object 类可以显示继承，也可以隐式继承，以下两种方式是一样的：
显示继承:
```java
public class Runoob extends Object{

}
```
隐式继承:
```java
public class Runoob {   // 没有明确继承的父类，自动继承 object

}
```


## 类的构造函数

构造一个新对象。
```java
Object()
```


## Object 类的方法

即，所有(子)类都会有的方法
```java
protected Object clone()
// 创建并返回一个对象的拷贝

boolean equals(Object obj)
// 比较两个对象是否相等

protected void finalize()
// 当 GC (垃圾回收器)确定不存在对该对象的有更多引用时，由对象的垃圾回收器调用此方法。

Class<?> getClass()
// 获取对象的运行时对象的类

int hashCode()
// 获取对象的 hash 值

void notify()
// 唤醒在该对象上等待的某个线程

void notifyAll()
// 唤醒在该对象上等待的所有线程

String toString()
// 返回对象的字符串表示形式

void wait()
// 让当前线程进入等待状态。直到其他线程调用此对象的 notify() 方法或 notifyAll() 方法。

void wait(long timeout)
// 让当前线程处于等待(阻塞)状态，直到其他线程调用此对象的 notify() 方法或 notifyAll() 方法，或者超过参数设置的timeout超时时间。

void wait(long timeout, int nanos)
// 与 wait(long timeout) 方法类似，多了一个 nanos 参数，这个参数表示额外时间（以纳秒为单位，范围是 0-999999）。 所以超时的时间还需要加上 nanos 纳秒。。
```






<br>
<br><br><br><br><br><br>


<u></u>

<img style="width:500px" src=""></img>






