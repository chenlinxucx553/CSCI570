__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/13/2020 3:55 AM'

import collections


def go_check(arr):
    # char_map = collections.defaultdict(int)
    for val in zip(*arr):
        if val[0] != val[1]:
            return False

    return True


while True:
    try:

        strs = []
        for i in range(2):
            line = sorted(list(input().strip()))
            strs.append(line)

        print(1 if go_check(strs) else 0)

    except:
        break
