__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/10/2020 4:42 PM'


class Solution:
    def coinChange(self, coins, amount: int) -> int:

        m = len(coins)

        dp = [[float('inf') for _ in range(m + 1)] for _ in range(amount + 1)]

        for j in range(m + 1):
            dp[0][j] = 0

        for i in range(1, amount + 1):
            for j in range(1, m + 1):
                coin = coins[j - 1]
                if i >= coin:
                    dp[i][j] = min(dp[i - coin][j] + 1, dp[i][j - 1])
                else:
                    dp[i][j] = dp[i][j - 1]

        return -1 if dp[-1][-1] == float('inf') else dp[-1][-1]


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    ss = Solution().coinChange(coins, amount)
    print(ss)
