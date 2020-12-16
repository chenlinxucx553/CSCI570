__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '11/26/2020 3:44 PM'


def use_logging(func):
    def wrapper():
        print("%s is invoking" % func.__name__)
        return func()

    return wrapper


@use_logging
def foo():
    print("func foo")


foo()
