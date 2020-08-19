__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/17/2020 5:17 PM'


# -*- coding:utf-8 -*-
class Solution:

    def Fibonacci(self, n):
        # write code here

        if n < 2:
            return n
        dp = [0] * (n + 1)

        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


if __name__ == '__main__':
    Solution().Fibonacci(0)
