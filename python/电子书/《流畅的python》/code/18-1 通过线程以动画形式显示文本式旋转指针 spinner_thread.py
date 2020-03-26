""" 通过线程以动画形式显示文本式旋转指针 """

import threading
import itertools
import time
import sys


class Signal:                           # ➊ 这个类定义一个简单的可变对象；其中有个 go 属性，用于从外部控制线程。
    go = True


def spin(msg, signal):                  # ➋ 这个函数会在单独的线程中运行。signal 参数是前面定义的Signal 类的实例。
    """ 以动画形式显示文本式旋转指针 """
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'): # ➌ 这其实是个无限循环，因为 itertools.cycle 函数会从指定的序列中反复不断地生成元素。
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))     # ➍ 这是显示文本式动画的诀窍所在：使用退格符（\x08）把光标移回来。
        time.sleep(.1)
        if not signal.go:               # ➎ 如果go 属性的值不是True 了，那就退出循环。
            break
        write(' ' * len(status) + '\x08' * len(status)) # ➏ 使用空格清除状态消息，把光标移回开头。


def slow_function():                    # ➐ 假设这是耗时的计算。
    # 假装等待I/O一段时间
    time.sleep(3)                       # ➑ 调用sleep 函数会阻塞主线程，不过一定要这么做，以便释放GIL，创建从属线程。
    return 42


def supervisor():                       # ➒ 这个函数设置从属线程，显示线程对象，运行耗时的计算，最后杀死线程。
    signal = Signal()
    spinner = threading.Thread(target=spin, args=('thinking!', signal))
    print('spinner object:', spinner)   # ➓ 显示从属线程对象。输出类似于<Thread(Thread-1, initial)>。
    spinner.start()                     # 11 启动从属线程。
    result = slow_function()            # 12 运行slow_function 函数，阻塞主线程。同时，从属线程以动画形式显示旋转指针。
    signal.go = False                   # 13 改变signal 的状态；这会终止spin 函数中的那个for 循环。
    spinner.join()                      # 14 等待spinner 线程结束。
    return result


def main():
    result = supervisor()               # 15 运行 supervisor 函数。
    print('Answer:', result)


if __name__ == '__main__':
    main()