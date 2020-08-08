__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/4/2020 9:42 AM'

# import math
#
# while True:
#     try:
#         n, m = map(int, input().split())
#
#         res = []
#         for _ in range(m):
#             res.append(n)
#             n = round(math.sqrt(n), 4)
#         print(round(sum(res), 2))
#     except:
#         break


import math

while True:
    try:
        m, n = map(int, input().split())

        res = []
        for val in range(m, n + 1):
            c_list = map(int, list(str(val)))
            c_sum = sum(list(map(lambda a: a ** 3, c_list)))
            if c_sum == val:
                res.append(c_sum)

        print(sorted(res) if res else "no")
    except:
        break
