__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '7/13/2020 9:45 AM'


class Solution:
    def waysToStep(self, n: int) -> int:
        f = [0, 1, 2, 4]
        if n <= 3:
            return f[n]
        for index in range(4, n + 1):
            f.append(f[index - 3] + f[index - 2] + f[index - 1] % 1000000007)
        return f[n]


if __name__ == '__main__':
    ss = Solution().waysToStep(4)
    print(ss)
