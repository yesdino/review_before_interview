**①. HTTPResponse**

是由 Django 创建的，他的返回格式为 
**`HTTPResponse(content=响应体, content_type=响应体数据类型, status=状态码)`** ，
可以修改返回的数据类型，
适用于返回 <u>图片，视频，音频</u> 等二进制文件

**②. JsonReponse** 

是 HTTPResponse 的子类，
**适用于处理 json 格式的数据**，但是不能返回模板。

帮助我们将数据转换为 json 字符串
设置响应头 `Content-Type` 为 **`application/json`**

**③. Response**

是 **Django-rest-Framework** 框架中封装好的响应对象，他的返回格式为 
**`Response(data, status=None, template_name=None, headers=None, content_type=None)`** 

data 只需传递 python 的内建类型数据即可，
如果是 Django 的模型类对象，那么就使用序列化将数据（ python 的字典数据）传递给 data 。


---
作者：咏远瑞智
链接：https://www.jianshu.com/p/d8fca63d42b1
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。