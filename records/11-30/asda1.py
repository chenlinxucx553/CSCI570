__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '11/30/2020 9:53 PM'


def show(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(res)
        return res
    return wrapper

class Solution:
    @show
    def coinChange(self, coins, amount: int) -> int:

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]


Solution().coinChange([1, 2, 5], 11)
