def consumer():             # 消费者 生成器
    ret = ''                # ret: 传递给外界的结果
    while True:             # while True 表此生成器在遍历使用时可以循环无限次
        n = yield ret       # n: 接收调用者传递的参数 ret: 由上一层循环得到的字符串 '200 OK'
        if not n:
            return          # return 表不继续往下执行 print 不是返回值出去的意思
        print('[消费者] Consuming %s...' % n)  # 【消费】
        ret = '200 OK'


def produce(c):             # 生产者
    '''边生产边消费'''
    c.send(None)            # 启动 consumer 消费者生成器
    n = 0
    while n < 5:
        n = n + 1           # 【生产】
        print('[生产者] Producing %s...' % n)
        ret = c.send(n)     # 【边生产边消费】consumer 生成器接收数据 返回处理后的值
        print('[生产者] Consumer return: %s' % ret)
        print('----------------------------')
    c.close()               # 关闭 consumer 生成器


def main():
    c = consumer()  # 生成器
    produce(c)


if __name__ == "__main__":
    main()
