__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/20/2020 9:22 PM'

import sys

for line in sys.stdin:
    nums = line.split()
    num1, num2 = int(nums[0]), int(nums[1])

    res = str(num1 / num2)
    a, b = res.split('.')[0], res.split('.')[1]
    if len(b) == len(set(list(b))):
        if b[0] == '0':
            print(a)
        else:
            print(res)
    else:
        i, j = 0, len(b) - 1
        while j > 1:
            if b[j] == b[j - 1]:
                j -= 1
            else:
                break

        while i < j:
            if b[i] != b[i + 1]:
                i += 1
            else:
                break
        print(a + "." + b[:i] + "{" + b[i:j + 1] + "}")
