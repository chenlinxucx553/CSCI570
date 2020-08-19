__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/12/2020 10:27 AM'

import time
import threading


class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        # time.sleep(1)
        pass

    @classmethod
    def get_instance(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = Singleton(*args, **kwargs)
        return Singleton._instance

    # def __new__(cls, *args, **kwargs):
    #     if not hasattr(Singleton, "_instance"):
    #         with Singleton._instance_lock:
    #             if not hasattr(Singleton, "_instance"):
    #                 Singleton._instance = object.__new__(cls)
    #     return Singleton._instance


# def task(arg):
#     obj = Singleton.instance()
#     print(obj)
#
#
# for i in range(10):
#     t = threading.Thread(target=task, args=[i, ])
#     t.start()
# time.sleep(20)
for _ in range(33):
    obj = Singleton.get_instance()
    print(obj)
