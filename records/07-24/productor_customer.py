import time
import queue
import threading

q = queue.Queue(10)


def productor(i):
    while True:
        q.put("厨师 {} 做的包子！".format(i))
        time.sleep(2)


def consumer(j):
    while True:
        print("顾客 {} 吃了一个 {}".format(j, q.get()))
        time.sleep(1)


for i in range(3):
    t = threading.Thread(target=productor, args=(i,))
    t.start()

for j in range(10):
    v = threading.Thread(target=consumer, args=(j,))
    v.start()
