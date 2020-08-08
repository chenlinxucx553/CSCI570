__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/3/2020 11:31 PM'


import threading
import time


def Write():
    for i in range(30):
        print('cooking %d times'%(i+1))
        # time.sleep(1)  # 程序运行到这里休眠一秒，方便观察


def Sing():
    for i in range(300):
        print('eating %d times'%(i+1))
        # time.sleep(2)


if __name__ == '__main__':
    tr1 = threading.Thread(target=Write)  # 传入函数名
    tr2 = threading.Thread(target=Sing)
    tr1.start()
    tr2.start()