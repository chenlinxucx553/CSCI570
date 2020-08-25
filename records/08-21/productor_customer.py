__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '7/24/2020 10:29 PM'

import time
import queue
import threading

q = queue.Queue(10)  # 生成一个队列，用来保存“包子”，最大数量为10


def productor(i):
    # 厨师不停地每2秒做一个包子
    while True:
        q.put("厨师 %s 做的包子！" % i)
        time.sleep(2)


def consumer(j):
    # 顾客不停地每秒吃一个包子
    while True:
        print("顾客 %s 吃了一个 %s" % (j, q.get()))
        time.sleep(1)


# 实例化了3个生产者（厨师）
for i in range(3):
    t = threading.Thread(target=productor, args=(i,))
    t.start()
# 实例化了10个消费者（顾客）
for j in range(10):
    v = threading.Thread(target=consumer, args=(j,))
    v.start()
