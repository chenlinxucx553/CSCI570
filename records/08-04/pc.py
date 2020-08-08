__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/4/2020 10:26 AM'

import queue
import time
import  threading

msg_queue = queue.Queue(10)

def producer(index):
    i = 1
    while True:
        msg_queue.put("the {} ith cook made the {} ith item".format(index, i))
        i += 1
        # time.sleep(1)


def customer(index):
    while True:
        print("the {} ith customer eat {}".format(index, msg_queue.get()))
        # time.sleep(1)


for i in range(1, 4):
    t = threading.Thread(target=producer, args=(i,))
    t.start()


for j in range(1, 10):
    t = threading.Thread(target=customer, args=(j,))
    t.start()