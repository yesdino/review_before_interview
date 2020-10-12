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


# ------------------------------------

---


# String 类
字符串广泛应用 在 Java 编程中，**==在 Java 中字符串属于对象==**，
Java 提供了 String 类来创建和操作字符串。

## 创建字符串
创建字符串最简单的方式如下:
```java
String greeting = "菜鸟教程";
```
在代码中遇到字符串常量时，这里的值是 "菜鸟教程""，
编译器会使用该值创建一个 String 对象。

和其它对象一样，可以使用 **关键字** 和 **构造方法** 来创建 String 对象。

String 类有 11 种构造方法，这些方法提供不同的参数来初始化字符串，比如提供一个字符数组参数:

StringDemo.java 文件代码：
```java
public class StringDemo{
   public static void main(String args[]){
      char[] helloArray = { 'r', 'u', 'n', 'o', 'o', 'b'};
      String helloString = new String(helloArray);  // 将 char 数组对象转换成 String 对象  
      System.out.println( helloString );
   }
}
```
以上实例编译运行结果如下：
`runoob`

注意:
**==String 类是不可改变的==**，
所以你一旦创建了 String 对象，那它的值就无法改变了（详看笔记部分解析）。

如果需要对字符串做很多修改，那么应该选择使用 **`StringBuffer`** & **`StringBuilder`** 类。

## 字符串长度

<u>用于获取有关对象的信息的方法</u> 称为 **访问器方法**。

String 类的一个访问器方法是 **`length()`** 方法，它返回字符串对象包含的字符数。

StringDemo.java 文件代码：
```java
public class StringDemo {
    public static void main(String args[]) {
        String site = "www.runoob.com";
        int len = site.length();
        System.out.println( "菜鸟教程网址长度 : " + len );
   }
}
```
以上实例编译运行结果如下：
`菜鸟教程网址长度 : 14`

## 连接字符串
String 类提供了连接两个字符串的方法：
**方法①：`concat() 方法`**
```java
string1.concat(string2);
```
返回 string2 连接 string1 的新字符串。

也可以对字符串常量使用 concat() 方法，如：

```java
"我的名字是 ".concat("Runoob");
```
**方法②：使用 `+` 直接连接**
更常用的是使用'+'操作符来连接字符串，如：

```java
"Hello," + " runoob" + "!"
```
结果如下:
`"Hello, runoob!"`

下面是一个例子:
StringDemo.java 文件代码：
```java
public class StringDemo {
    public static void main(String args[]) {     
        String string1 = "菜鸟教程网址：";     
        System.out.println("1、" + string1 + "www.runoob.com");  
    }
}
```
以上实例编译运行结果如下：
`1、菜鸟教程网址：www.runoob.com`

## 创建格式化字符串
我们知道输出格式化数字可以使用 **`printf()`** 和 **`format()`** 方法。

String 类使用 <u>静态方法 format() 返回一个 String 对象</u> 而不是 PrintStream 对象。

String 类的静态方法 format() 能用来 **创建可复用的格式化字符串**，而不仅仅是用于一次打印输出。

如下所示：
```java
System.out.printf("浮点型变量的值为 " +
                  "%f, 整型变量的值为 " +
                  " %d, 字符串变量的值为 " +
                  "is %s", floatVar, intVar, stringVar);
```
你也可以这样写

```java
String fs;
fs = String.format("浮点型变量的值为 " +
                   "%f, 整型变量的值为 " +
                   " %d, 字符串变量的值为 " +
                   " %s", floatVar, intVar, stringVar);
```

## String 方法
下面是 String 类支持的方法，更多详细，参看 [Java String API](https://www.runoob.com/manual/jdk1.6/java/lang/String.html) 文档:

方法前面的类型表示 String 对象方法的返回值



<table class="reference" style="font-family:consola; font-size:14px">
	<tbody>
		<tr>
			<th style="width:76px;">
				SN(序号)</th>
			<th style="width:501px;">
				方法描述</th>
		</tr>
		<tr>
			<td style="width:76px;">
				1</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-charat.html" target="_blank" rel="noopener noreferrer">char charAt(int index)</a><br>
				返回指定索引处的 char 值。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				2</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-compareto.html" target="_blank" rel="noopener noreferrer">int compareTo(Object o)</a><br>
				把这个字符串和另一个对象比较。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				3</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-compareto.html" target="_blank" rel="noopener noreferrer">int compareTo(String anotherString)</a><br>
				按字典顺序比较两个字符串。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				4</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-comparetoignorecase.html" target="_blank" rel="noopener noreferrer">int compareToIgnoreCase(String str)</a><br>
				按字典顺序比较两个字符串，不考虑大小写。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				5</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-concat.html" target="_blank" rel="noopener noreferrer">String concat(String str)</a><br>
				将指定字符串连接到此字符串的结尾。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				6</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-contentequals.html" target="_blank" rel="noopener noreferrer">boolean contentEquals(StringBuffer sb)</a><br>
				当且仅当字符串与指定的StringBuffer有相同顺序的字符时候返回真。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				7</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-copyvalueof.html" target="_blank" rel="noopener noreferrer">static String copyValueOf(char[] data)</a><br>
				返回指定数组中表示该字符序列的 String。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				8</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-copyvalueof.html" target="_blank" rel="noopener noreferrer">static String copyValueOf(char[] data, int offset, int count)</a><br>
				返回指定数组中表示该字符序列的 String。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				9</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-endswith.html" target="_blank" rel="noopener noreferrer">boolean endsWith(String suffix)</a><br>
				测试此字符串是否以指定的后缀结束。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				10</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-equals.html" target="_blank" rel="noopener noreferrer">boolean equals(Object anObject)</a><br>
				将此字符串与指定的对象比较。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				11</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-equalsignorecase.html" target="_blank" rel="noopener noreferrer">boolean equalsIgnoreCase(String anotherString)</a><br>
				将此 String 与另一个 String 比较，不考虑大小写。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				12</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-getbytes.html" target="_blank" rel="noopener noreferrer">byte[] getBytes()</a><br>
				&nbsp;使用平台的默认字符集将此 String 编码为 byte 序列，并将结果存储到一个新的 byte 数组中。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				13</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-getbytes.html" target="_blank" rel="noopener noreferrer">byte[] getBytes(String charsetName)</a><br>
				使用指定的字符集将此 String 编码为 byte 序列，并将结果存储到一个新的 byte 数组中。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				14</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-getchars.html" target="_blank" rel="noopener noreferrer">void getChars(int srcBegin, int srcEnd, char[] dst, int dstBegin)</a><br>
				将字符从此字符串复制到目标字符数组。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				15</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-hashcode.html" target="_blank" rel="noopener noreferrer">int hashCode()</a><br>
				返回此字符串的哈希码。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				16</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-indexof.html" target="_blank" rel="noopener noreferrer">int indexOf(int ch)</a><br>
				返回指定字符在此字符串中第一次出现处的索引。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				17</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-indexof.html" target="_blank" rel="noopener noreferrer">int indexOf(int ch, int fromIndex)</a><br>
				返回在此字符串中第一次出现指定字符处的索引，从指定的索引开始搜索。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				18</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-indexof.html" target="_blank" rel="noopener noreferrer">int indexOf(String str)</a><br>
				&nbsp;返回指定子字符串在此字符串中第一次出现处的索引。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				19</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-indexof.html" target="_blank" rel="noopener noreferrer">int indexOf(String str, int fromIndex)</a><br>
				返回指定子字符串在此字符串中第一次出现处的索引，从指定的索引开始。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				20</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-intern.html" target="_blank" rel="noopener noreferrer">String intern()</a><br>
				&nbsp;返回字符串对象的规范化表示形式。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				21</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-lastindexof.html" target="_blank" rel="noopener noreferrer">int lastIndexOf(int ch)</a><br>
				&nbsp;返回指定字符在此字符串中最后一次出现处的索引。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				22</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-lastindexof.html" target="_blank" rel="noopener noreferrer">int lastIndexOf(int ch, int fromIndex)</a><br>
				返回指定字符在此字符串中最后一次出现处的索引，从指定的索引处开始进行反向搜索。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				23</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-lastindexof.html" target="_blank" rel="noopener noreferrer">int lastIndexOf(String str)</a><br>
				返回指定子字符串在此字符串中最右边出现处的索引。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				24</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-lastindexof.html" target="_blank" rel="noopener noreferrer">int lastIndexOf(String str, int fromIndex)</a><br>
				&nbsp;返回指定子字符串在此字符串中最后一次出现处的索引，从指定的索引开始反向搜索。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				25</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-length.html" target="_blank" rel="noopener noreferrer">int length()</a><br>
				返回此字符串的长度。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				26</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-matches.html" target="_blank" rel="noopener noreferrer">boolean matches(String regex)</a><br>
				告知此字符串是否匹配给定的正则表达式。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				27</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-regionmatches.html" target="_blank" rel="noopener noreferrer">boolean regionMatches(boolean ignoreCase, int toffset, String other, int ooffset, int len)</a><br>
				测试两个字符串区域是否相等。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				28</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-regionmatches.html" target="_blank" rel="noopener noreferrer">boolean regionMatches(int toffset, String other, int ooffset, int len)</a><br>
				测试两个字符串区域是否相等。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				29</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-replace.html" target="_blank" rel="noopener noreferrer">String replace(char oldChar, char newChar)</a><br>
				返回一个新的字符串，它是通过用 newChar 替换此字符串中出现的所有 oldChar 得到的。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				30</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-replaceall.html" target="_blank" rel="noopener noreferrer">String replaceAll(String regex, String replacement)</a><br>
				使用给定的 replacement 替换此字符串所有匹配给定的正则表达式的子字符串。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				31</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-replacefirst.html" target="_blank" rel="noopener noreferrer">String replaceFirst(String regex, String replacement)</a><br>
				&nbsp;使用给定的 replacement 替换此字符串匹配给定的正则表达式的第一个子字符串。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				32</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-split.html" target="_blank" rel="noopener noreferrer">String[] split(String regex)</a><br>
				根据给定正则表达式的匹配拆分此字符串。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				33</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-split.html" target="_blank" rel="noopener noreferrer">String[] split(String regex, int limit)</a><br>
				根据匹配给定的正则表达式来拆分此字符串。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				34</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-startswith.html" target="_blank" rel="noopener noreferrer">boolean startsWith(String prefix)</a><br>
				测试此字符串是否以指定的前缀开始。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				35</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-startswith.html" target="_blank" rel="noopener noreferrer">boolean startsWith(String prefix, int toffset)</a><br>
				测试此字符串从指定索引开始的子字符串是否以指定前缀开始。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				36</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-subsequence.html" target="_blank" rel="noopener noreferrer">CharSequence subSequence(int beginIndex, int endIndex)</a><br>
				&nbsp;返回一个新的字符序列，它是此序列的一个子序列。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				37</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-substring.html" target="_blank" rel="noopener noreferrer">String substring(int beginIndex)</a><br>
				返回一个新的字符串，它是此字符串的一个子字符串。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				38</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-substring.html" target="_blank" rel="noopener noreferrer">String substring(int beginIndex, int endIndex)</a><br>
				返回一个新字符串，它是此字符串的一个子字符串。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				39</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-tochararray.html" target="_blank" rel="noopener noreferrer">char[] toCharArray()</a><br>
				将此字符串转换为一个新的字符数组。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				40</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-tolowercase.html" target="_blank" rel="noopener noreferrer">String toLowerCase()</a><br>
				使用默认语言环境的规则将此 String 中的所有字符都转换为小写。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				41</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-tolowercase.html" target="_blank" rel="noopener noreferrer">String toLowerCase(Locale locale)</a><br>
				&nbsp;使用给定 Locale 的规则将此 String 中的所有字符都转换为小写。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				42</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-tostring.html" target="_blank" rel="noopener noreferrer">String toString()</a><br>
				&nbsp;返回此对象本身（它已经是一个字符串！）。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				43</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-touppercase.html" target="_blank" rel="noopener noreferrer">String toUpperCase()</a><br>
				使用默认语言环境的规则将此 String 中的所有字符都转换为大写。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				44</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-touppercase.html" target="_blank" rel="noopener noreferrer">String toUpperCase(Locale locale)</a><br>
				使用给定 Locale 的规则将此 String 中的所有字符都转换为大写。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				45</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-trim.html" target="_blank" rel="noopener noreferrer">String trim()</a><br>
				返回字符串的副本，忽略前导空白和尾部空白。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				46</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-valueof.html" target="_blank" rel="noopener noreferrer">static String valueOf(primitive data type x)</a><br>
				返回给定data type类型x参数的字符串表示形式。</td>
		</tr>
<tr>
			<td style="width:76px;">
				47</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-contains.html" target="_blank" rel="noopener noreferrer">contains(CharSequence chars)</a><br>
				判断是否包含指定的字符系列。</td>
		</tr>
<tr>
			<td style="width:76px;">
				48</td>
			<td style="width:501px;">
				<a href="https://www.runoob.com/java/java-string-isempty.html" target="_blank" rel="noopener noreferrer">isEmpty()</a><br>
				判断字符串是否为空。</td>
		</tr>
	</tbody>
</table>





---

# StringBuffer 和 StringBuilder 类

当对字符串进行修改的时候，需要使用 **`StringBuffer`** 和 **`StringBuilder`** 类。

和 String 类不同的是，StringBuffer 和 StringBuilder 类的对象能够被多次的修改，并且 <u>不产生新的未使用对象</u>。

StringBuilder 类在 Java 5 中被提出，它和 StringBuffer 之间的最大不同
在于 **StringBuilder 的方法不是线程安全的（不能同步访问）。**
由于 StringBuilder 相较于 StringBuffer 有速度优势，
所以<u>**多数情况下建议使用 StringBuilder 类**</u>。
然而 **==在应用程序要求线程安全的情况下，则必须使用 StringBuffer 类==**。

使用 **`append()`** 方法修改 StringBuffer 字符串。
```java
public class Test{
  public static void main(String args[]){
    StringBuffer sBuffer = new StringBuffer("菜鸟教程官网：");
    sBuffer.append("www");
    sBuffer.append(".runoob");
    sBuffer.append(".com");
    System.out.println(sBuffer);  
  }
}
```
以上实例编译运行结果如下：
`菜鸟教程官网：www.runoob.com`

## StringBuffer 方法
以下是 **StringBuffer 类支持的主要方法**：

<table class="reference" style="font-family:consola; font-size:14px; ">
	<tbody style="background-color:rgb(247, 247, 247);">
		<tr>
			<th>
				序号</th>
			<th>
				方法描述</th>
		</tr>
		<tr>
			<td>
				1</td>
			<td>
				public StringBuffer <b>append</b>(String s)<br>
				将指定的字符串追加到此字符序列。</td>
		</tr>
		<tr>
			<td>
				2</td>
			<td>
				public StringBuffer <b>reverse</b>()<br>
				&nbsp;将此字符序列用其反转形式取代。</td>
		</tr>
		<tr>
			<td>
				3</td>
			<td>
				public <b>delete</b>(int start, int end)<br>
				移除此序列的子字符串中的字符。</td>
		</tr>
		<tr>
			<td>
				4</td>
			<td>
				public <b>insert</b>(int offset, int i)<br>
				将 int 参数的字符串表示形式插入此序列中。</td>
		</tr>
		<tr>
			<td>
				5</td>
			<td>
				<b>replace</b>(int start, int end, String str)<br>
				使用给定 String 中的字符替换此序列的子字符串中的字符。</td>
		</tr>
	</tbody>
</table>


下面的列表里的方法 **和 String 类的方法类似**：

<table class="reference" style="font-family:consola; font-size:14px; ">
	<tbody style="background-color:rgb(247, 247, 247);">
		<tr>
			<th style="width:64px;">
				序号</th>
			<th style="width:517px;">
				方法描述</th>
		</tr>
		<tr>
			<td style="width:64px;">
				1</td>
			<td style="width:517px;">
				int <b>capacity</b>()<br>
				返回当前容量。</td>
		</tr>
		<tr>
			<td style="width:64px;">
				2</td>
			<td style="width:517px;">
				char <b>charAt</b>(int index)<br>
				返回此序列中指定索引处的 <code>char</code> 值。</td>
		</tr>
		<tr>
			<td style="width:64px;">
				3</td>
			<td style="width:517px;">
				void <b>ensureCapacity</b>(int minimumCapacity)<br>
				确保容量至少等于指定的最小值。</td>
		</tr>
		<tr>
			<td style="width:64px;">
				4</td>
			<td style="width:517px;">
				void <b>getChars</b>(int srcBegin, int srcEnd, char[] dst, int dstBegin)<br>
				将字符从此序列复制到目标字符数组 <code>dst</code>。</td>
		</tr>
		<tr>
			<td style="width:64px;">
				5</td>
			<td style="width:517px;">
				int <b>indexOf</b>(String str)<br>
				返回第一次出现的指定子字符串在该字符串中的索引。</td>
		</tr>
		<tr>
			<td style="width:64px;">
				6</td>
			<td style="width:517px;">
				int <b>indexOf</b>(String str, int fromIndex)<br>
				从指定的索引处开始，返回第一次出现的指定子字符串在该字符串中的索引。</td>
		</tr>
		<tr>
			<td style="width:64px;">
				7</td>
			<td style="width:517px;">
				int <b>lastIndexOf</b>(String str)<br>
				返回最右边出现的指定子字符串在此字符串中的索引。</td>
		</tr>
		<tr>
			<td style="width:64px;">
				8</td>
			<td style="width:517px;">
				int <b>lastIndexOf</b>(String str, int fromIndex)<br>
返回 String 对象中子字符串最后出现的位置。</td>
		</tr>
		<tr>
			<td style="width:64px;">
				9</td>
			<td style="width:517px;">
				int <b>length</b>()<br>
				&nbsp;返回长度（字符数）。</td>
		</tr>
		<tr>
			<td style="width:64px;">
				10</td>
			<td style="width:517px;">
				void <b>setCharAt</b>(int index, char ch)<br>
				将给定索引处的字符设置为 <code>ch</code>。</td>
		</tr>
		<tr>
			<td style="width:64px;">
				11</td>
			<td style="width:517px;">
				void <b>setLength</b>(int newLength)<br>
				设置字符序列的长度。</td>
		</tr>
		<tr>
			<td style="width:64px;">
				12</td>
			<td style="width:517px;">
				CharSequence <b>subSequence</b>(int start, int end)<br>
				返回一个新的字符序列，该字符序列是此序列的子序列。</td>
		</tr>
		<tr>
			<td style="width:64px;">
				13</td>
			<td style="width:517px;">
				String <b>substring</b>(int start)<br>
				返回一个新的 <code>String</code>，它包含此字符序列当前所包含的字符子序列。</td>
		</tr>
		<tr>
			<td style="width:64px;">
				14</td>
			<td style="width:517px;">
				String <b>substring</b>(int start, int end)<br>
				返回一个新的 <code>String</code>，它包含此序列当前所包含的字符子序列。</td>
		</tr>
		<tr>
			<td style="width:64px;">
				15</td>
			<td style="width:517px;">
				String <b>toString</b>()<br>
				返回此序列中数据的字符串表示形式。</td>
		</tr>
	</tbody>
</table>


# ------------------------------------

---


# 数组
数组对于每一门编程语言来说都是重要的数据结构之一，当然不同语言对数组的实现及处理也不尽相同。

Java 语言中提供的数组是用来存储 **<u>固定大小的</u>** **<u>==同类型==</u>** 元素。

你可以声明一个数组变量，如 `numbers[100]` 来代替直接声明 100 个独立变量 `number0，number1，....，number9`9。


## 声明数组变量
首先必须声明数组变量，才能在程序中使用数组。下面是声明数组变量的语法：

```java
dataType[] arrayRefVar;   // 首选的方法
 
或
 
dataType arrayRefVar[];  // 效果相同，但不是首选方法
```

注意: 
建议使用 **`dataType[] arrayRefVar`** （**将 `[]` 括号紧跟在数组类型后**）的声明风格声明数组变量。 
`dataType arrayRefVar[]` 风格是来自 C/C++ 语言 ，在Java中采用是为了让 C/C++ 程序员能够快速理解 java 语言。

实例
下面是这两种语法的代码示例：
```java
double[] myList;         // 首选的方法
 
或
 
double myList[];         //  效果相同，但不是首选方法
```

## 创建数组
Java 语言使用 new 操作符来创建数组，语法如下：

```java
arrayRefVar = new dataType[arraySize];
```
上面的语法语句做了两件事：

- 一、使用 `dataType[arraySize]` 创建了一个数组。
- 二、把新创建的数组的引用赋值给变量 `arrayRefVar`。

**数组变量的声明，和创建数组可以用一条语句完成**，
如下所示：
```java
dataType[] arrayRefVar = new dataType[arraySize];
```
另外，你还可以使用如下的方式创建数组。
```java
dataType[] arrayRefVar = {value0, value1, ..., valuek};
```
数组的元素是通过索引访问的。数组索引从 0 开始，所以索引值从 0 到 arrayRefVar.length-1。

实例
下面的语句首先声明了一个数组变量 myList，
接着创建了一个包含 10 个 double 类型元素的数组，并且把它的引用赋值给 myList 变量。

TestArray.java 文件代码：
```java
public class TestArray {
   public static void main(String[] args) {
      // 给定数组大小
      int size = 10;
      // 定义数组
      double[] myList = new double[size];
      myList[0] = 5.6;
      myList[1] = 4.5;
      myList[2] = 3.3;
      myList[3] = 13.2;
      myList[4] = 4.0;
      myList[5] = 34.33;
      myList[6] = 34.0;
      myList[7] = 45.45;
      myList[8] = 99.993;
      myList[9] = 11123;
      // 计算所有元素的总和
      double total = 0;
      for (int i = 0; i < size; i++) {
         total += myList[i];
      }
      System.out.println("总和为： " + total);
   }
}
```
以上实例输出结果为：
`总和为： 11367.373`

下面的图片描绘了数组 myList。这里 myList 数组里有 10 个 double 元素，它的下标从 0 到 9。
![img](https://www.runoob.com/wp-content/uploads/2013/12/12-130Q0221Q5602.jpg)


## 处理数组

**==数组的元素类型和数组的大小都是确定的==**，
所以当处理数组元素时候，我们通常使用基本循环或者 `For-Each` 循环。

示例
该实例完整地展示了如何创建、初始化和操纵数组：

TestArray.java 文件代码：
```java
public class TestArray {
   public static void main(String[] args) {
      double[] myList = {1.9, 2.9, 3.4, 3.5};
 
      // 打印所有数组元素
      for (int i = 0; i < myList.length; i++) {
         System.out.println(myList[i] + " ");
      }
      // 计算所有元素的总和
      double total = 0;
      for (int i = 0; i < myList.length; i++) {
         total += myList[i];
      }
      System.out.println("Total is " + total);
      // 查找最大元素
      double max = myList[0];
      for (int i = 1; i < myList.length; i++) {
         if (myList[i] > max) max = myList[i];
      }
      System.out.println("Max is " + max);
   }
}
```
以上实例编译运行结果如下：

```html
1.9
2.9
3.4
3.5
Total is 11.7
Max is 3.5
```

### For-Each 循环

JDK 1.5 引进了一种新的循环类型，被称为 For-Each 循环或者加强型循环，
它能在 **不使用下标的情况下遍历数组**。

语法格式如下：

```java
for(type element: array)
{
    System.out.println(element);
}
```
实例
该实例用来显示数组 myList 中的所有元素：

TestArray.java 文件代码：
```java
public class TestArray {
   public static void main(String[] args) {
      double[] myList = {1.9, 2.9, 3.4, 3.5};
 
      // 打印所有数组元素
      for (double element: myList) {
         System.out.println(element);
      }
   }
}
```
以上实例编译运行结果如下：

```html
1.9
2.9
3.4
3.5
```

### 数组作为函数的参数

数组可以作为参数传递给方法。

例如，下面的例子就是一个打印 int 数组中元素的方法:

```java
public static void printArray(int[] array) {
  for (int i = 0; i < array.length; i++) {
    System.out.print(array[i] + " ");
  }
}
```
下面例子调用 printArray 方法打印出 3，1，2，6，4 和 2：
```java
printArray(new int[]{3, 1, 2, 6, 4, 2});
```

### 数组作为函数的返回值

```java
public static int[] reverse(int[] list) {
  int[] result = new int[list.length];
 
  for (int i = 0, j = result.length - 1; i < list.length; i++, j--) {
    result[j] = list[i];
  }
  return result;
}
```
以上实例中 result 数组作为函数的返回值。



## 多维数组

多维数组可以看成是数组的数组，比如二维数组就是一个特殊的一维数组，其每一个元素都是一个一维数组，例如：

String str[][] = new String[3][4];
多维数组的动态初始化（以二维数组为例）
1. 直接为每一维分配空间，格式如下：

type[][] typeName = new type[typeLength1][typeLength2];
type 可以为基本数据类型和复合数据类型，arraylength1 和 arraylength2 必须为正整数，arraylength1 为行数，arraylength2 为列数。

例如：

int a[][] = new int[2][3];
解析：

二维数组 a 可以看成一个两行三列的数组。

2. 从最高维开始，分别为每一维分配空间，例如：

String s[][] = new String[2][];
s[0] = new String[2];
s[1] = new String[3];
s[0][0] = new String("Good");
s[0][1] = new String("Luck");
s[1][0] = new String("to");
s[1][1] = new String("you");
s[1][2] = new String("!");
解析：

s[0]=new String[2] 和 s[1]=new String[3] 是为最高维分配引用空间，也就是为最高维限制其能保存数据的最长的长度，然后再为其每个数组元素单独分配空间 s0=new String("Good") 等操作。

多维数组的引用（以二维数组为例）
对二维数组中的每个元素，引用方式为 arrayName[index1][index2]，例如：

num[1][0];



# Arrays 类
java.util.Arrays 类能方便地操作数组，它提供的所有方法都是静态的。

具有以下功能：

给数组赋值：通过 fill 方法。
对数组排序：通过 sort 方法,按升序。
比较数组：通过 equals 方法比较数组中元素值是否相等。
查找数组元素：通过 binarySearch 方法能对排序好的数组进行二分查找法操作。
具体说明请查看下表：

<table class="reference" style="font-family:consola; font-size:14px; ">
	<tbody style="background-color:rgb(247, 247, 247);">
		<tr>
			<th style="width:76px;">
				序号</th>
			<th style="width:501px;">
				方法和说明</th>
		</tr>
		<tr>
			<td style="width:76px;">
				1</td>
			<td style="width:501px;">
				<strong>public static int binarySearch(Object[] a, Object key)</strong><br>
				用二分查找算法在给定数组中搜索给定值的对象(Byte,Int,double等)。数组在调用前必须排序好的。如果查找值包含在数组中，则返回搜索键的索引；否则返回 (-(<em>插入点</em>) - 1)。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				2</td>
			<td style="width:501px;">
				<strong>public static boolean equals(long[] a, long[] a2)</strong><br>
				如果两个指定的 long 型数组彼此<em>相等</em>，则返回 true。如果两个数组包含相同数量的元素，并且两个数组中的所有相应元素对都是相等的，则认为这两个数组是相等的。换句话说，如果两个数组以相同顺序包含相同的元素，则两个数组是相等的。同样的方法适用于所有的其他基本数据类型（Byte，short，Int等）。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				3</td>
			<td style="width:501px;">
				<strong>public static void fill(int[] a, int val)</strong><br>
				将指定的 int 值分配给指定 int 型数组指定范围中的每个元素。同样的方法适用于所有的其他基本数据类型（Byte，short，Int等）。</td>
		</tr>
		<tr>
			<td style="width:76px;">
				4</td>
			<td style="width:501px;">
				<strong>public static void sort(Object[] a)</strong><br>
				对指定对象数组根据其元素的自然顺序进行升序排列。同样的方法适用于所有的其他基本数据类型（Byte，short，Int等）。</td>
		</tr>
	</tbody>
</table>























