普通用户下无法运行 pip3 命令
```py
[dino@localhost Pro]$ pip3
bash: pip3: command not found...
[dino@localhost Pro]$ python3
Python 3.6.4 (default, Jun 13 2019, 09:28:06)
[GCC 4.8.5 20150623 (Red Hat 4.8.5-36)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
[dino@localhost Pro]$ ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
ln: failed to create symbolic link ‘/usr/bin/pip3’: Permission denied
[dino@localhost Pro]$ su root
Password:
su: Authentication failure
[dino@localhost Pro]$ ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
ln: failed to create symbolic link ‘/usr/bin/pip3’: Permission denied
```
进入 root 用户创建软链接
```
[dino@localhost Pro]$ su root
Password:
[root@localhost Pro]# ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
[root@localhost Pro]# pip3
```
正常。

root 下安装 cookiecutter（普通用户下安装显示permission deniey）。
```
pip3 install cookiecutter
```
安装完毕后回到普通用户
```
[root@localhost Pro]# exit
exit
[dino@localhost Pro]$ cookiecutter
bash: cookiecutter: command not found...
```
- 方法1：去 cookiecutter 安装路径下执行指令
```
[dino@localhost Pro]$ /usr/local/python3/bin/cookiecutter
Usage: cookiecutter [OPTIONS] TEMPLATE [EXTRA_CONTEXT]...
Try "cookiecutter -h" for help.

Error: Missing argument "TEMPLATE".
```
- 方法2：root用户创建软链接，回到普通用户
```
[dino@localhost Pro]$ su root
Password:
[root@localhost Pro]# ln -s /usr/local/python3/bin/cookiecutter /usr/bin/cookiecutter
[root@localhost Pro]# cookiecutter
Usage: cookiecutter [OPTIONS] TEMPLATE [EXTRA_CONTEXT]...
Try "cookiecutter -h" for help.

Error: Missing argument "TEMPLATE".

[root@localhost Pro]# exit
exit
[dino@localhost Pro]$ 
```

在 github 下载 cookiecutter-django：在你想创建项目的目录下执行指令：

```
cookiecutter https://github.com/pydanny/cookiecutter-django.git
```

```
[dino@localhost Pro]$ cookiecutter https://github.com/pydanny/cookiecutter-django.git
project_name [My Awesome Project]: zhanhu
project_slug [zhanhu]:
description [Behold My Awesome Project!]: a Q&A website
author_name [Daniel Roy Greenfeld]: __dino__
domain_name [example.com]:
email [__dino__@example.com]:
version [0.1.0]:
Select open_source_license:
1 - MIT
2 - BSD
3 - GPLv3
4 - Apache Software License 2.0
5 - Not open source
Choose from 1, 2, 3, 4, 5 (1, 2, 3, 4, 5) [1]: 5
timezone [UTC]: Aisa/Shanghai
windows [n]:
use_pycharm [n]: y
use_docker [n]:
Select postgresql_version:
1 - 11.3
2 - 10.8
3 - 9.6
4 - 9.5
5 - 9.4
Choose from 1, 2, 3, 4, 5 (1, 2, 3, 4, 5) [1]: 1
Select js_task_runner:
1 - None
2 - Gulp
Choose from 1, 2 (1, 2) [1]:
Select cloud_provider:
1 - AWS
2 - GCP
3 - None
Choose from 1, 2, 3 (1, 2, 3) [1]:
custom_bootstrap_compilation [n]:
use_compressor [n]: y
use_celery [n]: y
use_mailhog [n]:
use_sentry [n]:
use_whitenoise [n]:
use_heroku [n]:
use_travisci [n]:
keep_local_envs_in_vcs [y]:
debug [n]: y
 [INFO]: .env(s) are only utilized when Docker Compose and/or Heroku support is enabled so keeping them does not make sense given your current setup.
 [SUCCESS]: Project initialized, keep up the good work!
[dino@localhost Pro]$ ls
djangoEnterprisePro1  djangoPro1  scrapyPro1  tornadoPro1  zhanhu
```





创建 pipenv 虚拟环境（由于系统没有装python3.7，所以改成了系统装的3.6）
```
[dino@localhost zhanhu]$ pipenv --python 3.6
Creating a virtualenv for this project…
Pipfile: /home/dino/Pro/zhanhu/Pipfile
Using /usr/bin/python3 (3.6.4) to create virtualenv…
⠙ Creating virtual environment...Using base prefix '/usr/local/python3'
New python executable in /home/dino/.local/share/virtualenvs/zhanhu-R6eiX4BI/bin/python3
Also creating executable in /home/dino/.local/share/virtualenvs/zhanhu-R6eiX4BI/bin/python
Installing setuptools, pip, wheel...
done.
Running virtualenv with interpreter /usr/bin/python3
✔ Successfully created virtual environment!
Virtualenv location: /home/dino/.local/share/virtualenvs/zhanhu-R6eiX4BI
Creating a Pipfile for this project…
```
记住这个路径，是项目的虚拟环境路径

```
Virtualenv location: /home/dino/.local/share/virtualenvs/zhanhu-R6eiX4BI
```
进入这个目录可以看到已经建好了 python 对应的文件夹
```
[dino@localhost zhanhu]$ cd /home/dino/.local/share/virtualenvs/zhanhu-R6eiX4BI
[dino@localhost zhanhu-R6eiX4BI]$ ll
total 4
drwxrwxr-x. 2 dino dino 4096 Jun 15 15:02 bin
drwxrwxr-x. 2 dino dino   24 Jun 15 15:02 include
drwxrwxr-x. 3 dino dino   23 Jun 15 15:02 lib
```
如果要安装任何的模块，只需要去到我们安装虚拟环境的项目目录，用 pipenv 指令安装即可。（安装可能会稍慢，因为把 pip 源修改为国内的）

```
[dino@localhost ~]$ cd /home/dino/Pro/zhanhu/
[dino@localhost zhanhu]$ ls
config  docs  locale  manage.py  Pipfile  pytest.ini  README.rst  requirements  setup.cfg  utility  zhanhu
[dino@localhost zhanhu]$ pipenv install django
Installing django…
✔ Installation Succeeded
Pipfile.lock not found, creating…
Locking [dev-packages] dependencies…
Locking [packages] dependencies…
✔ Success!
Updated Pipfile.lock (85c883)!
Installing dependencies from Pipfile.lock (85c883)…
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 3/3 — 00:00:06
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
```

```
[dino@localhost zhanhu]$ ls
config  docs  locale  manage.py  Pipfile  Pipfile.lock  pytest.ini  README.rst  requirements  setup.cfg  utility  zhanhu
[dino@localhost zhanhu]$ vim Pipfile
```
把pip源改成国内的（改了之后不能下载了，有可能是办公室的网络问题，看情况跳过这一步吧。反正不改也不怎么慢。）
```
[[source]]
name = "pypi"
# url = "https://pypi.org/simple"
url = "https://mirrors.aliyum.com/pypi/simple"
verify_ssl = true

[dev-packages]
# 开发环境中需要用到的包

[packages]
django = "*"
# 生成环境需要用到的包

[requires]
python_version = "3.6"
```
Pipfile.lock 文件中记录的是一些哈希值和使用的包，可以暴露安全问题，如果我们的值被别人篡改过了可以看得到

`pipenv graph` 可以查看包与包之间的依赖关系
```
[dino@localhost zhanhu]$ pipenv graph
Django==2.2.2
  - pytz [required: Any, installed: 2019.1]
  - sqlparse [required: Any, installed: 0.3.0]
```

我们每次 `pipenv install django` 时它都会去更新 `Pipfile  Pipfile.lock` 这两个文件。

但我们可以使用指令`--skip-lock`跳过他们，在最后项目开发完了再来更新 lock 文件的哈希值。

```
[dino@localhost zhanhu]$ pipenv install requests --skip-lock
Installing requests…
✔ Installation Succeeded
Installing dependencies from Pipfile…
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 2/2 — 00:00:06
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
```

pipenv 还可以区别安装生产环境和开发环境各自使用的包。

比如开发环境想要安装某个模块
```
pipenv install --dev 模块名 --skip-lock
```
它会在 Pipfile 的 `[dev-packages]` 下面自动生成模块对应的设置

还有一些其他指令

```
pipenv --where  # 定位项目路径
pipenv --venv   # 定位虚拟环境保存的路径
pipenv --py     # 解释器的路径
pipenv update   # 更新目前安装的所有的包到最新的版本
pipenv check    # 检查漏洞
pipenv --rm     # 删除虚拟环境
```








