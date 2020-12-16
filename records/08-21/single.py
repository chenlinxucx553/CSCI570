__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/20/2020 8:13 PM'

import threading


class Singleton(object):
    _lock = threading.Lock()
    _instances = None


    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if not cls :
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


def test_singleton(value: str) -> None:
    singleton = Singleton()
    print(singleton)


for _ in range(33):
    obj = Singleton()
    print(obj)

# for i in range(10):
#     process = threading.Thread(target=test_singleton, args=(i,))
#     process.start()
