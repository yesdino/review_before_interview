[toc]

---



# Character 类
Character 类用于对单个字符进行操作。

Character 类 **在对象中包装一个基本类型 char 的值**

实例
```java
char ch = 'a';
 
// Unicode 字符表示形式
char uniChar = '\u039A'; 
 
// 字符数组
char[] charArray ={ 'a', 'b', 'c', 'd', 'e' };
```
然而，在实际开发过程中，我们经常会遇到需要使用对象，而不是内置数据类型的情况。
为了解决这个问题， Java 语言为内置数据类型 char 提供了包装类 Character 类。

Character 类提供了一系列方法来 **操纵字符**。
你可以使用 Character 的构造方法创建一个 Character 类对象，
例如：

```java
// 创建一个 Character 类实例
Character ch = new Character('a');
```
在某些情况下， Java 编译器会自动创建一个 Character 对象。

例如，
<u>**将一个 char 类型的参数传递给需要一个 Character 类型参数的方法时，
那么编译器会自动地将 char 类型参数转换为 Character 对象。**(==**自动类型转换**==）</u>
这种特征称为 **装箱**，反过来称为拆箱。
(==所以其实 char 类型的数据与 Character 对象类型的数据是可以通用的，
Java 会自动在内部装箱和拆箱来进行类型转换==)



实例
```java
// 原始字符 'a' 装箱到 Character 对象 ch 中 (自动/隐式转换类型)
Character ch = 'a';
 
// 原始 char 字符 'x' 用 test 方法装箱
// 返回拆箱的值到 'c'
char c = test('x');
```

## 转义序列

前面有反斜杠（\）的字符代表转义字符，它对编译器来说是有特殊含义的。

下面列表展示了Java的转义序列：
```html
【转义序列】      【描述】
  \t	        在文中该处插入一个tab键
  \b	        在文中该处插入一个后退键
  \n	        在文中该处换行
  \r	        在文中该处插入回车
  \f	        在文中该处插入换页符
  \'	        在文中该处插入单引号
  \"	        在文中该处插入双引号
  \\	        在文中该处插入反斜杠
```
实例
当打印语句遇到一个转义序列时，编译器可以正确地对其进行解释。

以下实例转义双引号并输出：

Test.java 文件代码：
```java
public class Test {
 
   public static void main(String args[]) {
      System.out.println("访问\"菜鸟教程!\"");
   }
}
```
以上实例编译运行结果如下：
`访问"菜鸟教程!"`


## Character 方法
下面是Character类的方法：

序号	方法与描述
**`isLetter()`**      是否是一个字母
**`isDigit()`**       是否是一个数字字符
**`isWhitespace()`**      是否是一个空白字符
**`isUpperCase()`**       是否是大写字母
**`isLowerCase()`**       是否是小写字母
**`toUpperCase()`**       指定字母的大写形式
**`toLowerCase()`**       指定字母的小写形式
**`toString()`**      返回字符的字符串形式，字符串的长度仅为1
对于方法的完整列表，请参考的 [java.lang.Character API](https://www.runoob.com/manual/jdk1.6/java/lang/Character.html) 规范。

















<br>
<br><br><br><br><br><br>


<u></u>

<img style="width:500px" src=""></img>






