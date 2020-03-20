# python string 字符串内置函数
## 格式化字符串
| ||
| :------|:------|
|string.  <b>format</b>()<br>       |格式化字符串|
|string.  <b>lower</b>()<br>        |转换 string 中所有大写字符为==小写==.  
|string. <b>upper</b>()<br>         |转换 string 中的小写字母为==大写==
|string. <b>swapcase</b>()<br>      |==翻转== string 中的==大小写==
|string.  <b>capitalize</b>() <br>  |把字符串的==第一个字符大写==
|string.  <b>join</b>(seq)<br>      |以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
|string.  <b>replace</b>(str1, str2,  num=string.count(str1))|把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次.
|string. <b>translate</b>(str, del="")<br>    |根据 str 给出的表(包含 256 个字符)转换 string 的字符,要过滤掉的字符放到 del 参数中

---
## 搜索
| ||
| :------|:------|
|<b>max</b>(str)<br>                |返回字符串 str 中最大的字母。
|<b>min</b>(str)<br>                |返回字符串 str 中最小的字母。
|string. <b>find</b>(str, beg=0, end=len(string))<br>       |检测 str 是否包含在 string 中，<br>如果 beg 和 end 指定范围，则检查是否包含在指定范围内，<br>如果是返回开始的索引值，否则返回-1
|string. <b>rfind</b>(str, beg=0,end=len(string) )<br>      |类似于 find()函数，不过是从右边开始查找.
|string. <b>index</b>(str, beg=0, end=len(string))<br>      |跟find()方法一样，只不过如果str不在 string中会报一个异常.
|string. <b>rindex</b>( str, beg=0,end=len(string))<br>    |类似于 index()，不过是从右边开始.
|string. <b>split</b>(str="", num=string.count(str))<br>    |以 str 为分隔符切片 string，如果 num 有指定值，则仅分隔 num+ 个子字符串
|string. <b>partition</b>(str)<br>                          |有点像 find()和 split()的结合体,<br>从 str 出现的第一个位置起, <br>把字符串 string 分成一个3元素的元组(string_pre_str,str,string_post_str),<br>如果 string 中不包含str 则 string_pre_str == string.
|string. <b>rpartition</b>(str)<br>                         |类似于 partition()函数,不过是从右边开始查找
|string. <b>count</b>(str, beg=0, end=len(string))<br>      |返回 str 在 string 里面出现的次数，<br>如果 beg 或者 end 指定则返回指定范围内 str 出现的次数

---
## 检验是否为某格式的字符串
| | |
| :------|:------|
|string. <b>isalnum</b>()<br>   | string 是否 **至少有一个字符并且所有字符都是字母或数字**，是返回 True 否返回 False
|string. <b>isalpha</b>()<br>   | string 是否 **至少有一个字符并且所有字符都是字母**，是返回 True 否返回 False
|string. <b>isdecimal</b>()<br> | string 是否 **只包含十进制数字**，是返回 True 否返回 False
|string. <b>isdigit</b>()<br>   | string 是否 **只包含数字**，是返回 True 否返回 False
|string. <b>islower</b>()<br>   | string 是否 **至少包含一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写**，是返回 True 否返回 False
|string. <b>isupper</b>()<br>   | string 是否 **至少包含一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写**，是返回 True 否返回 False
|string. <b>isnumeric</b>()<br> | string 是否 **只包含数字字符**，是返回 True 否返回 False
|string. <b>isspace</b>()<br>   | string 是否 **只包含空格**，是返回 True 否返回 False
|string. <b>istitle</b>()<br>   | string 是否 是标题化的(见 title())，是返回 True 否返回 False
|string. <b>startswith</b>(obj, beg=0,end=len(string))<br>  |检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。<br>如果beg 和 end 指定值，则在指定范围内检查.
|string. <b>endswith</b>(obj, beg=0, end=len(string))<br>   | string是否  **以 obj 结束**，若beg 或者 end 指定则检查指定的范围内是否以 obj 结束，<br>是返回 True 否返回 False

---
## 对齐
| ||
| :------| :------|
|string. <b>center</b>(width)<br>   |返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
|string. <b>ljust</b>(width)<br>    |返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
|string. <b>rjust</b>(width)<br>    |返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
|string. <b>zfill</b>(width)<br>    |返回长度为 width 的字符串，原字符串 string 右对齐，前面填充0


---
## 其他
| ||
| :------|:------|
|string. <b>decode</b>(encoding='UTF-8', errors='strict')<br>    |以 encoding 指定的编码格式解码 string，如果出错默认报一个 ValueError 的 异 常 ， 除非 errors 指 定 的 是 'ignore' 或 者'replace'
|string. <b>encode</b>(encoding='UTF-8', errors='strict')<br>    |以 encoding 指定的编码格式编码 string，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
|string. <b>maketrans</b>(intab, outtab])<br>                   |maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
|string. <b>splitlines</b>([keepends])<br>                      |按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
|string. <b>title</b>()<br>         |返回"标题化"的 string,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())










