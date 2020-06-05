__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '6/4/2020 11:03 AM'

import random

if __name__ == '__main__':
    print(int(7 / 2))
    print(33 // 2)

    arr = random.sample(range(0, 100000), 11)
    print(arr)
    mid = len(arr) // 2
    print(mid)
    print(arr[:mid])
    print(arr[mid:])
    print(arr[1:2])

    a = 3
    b = 4
    c = [a, b]
    print(c)
