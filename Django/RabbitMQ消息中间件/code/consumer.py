import pika


host = '127.0.0.1'
port = 5672
virtual_host = '/'
user = 'guest'
pswd = 'guest'

credentials = pika.PlainCredentials(user, pswd)     # mq 用户名和密码
connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, port=port, virtual_host=virtual_host, credentials=credentials))
channel = connection.channel()

# 申明消息队列，消息在这个队列传递，如果不存在，则创建队列
channel.queue_declare(queue='python-test', durable = False)

# 定义一个回调函数来处理消息队列中的消息，这里是打印出来
def callback(ch, method, properties, body):
    ch.basic_ack(delivery_tag = method.delivery_tag)
    print(body.decode())


channel.basic_consume('python-test', callback)  # 告诉 rabbitmq，用 callback 来接收消息
channel.start_consuming()                       # 开始接收信息，并进入阻塞状态，队列里有信息才会调用 callback 进行处理





