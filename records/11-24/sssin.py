from threading import Lock, Thread


class SingletonMeta(type):
    _instances = None

    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if not cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances = instance
        return cls._instances


class Singleton(metaclass=SingletonMeta):
    value: str = None

    def __init__(self, value: str) -> None:
        self.value = value

    def some_business_logic(self):
        pass


def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(singleton.value)


for i in range(10):
    process = Thread(target=test_singleton, args=(i,))
    process.start()
