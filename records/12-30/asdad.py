__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/30/2020 10:50 PM'

while True:
    n = int(input())
    lose = 0
    money = n
    for i in range(2, n):
        money = money - i
        if money > 0:
            lose += 1
        else:
            break
    print(n - 2 * lose)
