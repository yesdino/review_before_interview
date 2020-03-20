[toc]

---

## setting.py
```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cmdb',
    'channels', #注册app
]

ASGI_APPLICATION = 'devops.routing.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('10.1.210.33', 6379)],   # 需修改
        },
    },
}
```


在项目 settings 文件同级目录中新增 routing.py
```py
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:wd

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import deploy.routing

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            # 指明路由文件是 devops/routing.py
            deploy.routing.websocket_urlpatterns
        )
    ),
})
```

devops 下的 routing.py
```py
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:wd
from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    # consumers.DeployResult 是该路由的消费者
    url(r'^ws/deploy/(?P<service_name>[^/]+)/$', consumers.DeployResult), 
]
```

## 编写webscoket消息处理方法(消费者)
deploy/consumers.py：
```py
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:wd

from channels.generic.websocket import AsyncWebsocketConsumer
import json

class DeployResult(AsyncWebsocketConsumer):
    async def connect(self):
        self.service_uid = self.scope["url_route"]["kwargs"]["service_uid"]
        self.chat_group_name = 'chat_{}'.format(self.service_uid)
        # 收到连接时候处理
        await self.channel_layer.group_add(self.chat_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # 关闭 channel 时候处理
        await self.channel_layer.group_discard(
            self.chat_group_name,
            self.channel_name
        )

    # 收到消息
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print("收到消息--》",message)
        # 发送消息到组
        await self.channel_layer.group_send(
            self.chat_group_name,
            {
                'type': 'client.message',
                'message': message
            }
        )

    # 处理客户端发来的消息
    async def client_message(self, event):
        message = event['message']
        print("发送消息。。。",message)
        # 发送消息到 WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
```

## 前端 js 发起 websocket 请求
```js
function InitWebSocket() {
    var websocket = new WebSocket( 
        'ws://' + window.location.host + '/ws/deploy/tasks/' );

    websocket.onmessage = function (e) {
        var data = JSON.parse(e.data);
        var message = '\n' + data['message'];
        document.querySelector('#deploy-res').innerText += (message + '\n');
    };
}
```

## 发送消息到 channel
无论是消息的推送或者消息的接受，都是经过 channel layer 进行传输，以下是发送消息示例，
```py
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

channel_layer = get_channel_layer()
def send_channel_msg(channel_name, msg):
     """
    send msg to channel
    :param channel_name: 
    :param msg: 
    :return: 
    """
    # channel_layer.group_send(channel_name, {"type": "deploy.run", "text": msg})   # 其实执行的是这句
    async_to_sync(channel_layer.group_send)(channel_name, {"type": "deploy.run", "text": msg})
```

## 生产部署
大多数django的应用部署方式都采用的是nginx+uwsgi进行部署，当django集成channels时候，由于uwsgi不能处理websocket请求，所以我们需要asgi服务器来处理websocket请求，官方推荐使用daphne。下一篇文章将介绍nginx+supervisor+daphne+uwsgi进行生产部署。





---

- 参考：

[django实时通讯--channels2.x使用](https://www.cnblogs.com/wdliu/p/10028236.html)

- 接下来部署 dapgne + supervisor 参考：

[django+uwsgi+daphne+supervisor生产环境部署](https://www.cnblogs.com/wdliu/p/10032180.html)

[Django使用Channels实现WebSocket消息通知功能](https://www.jianshu.com/p/0f75e2623418)