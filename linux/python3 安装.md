
[参考](https://www.cnblogs.com/kimyeee/p/7250560.html)

安装 python3 时，不要覆盖原环境的 python2。因为环境中有些程序是依赖 2 的，比如 yum。直接覆盖是会影响环境的。
最好的是编译安装 python3，执行指令是用 python3 作为指令区别 python(2) 来下指令。

# 1. 安装依赖
```
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
```
如果这一步没做好，后面会对 pip install 安装功能造成影响

# 2. 下载安装 python3
安装位置看个人喜好，这里假设 `/usr/local/python3`

- **下载**

```py
# 这个指令执行位置即下载位置
wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tgz
```
- **解压**
```
tar -zxvf Python-3.6.1.tgz
```

# 3. 编译安装
进入解压后目录
```
cd Python-3.6.1
```
编译安装，--prefix后路径为安装位置
```
./configure --prefix=/usr/local/python3     
make && make install
```
如果后面执行时出行错误，显示缺少某个模块时，要重新执行【编译安装】步骤


# 4. 建立 python3 的软链
这一步是为了区分 python3 和 python
如果不执行这一步，后面下 python3 指令时，将报错：`python3: command not found`

```
ln -s /usr/local/python3/bin/python3 /usr/bin/python3
```
假如重新编译安装 python3 换了安装位置，安装完了之后执行这步出现错误：`ln: python3: file exit`
则执行:

```
ln -snf /usr/local/python3/bin/python3 /usr/bin/python3
```
参数 `-snf` 表示覆盖

# 5. 将/usr/local/python3/bin加入PATH
此文件开机执行
```py
# vim ~/.bash_profile

# .bash_profile
# Get the aliases and functions
if [ -f ~/.bashrc ]; then
. ~/.bashrc
fi
# User specific environment and startup programs
PATH=$PATH:$HOME/bin:/usr/local/python3/bin
export PATH
```
编译文件
```
source ~/.bash_profile
```
安装完成，检查 python3, pip3 执行是否有效。
如果 pip3 无效，创建一下软链接：
```
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
```

# 6. 解决缺少模块报错

检查 pip3 是否能正常安装模块：
```
pip3 install paramiko
```
最常出现的报错是缺少 ssl 模块。
```
pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.
```
这是由于前面安装依赖环境的时候没做，缺少 ssl 依赖。
那就补安装这个模块
```
yum install openssl
yum install openssl-devel
```
安装完了之后要重新执行第 3 步编译安装 python3 环境，将新安装的模块兼容进 python3 的安装环境中
```
cd Python-3.6.1
./configure --prefix=/usr/local/python3     
make && make install
```

[参考原文](https://www.cnblogs.com/kimyeee/p/7250560.html)中还有缺少`setuptools`模块和安装`pip`模块的步骤，有遇到相关问题的点进去看就行。
<br>


**基本思路：**<u>
看它的报错里面写的缺少的是什么模块，就去补安装什么模块。
安装完了要重新执行第 3 步编译安装 python3 环境，将新安装的模块兼容进 python3 的安装环境中</u>


# 7. 快速安装步骤
照着下指令就行，大概率不会出错。
先进入存放下载安装包的目录
```py
# 安装依赖
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
# 下载安装包，如果已经有了跳过这步
wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tgz
tar -zxvf Python-3.6.1.tgz
cd Python-3.6.1
# 编译安装
./configure --prefix=/usr/local/python3
make && make install
# 写软链接
ln -s /usr/local/python3/bin/python3 /usr/bin/python3
# 加入 PATH
vim ~/.bash_profile
# PATH=$PATH:$HOME/bin:/usr/local/python3/bin
source ~/.bash_profile
# 安装完毕
python3, pip3 检查
pip3 install paramiko 检查
```





