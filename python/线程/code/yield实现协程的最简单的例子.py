import time

def task1():
    '''任务一'''
    while True:
        print("-----1------")
        time.sleep(0.1)
        yield


def task2():
    '''任务二'''
    while True:
        print("-----2------")
        time.sleep(0.1)
        yield


def main():
    '''调度函数'''
    t1 = task1()
    t2 = task2()
    while True:
        next(t1)
        next(t2)


if __name__ == "__main__":
    main()