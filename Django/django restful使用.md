原文：
https://blog.csdn.net/haeasringnar/article/details/80849945


## 依赖
本文开发环境：
```
python3.6
django2.0.6
djangorestframework3.8.2
```
值得注意的是要使用django restful并且和数据交互你还需要的必要软件和依赖：
依赖：
```
pymysql
django-filter
coreapi
Markdown
django-crispy-forms
django-guardian
```
软件：
```
Navicat
Postman
```


## 开始工作

首先新建好django项目，并新建一个app；
### 1、设置settings
```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'newapp.apps.NewappConfig', # 添加你自己的app，这里是我的app demo
    'rest_framework'            # 这个就是rest framework的配置
]
DEBUG = True # 开启debug模式

ALLOWED_HOSTS = ['*']           # 允许所有IP访问
# 下面的配置是解决跨域的问题
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS= True
CORS_ALLOW_HEADERS = ('*')
# 下面是配置MySql的链接
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'drfaeademo',
        'USER':'root',
        'PASSWORD':'你的密码',
        'HOST':'你的数据库地址',
        'PORT':'你的数据库端口',
    }
}
```

### 2、配置项目根urls
```py
from django.conf.urls import include,url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^newapp/',include('newapp.urls')) 
]
```
### 3、开始新建模型
```py
from django.db import models

class Student(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100,default='')
    describe = models.CharField(max_length=500,default='')
    isDelete = models.BooleanField(default=False)

    # Model 元数据就是 "不是一个字段的任何数据" -- 比如排序选项, admin 选项等等.
    # 通过一个内嵌类 "class Meta" 给你的 model 定义元数据,
    # 这里表示的是默认使用created这个字段进行排序。
    class Meta:
        # 重新定义表名.

        db_table = 'student_table'

class course(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100,default='')
    describe = models.CharField(max_length=500,default='')
    isDelete = models.BooleanField(default=False)
    student = models.ForeignKey(Student,on_delete=models.CASCADE,default=None)

    class Meta:
        db_table = 'course_table'
```
写完模型文件之后，要进行数据迁移

### 4、然后开始写 serializers.py

注意：这个文件是 **drf(django rest framework)** 的必要序列化器，它的作用就是将我们查出来的模型数据进行序列化，这样一来我们能很方便的返回json数据。
当然有些小伙伴就会问为什么不直接用json包来序列化数据呢？
因为**json处理数据时日期类型的是无法序列化的**，会报错，细心的小伙伴肯定早就发现了。
回到正文如果你没有这个文件，请先建立一个。然后：
```py
#导入相关的包
from rest_framework import serializers
from newapp.models import Student,course

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = ('name','describe','price')
        fields = '__all__'  #将所有的字段都序列化
        # 注意serializers是可以进行嵌套输出的非常简单

class CoursesSerializer(serializers.ModelSerializer):
    student = StudentsSerializer()

    class Meta:
        model = course
        # fields = ('name','describe','price')
        fields = '__all__'  #这个是将所有的字段都序列化
```

### 5、配置路由逻辑 views.py
```py
from rest_framework.response import Response
from rest_framework.views import APIView    # 使用 APIview 的方法
from rest_framework import status   # 导入状态码相关包
from rest_framework.pagination import PageNumberPagination  # 分页
from newapp.serializers import StudentsSerializer,CoursesSerializer
from newapp.models import Student,course
import json


# 使用自定义的分页类
class MyPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"
    page_query_param = 'page'
    max_page_size = 100


class StudentsApiView(APIView):

    def get(self,request,format=None):
        """
        获取具体ID的数据的操作
        """
        print(request.GET.get('id'))
        print(request.META.get('HTTP_TOKEN'))
        if request.GET.get('id'):
            id = request.GET.get('id')
            students = Student.objects.filter(id=id).filter(isDelete=False) # 获取指定的资源并加上没有删除的条件
            print(students)
        else:
            students = Student.objects.all().filter(isDelete=False) # 获取所有的数据，并筛选出没有删除的数据

        json_data = {
            "message": "ok", 
            "errorCode": 0
        }
        pg = MyPageNumberPagination()   # 分页
        page_roles = pg.paginate_queryset(queryset=students, request=request, view=self)
        serializer = StudentsSerializer(instance=page_roles, many=True)
        json_data['data'] = serializer.data
        print(serializer)
        return Response(json_data)

    def post(self,request,format=None):
        """
        post请求添加数据
        使用这个之后就会呈现一个post入口 下面就是我重写的方法
        """
        try:
            data = request.body
            
            data_str = data.decode()        # 将传进来的二进制数据转换成字符串
            print(data.decode())
            print(type(data))
            
            newdata = json.loads(data_str)  # 将字符串转换成json也就是我们需要的字典类型
            print(newdata,type(newdata))
            result = Student.objects.create(name=newdata['name'],describe=newdata['describe'])
            print(result)

            # 方法一 导入序列化
            # from django.core import serializers
            # serializer = serializers.serialize('json',[result])
            # print(serializer,type(serializer))
            # j_s = json.loads(serializer)
            # print(j_s,type(j_s))

            #方法二 比较后选用这个方法
            serializer = StudentsSerializer([result], many=True)
            print(serializer.data)
            json_data = {
                "message": "post_ok", 
                "errorCode": 0
            }
            json_data['data'] = serializer.data
            return Response(json_data)
        except Exception as e:
            return Response({"message": "error", "errorCode": 100})

    def delete(self, request, format=None):
        """
        定义前端的删除删除请求，当发起这个请求的时候就回去把这条数据的删除状态变为真
        """
        print(request.GET.get('id'))
        if request.GET.get('id'):
            id = request.GET.get('id')
            students = Student.objects.filter(id=id)
            
            student = students.first()# 得到需要操作的对象
            student.isDelete = True
            student.save()
            json_data = {
                "message": "delete", 
                "errorCode": 0
            }
            pg = MyPageNumberPagination()
            page_roles = pg.paginate_queryset(queryset=students, request=request, view=self)
            serializer = StudentsSerializer(instance=page_roles, many=True)
            json_data['data'] = serializer.data
        else:
            json_data = {
                "message": "error", 
                "errorCode": 1
            }
        return Response(json_data)

    def put(self, request, format=None, *args, **kwargs):
        print(request)
        print(args)
        print(kwargs)
        json_data = {"message": "put", "errorCode": 1}
        return Response(json_data)

    def patch(self, request, format=None,*args, **kwargs):
        print(request.body)
        print(args)
        print(kwargs)
        json_data = {"message": "patch", "errorCode": 1}
        return Response(json_data)

class CourseApiView(APIView):

    def get(self,request,format=None):
        print(request.user)
        courses = course.objects.all()
        json_data = {"message": "ok", "errorCode": 0}
        pg = MyPageNumberPagination()
        page_roles = pg.paginate_queryset(queryset=courses,request=request,view=self)
        print(pg.page_size)
        print(len(courses))
        import math
        print(math.ceil((len(courses)/pg.page_size)))
        # 进一取整
        page_nums = (math.ceil((len(courses)/pg.page_size)))
        serializer = CoursesSerializer(instance=page_roles,many=True)
        json_data['data'] = serializer.data

        return Response(json_data)

    def post(self, request, format=None):
        try:
            # 获取前台传来的json数据
            data = request.body
            # 将传进来的二进制数据转换成字符串
            data_str = data.decode()
            print(data.decode())
            print(type(data))
            # 将字符串转换成json也就是我们需要的字典类型
            newdata = json.loads(data_str)
            print(newdata,type(newdata))
            course_obj = course
            # 创建数据后返回的可操作对象
            # 返回需要的学生对象
            student_obj = Student.objects.filter(id=newdata['student']).filter(isDelete=False).first()
            if student_obj:
                result = course_obj.objects.create(name=newdata['name'],describe=newdata['describe'],student=student_obj)
                print(result)
                serializer = CoursesSerializer([result], many=True)
                json_data = {"message": "post_ok", "errorCode": 0}
                json_data['data'] = serializer.data
                return Response(json_data)
            else:
                json_data = {"message": "error", "errorCode": 400,'detail':'该学生已经删除或不存在'}
                return Response(json_data)
        except Exception as e:
            return Response({"message": "error", "errorCode": 100})
```

### 6、最后来配置 app 的路由
```py
from django.conf.urls import url
from newapp import views
urlpatterns = [
    url(r'students/',views.StudentsApiView.as_view()),
    url(r'courses/',views.CourseApiView.as_view()),
]
```

### 7、运行
在终端输入：python manage.py runserver 0.0.0.0:8000
这样你的 **`http://127.0.0.1:8000/students/`** 这个借口就可以实现数据的增删改查操作了

值得注意的是`http://127.0.0.1:8000/students/`这个借口同时支持分页查询
```
http://127.0.0.1:8000/students/?page=1 #查询第一页数据
http://127.0.0.1:8000/students/?page=1&page_size=10 #查询第一页数据请求每页数量为10
```



```py

```
```py

```

