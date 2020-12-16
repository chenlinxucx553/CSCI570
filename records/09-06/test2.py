__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '9/6/2020 5:46 AM'

import math


def format(arr):
    arr = list(set(arr))
    for idx, item in enumerate(arr):
        val = str(round(item, 2))
        if len(val.split('.')[1]) == 1:
            val += '0'
        arr[idx] = val
    return "".join(arr)


while True:
    try:
        n = int(input().split()[0])
        args = list(map(int, input().split()))
        if n == 1:
            if args[1] != 0:
                print(format([-args[1] / args[0]]))
            else:
                print(0.00)
        elif n == 2:
            a, b, c = args[0], args[1], args[2]
            delta = b ** 2 - 4 * a * c
            if delta < 0:
                print("No")
                continue
            print(format([(-b + math.sqrt(delta)) / (2 * a), (-b - math.sqrt(delta)) / (2 * a)]))
        elif n == 3:
            a, b, c, d = args[0], args[1], args[2], args[3]
            prime = c / a - (b ** 2 / (3 * a ** 2))
            q = d / a + (b ** 3 / (27 * a ** 3)) - (b * c / 3 * a ** 2)



        elif n == 4:
            pass
        elif n == 5:
            pass
        else:
            pass

    except:
        break
