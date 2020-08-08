__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '7/30/2020 11:34 PM'


def times(n):
    return 0.5 * (n - 1) * n


if __name__ == '__main__':
    n = int(input().split()[0])
    if n % 2 == 0:
        print(2 * times(n / 2))
    else:
        print(times((n / 2) + 1) + times(n / 2))
