# logging 日志打印

## 介绍

### Logger
用户使用的直接接口，将日志传递给Handler



### Handler
**`class`** 控制日志输出到哪里
- **`logging.StreamHandler`**：	指定向流对象进行
- **`logging.FileHandler`**：	指定文件
- **`logging.handlers.RotaingFileHandler`**：	指定文件，但可管理文件大小，当超过指定值后则重新创建日志文件
- **`logging.handlers.TimedRotatingFileHandler`**：	指定文件，超过指定周期后重新创建日志文件
- **`logging.handlers.SocketHandler`**：	指定socket
- **`logging.handlers.SyslogHandler`**：	指定syslog服务器
- **`logging.handlers.HTTPHandler`**：	使用post/get请求提交数据到web服务器
<br>

一个logger可以有多个Handler。用户可自定义 logger 也可使用内建的 logger：
- **`django`**： 不要使用这个记录器，用下面的。这是一个被供起来的记录器，^-^
- **`django.request`**： 记录与处理请求相关的消息。5XX错误被记录为ERROR消息；4XX错误记录- **`为WARNING消息。接收额外参数：status_code和request
- **`django.server`**： 记录开发服务器下处理请求相关的消息。只用于开发阶段。
- **`django.template`**: 记录与渲染模板相关的日志。
- **`django.db.backends`**: 与数据库交互的代码相关的消息。
- **`django.security`**： 记录任何与安全相关的错误。
- **`django.security.csrf`**： 记录CSRF验证失败日志。
- **`django.db.backends.schema`**： 记录查询导致数据库修改的日志。

### Filter
控制哪些日志可以从 logger 流向 Handler

Django还额外提供两个过滤器。

- **`CallbackFilter(callback)[source]`**：这个过滤器接受一个回调函数，并对每个传递给过滤器的记录调用它。如果回调函数返回False，将不会进行记录的处理。

- **`RequireDebugFalse[source]`**： 这个过滤器只会在settings.DEBUG==False时传递。

### Formatter
控制日志的格式

|参数	|说明|
|:---|:---|
| **`%(name)s`**    |	Logger的名字|
| **`%(levelno)s`**    |		数字日志级别
| **`%(levelname)s`**    |		文本日志级别
| **`%(pathname)s`**    |		调用日志输出函数的模块文件路径
| **`%(filenames)s`**    |		调用日志输出函数的模块文件名
| **`%(module)s`**    |		调用日志输出函数的模块名
| **`%(funcName)s`**    |		调用日志输出函数的函数名
| **`%(lineno)d`**    |		调用日志输出函数语句所在行号
| **`%(created)f`**    |		当前时间
| **`%(relativeCreated)d`**    |		当前时间
| **`%(asctime)s`**    |		当前时间,格式’2015-05-28 20:50:03,345’
| **`%(thread)d`**    |		线程id
| **`%(threadName)s`**    |		线程名
| **`%(process)d`**    |		进程id
| **`%（message)s`**    |		消息


## 日志记录错误等级


CRITICAL：重大错误
ERROR：系统里有错误
WARNING：警告
INFO：正常打印日志
DEBUG：调试信息

CRITICAL > ERROR > WARNING > INFO>DEBUG


## 示例说明

- 1、首先需要安装 logging
```
pip install logging
```

- 2、添加 logging.py 配置

以下 logging 配置可直接添加到 django project setting.py 中使用。
```py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
       'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d]  \
                        [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'
        },
        'simple': {
            'format': '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
        }
    },
    'handlers': {
        'default': {
            'level': 'WARNING',                             # 要打印系统运行信息是设为'DEBUG'
            'filename': 'logging.log',                      # log file name
            'class': 'logging.handlers.RotatingFileHandler',# 将日志消息写入文件filename
            'maxBytes': 1024 * 1024 * 5,                    # 日誌文件大小 如果文件的大小超出 maxBytes 值，那么它将被备份为filename1
            'backupCount': 5,
            'formatter': 'simple'
        },
        'error':{
            'level': 'ERROR',
            'filename': 'error.log',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard'
        },
        'development':{
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'development.log',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'simple'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['default', 'error'],   # 进入此 logger 的日志都会输出到的 handlers
            'level': 'DEBUG',                   # 进入此 logger 的最低级别
            'propagate': False                  # propagate 向不向更高級別的 loggers 傳遞
        },
        'django_development': {
            'handlers': ['development', 'error'],
            'level': 'DEBUG',
            'propagate': False
        },
    },
}
```

- 3、在 view.py 中使用

定义 logger

```py
import logging

logger = logging.getLogger("django_development") # 为loggers中定义的名称
```

在需要打印 log 信息的位置：
```py
logger.debug("some debug...")
logger.info("some info...")
logger.warning("some warning...")
logger.error("some error...")
logger.critical("some critical...")
```

logger 根据传入的不同的 key 定义不同的 logger，如上述设置：
`django_development` 定义的 logger 将打印 Info 级别以上的日志信息到文件 development.log 和 error.log；
`django` 定义的 logger 将只打印 Warning 级别以上的日志信息到文件 logging.log 和 error.log。

