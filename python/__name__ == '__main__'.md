原文：
https://www.cnblogs.com/kex1n/p/5975575.html

python 中__name__ = '__main__' 的作用，到底干嘛的？

有句话经典的概括了这段代码的意义：

“Make a script both importable and executable”

意思就是说 **让你写的脚本模块既可以导入到别的模块中用，另外该模块自己也可执行**。

这句话，可能一开始听的还不是很懂。下面举例说明：
先写一个模块：
```py
#module.py
def main():
    print "we are in %s"%__name__

if __name__ == '__main__':
    main()


# 本身执行该py文件 输出:
# we are in __main__

# 但如果从另我一个模块导入该模块，并调用 main() 函数 输出：
# we are in module
# 也就是说模块__name__ = '__main__' 下面的函数没有执行
```

**==这样既可以让“模块”文件运行，也可以被其他模块引入，而且不会执行函数2次==**。这才是关键。

 

### 总结：

如果我们是直接执行某个.py文件的时候，该文件中那么`__name__ == '__main__'`是`True`,但是我们如果从另外一个.py文件通过`import`导入该文件的时候，这时`__name__`的值就是我们这个`py文件的名字`而不是`__main__`。

这个功能还有一个用处：
调试代码的时候，在`if __name__ == '__main__'`中加入一些我们的 **==调试代码==**<br>我们可以让外部模块调用的时候不执行我们的调试代码<br>但是如果我们想排查问题的时候，直接执行该模块文件，调试代码能够正常运行！<br>


当你打开一个`.py文件`时,经常会在代码的最下面看到`if __name__ == '__main__':`

#### `if __name__ == '__main__'`的作用:
- ==模块是对象==，并且所有的模块都有一个内置属性 `__name__`。
- ==一个模块的 `__name__` 的值取决于您如何应用模块==。
  - 如果 import 一个模块，那么模块`__name__` 的值通常为模块文件名，不带路径或者文件扩展名。
  - 但是您也可以像一个标准的程序样直接运行模块，在这 种情况下, `__name__` 的值将是一个特别缺省`__main__`。



<br>

- 在cmd 中直接运行.py文件,则 `__name__`的值是`__main__`;

- 而在import 一个.py文件后,`__name__`的值就不是`__main__`了;

<u>==从而用`if __name__ == '__main__'`来判断是否是在直接运行该.py文件==</u>

如:
```py
#Test.py
class Test:
    def __init(self):pass
    def f(self):print 'Hello, World!'

if __name__ == '__main__':
    Test().f()

#End
```
 

你在cmd中输入:
```py
C:>python Test.py

Hello, World!
```
说明:`__name__ == '__main__'`是成立的

 

你再在cmd中输入:
```py
C:>python

>>>import Test
>>>Test.__name__                #Test模块的__name__
'Test'

>>>__name__                       #当前程序的__name__
'__main__'
```
无论怎样,Test.py中的"__name__ == '__main__'"都不会成立的!

所以,下一行代码永远不会运行到!