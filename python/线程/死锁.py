"""
【 死锁 demo 】
现象：
    我是程序员 1 ， module1 开发正式开始，谁也别动我的代码
    我是程序员 2 ， module2 开发正式开始，谁也别动我的代码

    两个线程都不能给对方解锁，两个线程都跑不下去
"""
import threading
import time


# 创建互斥锁。互斥锁对资源锁定之后就一定要解锁，否则资源会一直处于锁定状态，其他线程无法修改
mutex_one = threading.Lock()    # mutex: 互斥
mutex_two = threading.Lock()


def programmer_thread1():
    mutex_one.acquire()
    print("我是程序员 1 ， module1 开发正式开始，谁也别动我的代码")
    time.sleep(2)
    mutex_two.acquire()     # 此时会堵塞，因为这个 mutex_two 已经被线程 programmer_thread2 抢先上锁了 , 等待解锁
    print("等待程序员2通知我合并代码")
    mutex_two.release()     # mutex_two 解锁
    mutex_one.release()     # mutex_one 解锁


def programmer_thread2():
    mutex_two.acquire()
    print("我是程序员 2 ， module2 开发正式开始，谁也别动我的代码")
    time.sleep(2)
    mutex_one.acquire()     # 此时会堵塞，因为这个 mutex_one 已经被线程 programmer_thread1 抢先上锁了 , 等待解锁
    print("等待程序员 1 通知我合并代码")
    mutex_one.release()     # mutex_one 解锁
    mutex_two.release()     # mutex_two 解锁


def main():
    t1 = threading.Thread(target=programmer_thread1)
    t2 = threading.Thread(target=programmer_thread2)
    t1.start()  # 启动线程
    t2.start()
    t1.join()   # 阻塞函数，等待线程结束
    t2.join()
    # 整合代码结束
    print("整合代码结束 ")


if __name__ == "__main__":
    main()