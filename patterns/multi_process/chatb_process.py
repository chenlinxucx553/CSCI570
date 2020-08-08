__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/4/2020 11:30 AM'

from multiprocessing import Process

lis = []


def foo(i):
    lis.append(i)
    print("This is Process ", i, " and lis is ", lis, " and lis.address is  ", id(lis))


if __name__ == '__main__':
    for i in range(5):
        p = Process(target=foo, args=(i,))
        p.start()
    print("The end of list_1:", lis)
