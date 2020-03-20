import time

# 类装饰器
class LogTime:
    def __init__(self):
        pass

    def __call__(self, func):    # 作为外层函数
        def _inner(*args, **kwargs):
            beg = time.time()
            res = func(*args, **kwargs) # 执行函数
            print("time: {}".format(time.time()-beg))
            return res
        return _inner
    

# 调用类装饰器
@LogTime()  # 要加上括号，表示定义类实例
def func1():
    time.sleep(1)

# 测试用例
if __name__ == '__main__':
    func1()