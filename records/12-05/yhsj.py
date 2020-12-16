__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/5/2020 8:10 PM'


class Solution:
    def generate(self, numRows: int):
        dp = [[1] * (i + 1) for i in range(numRows)]

        index = 2
        while index < numRows:
            for i in range(1, len(dp[index]) - 1):
                dp[index][i] = dp[index - 1][i] + dp[index - 1][i - 1]

            index += 1

        return dp


res = Solution().generate(5)
print(res)
