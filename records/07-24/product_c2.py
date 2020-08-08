__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '7/28/2020 11:16 PM'


def consumer():
    print("[CONSUMER] start")
    r = 'c start'
    times = 3000
    while times > 0:
        n = yield r
        if not n:
            print("n is empty")
            continue
        print("[CONSUMER] Consumer is consuming %s" % n)
        r = "200 ok"
        times -=1


def producer(c):
    # 启动generator
    start_value = c.send(None)
    print("msg from customer:", start_value)
    n = 0
    while n < 300:
        n += 1
        print("[PRODUCER] Producer is producing %d" % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    # 关闭generator
    c.close()


# 创建生成器
c = consumer()
# 传入generator
producer(c)
