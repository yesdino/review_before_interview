from queue import Queue
import random
import threading
import time


# 生产者类
class Producer(threading.Thread):

    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.queue = queue

    def run(self):
        for i in range(1, 5):
            print("{} is 产出 {} to the queue!".format(self.getName(), i))
            self.queue.put(i)       # 往共享队列放数据
            time.sleep(random.randrange(10) / 5)
        print("%s finished!" % self.getName())


# 消费者类
class Consumer(threading.Thread):

    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.queue = queue

    def run(self):
        for i in range(1, 5):
            val = self.queue.get()  # 从共享队列读数据
            print("{} is 消费 {} in the queue.".format(self.getName(), val))
            time.sleep(random.randrange(10))
        print("%s finished!" % self.getName())


def main():
    queue = Queue()
    producer = Producer('生产者', queue)
    consumer = Consumer('消费者', queue)

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()
    print('All threads finished!')


if __name__ == '__main__':
    main()
