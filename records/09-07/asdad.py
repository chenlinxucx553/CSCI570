__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '9/7/2020 11:52 PM'


class Solution:
    def combine(self, n: int, k: int):

        self.result = []

        def backtrace(n, k, start, subset):
            if len(subset) == k:
                self.result.append(subset[:])
                return
            for i in range(start, n + 1):
                subset.append(i)
                backtrace(n, k, i + 1, subset)
                subset.pop()

        backtrace(n, k, 1, [])
        return self.result


if __name__ == '__main__':
    Solution().combine(4, 2)
