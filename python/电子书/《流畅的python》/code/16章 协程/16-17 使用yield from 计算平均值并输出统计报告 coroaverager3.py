from collections import namedtuple

Result = namedtuple('Result', 'count average')

def averager():             # ➊ 
    """ 子生成器 """
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield        # ➋ main 函数中的客户代码发送的各个值绑定到这里的 term 变量上。
        print("yield received : {}".format(term))
        if term is None:    # ➌ 至关重要的终止条件。如果不这么做，使用 yield from 调用这个协程的生成器会永远阻塞。
            break           # 当前的 averager 实例终止
        total += term
        count += 1
        average = total/count
    return Result(count, average)   # ➍ 返回的Result 会成为grouper 函数中yield from 表达式的值。


def grouper(results, key):          # ➎ 
    """ 委派生成器 相当于管道"""
    while True:                     # ➏ 这个循环每次迭代时会新建一个averager 实例；每个实例都是作为协程使用的生成器对象。
        # yield from 的意义：
        # “ 把迭代器当作生成器使用，相当于把子生成器(averager)的定义体内联在 yield from 表达式中。
        # 此外，子生成器(averager) 可以执行 return 语句返回一个值，而返回的值会成为 yield from 表达式的接收值。
        results[key] = yield from averager()    # ➐ for i in averager(): yield i。注意这里 results[key] 接收的是 averager 生成器全部迭代完了之后的 return 值
        # print("results[key] : {}".format(results[key]))
        """
        grouper 发送的每个值都会经由 yield from 处理， 通过管道传给 averager 实例。
        grouper 会在 yield from 表达式处暂停，等待 averager 实例处理客户端发来的值。
        外层 group.send(None) 使 averager 实例运行完毕后，返回的值绑定到 results[key] 上。
        继续下一个 for 循环创建下一个 averager 实例，等待外界 send value
        """

# -----------------------------------------------------------------------------------
data = {
    # 因为想看清楚执行过程所以只留了一组
    'girls;kg': [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
    # 'girls;m': [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
    # 'boys;kg': [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
    # 'boys;m': [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
}

def main(data):                         # ➑ “调用方”。这是驱动一切的函数。
    """ 客户端代码，即调用方 """
    results = {}                        # 用于收集结果
    for key, values in data.items():
        group = grouper(results, key)   # ➒ group 是调用 grouper 函数得到的生成器对象实例，作为协程使用。
        next(group)                     # ➓ 预激 此时进入 while True 循环，调用子生成器 averager 后，在 yield from 表达式处暂停
        for value in values:
            group.send(value)           # 传入的值最终到达averager 函数中 term = yield 那一行
        group.send(None)                # 重要！把 None 传入grouper，导致当前的 averager 实例终止，也让 grouper 继续运行，再创建一个 averager 实例，处理下一组值。
    # print(results) # 如果要调试，去掉注释

    # 输出报告
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(result.count, group, result.average, unit))


if __name__ == '__main__':
    main(data)  
    # 10 girls averaging 42.04kg