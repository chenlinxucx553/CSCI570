__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/24/2020 9:38 PM'


def func1(num):
    res = 1
    while num > 0:
        res *= num
        num -= 1

    return res


print(func1(5))


def func2(num):
    if num == 1:
        return 1
    return num * func2(num - 1)


print(func2(5))
