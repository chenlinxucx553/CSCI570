__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/24/2020 10:01 PM'


def func1():
    res = 0

    def inner_func(num):
        res = num * num

    inner_func(2)
    print(res)


func1()