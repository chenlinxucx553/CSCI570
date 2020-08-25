__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/22/2020 5:17 PM'


def show(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(res)

    return wrapper


class Solution:
    @show
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0: return False
        if n == 1: return True
        if n == 2: return True

        while n > 1:
            if n % 2 != 0:
                return False
            n //= 2

        return True


if __name__ == '__main__':
    # Solution().isPowerOfTwo(4)
    a, b = 3,3
    a /= 2
    b //= 2
    print(a)
    print(b)
