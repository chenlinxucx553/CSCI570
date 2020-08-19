__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/15/2020 7:42 PM'


class Solution:
    def minOperations(self, n: int) -> int:
        avg = n

        data = [2 * i + 1 for i in range(n)]

        res = sum(list(map(lambda val: abs(val - avg), data)))

        return res / 2


if __name__ == '__main__':
    res = Solution().minOperations(3)
    print(res)
