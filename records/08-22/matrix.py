__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/22/2020 3:14 PM'


def show(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(res)

    return wrapper


class Solution:
    @show
    def generateMatrix(self, n: int):

        if n <= 1: return [[n]]

        data = range(1, n ** 2 + 1)

        rows, cols = n, n
        i, j, symbol = 0, -1, 1
        size = len(data)
        index = 0

        res = [[0] * n for _ in range(n)]

        while index < size:
            for _ in range(cols):
                j += symbol
                res[i][j] = data[index]
                index += 1

            for _ in range(rows - 1):
                i += symbol
                res[i][j] = data[index]
                index += 1

            symbol *= -1
            cols -= 1
            rows -= 1

        return res


if __name__ == '__main__':
    # Solution().generateMatrix(3)
    size = 3
    k = 4
    print(k // 2)