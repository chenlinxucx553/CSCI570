__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/9/2020 10:52 PM'


class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1: return 1

        dp = [0] * (n + 1)

        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


if __name__ == '__main__':
    Solution().climbStairs(2)