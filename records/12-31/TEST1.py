__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/31/2020 4:42 PM'

num = int(input())
res = 0
for _ in range(num):
    vals = list(map(int, input().split()))
    a, b = vals[0], vals[1]
    res += min(a, b)

print(res)
