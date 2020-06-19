## 问题

修改了 model 文件之后 **`python manage.py makemigrations `** 之后出现 error


```py
(venv) [hugin@localhost hugin]$ python manage.py makemigrations database
Traceback (most recent call last):
  File "manage.py", line 15, in <module>
    execute_from_command_line(sys.argv)
  File "/home/hugin/hugin/venv/lib/python3.6/site-packages/django/core/management/__init__.py", line 381, in execute_from_command_line
    utility.execute()
  File "/home/hugin/hugin/venv/lib/python3.6/site-packages/django/core/management/__init__.py", line 375, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "/home/hugin/hugin/venv/lib/python3.6/site-packages/django/core/management/base.py", line 316, in run_from_argv
    self.execute(*args, **cmd_options)
  File "/home/hugin/hugin/venv/lib/python3.6/site-packages/django/core/management/base.py", line 350, in execute
    self.check()
  File "/home/hugin/hugin/venv/lib/python3.6/site-packages/django/core/management/base.py", line 379, in check
    include_deployment_checks=include_deployment_checks,
  File "/home/hugin/hugin/venv/lib/python3.6/site-packages/django/core/management/base.py", line 366, in _run_checks
    return checks.run_checks(**kwargs)
  File "/home/hugin/hugin/venv/lib/python3.6/site-packages/django/core/checks/registry.py", line 71, in run_checks
    new_errors = check(app_configs=app_configs)
  File "/home/hugin/hugin/venv/lib/python3.6/site-packages/django/core/checks/urls.py", line 40, in check_url_namespaces_unique
    all_namespaces = _load_all_namespaces(resolver)
  File "/home/hugin/hugin/venv/lib/python3.6/site-packages/django/core/checks/urls.py", line 57, in _load_all_namespaces
    url_patterns = getattr(resolver, 'url_patterns', [])
  File "/home/hugin/hugin/venv/lib/python3.6/site-packages/django/utils/functional.py", line 37, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/home/hugin/hugin/venv/lib/python3.6/site-packages/django/urls/resolvers.py", line 533, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
  File "/home/hugin/hugin/venv/lib/python3.6/site-packages/django/utils/functional.py", line 37, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/home/hugin/hugin/venv/lib/python3.6/site-packages/django/urls/resolvers.py", line 526, in urlconf_module
    return import_module(self.urlconf_name)
  File "/usr/python3.64/lib/python3.6/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "/home/hugin/hugin/hugin/hugin/urls.py", line 11, in <module>
    path('ssh_telnet/', include('ssh_telnet.urls')),
  File "/home/hugin/hugin/venv/lib/python3.6/site-packages/django/urls/conf.py", line 34, in include
    urlconf_module = import_module(urlconf_module)
  File "/usr/python3.64/lib/python3.6/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "/home/hugin/hugin/hugin/ssh_telnet/urls.py", line 2, in <module>
    from . import views
  File "/home/hugin/hugin/hugin/ssh_telnet/views.py", line 8, in <module>
    import uwsgi
ModuleNotFoundError: No module named 'uwsgi'
```

真的阿西吧！在 nginx + uwsgi 里面明明就运行得很好，而且这个模块用了很久了，也没有 log，真是气死人了。


## Reason


下面这段出自 [官网](https://uwsgi-docs.readthedocs.io/en/latest/PythonModule.html?highlight=import%20uwsgi)

```
The uWSGI server automagically adds a uwsgi module into your Python apps.

This is useful for configuring the uWSGI server, use its internal functions and get statistics. Also useful for detecting whether you’re actually running under uWSGI; 
if you attempt to import uwsgi and receive an ImportError you’re not running under uWSGI.
```
uWSGI server 会自动将 uwsgi 模块加入我们的 python app 中(当然你要用还是需要 Import 的)

**`if you attempt to import uwsgi and receive an ImportError you’re not running under uWSGI.`**

最后一句告诉我们如果你要用 `import uwsgi`，那一定要在有 uWSGI server 的环境中，否则会扔个 **ImportError** 给你。

这就可以说明为什么我在 uwsgi + nginx 的环境下可以正常执行 uwsgi 相关的 app，但是在 python manage.py 执行指令就一定会报出 **`ModuleNotFoundError: No module named 'uwsgi'`**, 因为在 python manage.py 运行没有给 uWSGI server 的环境


## Solution

参考：[link](https://stackoverflow.com/questions/30142267/cannot-use-manage-py-because-of-uwsgi-import-in-settings-py?r=SearchResults)

setting.py 注释使用了 uwsgi module 的 APP，url.py 注释使用了 uwsgi module 的 APP 路径。
然后再运行 `python manage.py`

如果嫌麻烦，就另写一份 setting.py 作为 DEBUG 使用，运行 manage.py 的时候使用 --setting 参数指定

或者


```
try:
    import uwsgi
except ImportError:
    pass
```


## 参考

[uWSGI之ImportError: No module named uwsgi](https://www.cnblogs.com/lazyboy/archive/2013/06/03/3115451.html)
[Cannot use manage.py because of uwsgi import in settings.py](https://stackoverflow.com/questions/30142267/cannot-use-manage-py-because-of-uwsgi-import-in-settings-py?r=SearchResults)