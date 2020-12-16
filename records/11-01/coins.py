__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '11/1/2020 8:54 PM'


class Solution:
    def coinChange(self, coins, amount: int) -> int:

        f = [float('inf')] * (amount + 1)
        f[0] = 0
        for j in range(0, amount + 1):
            for c in coins:
                if j < c: continue
                f[j] = min(f[j], f[j - c] + 1)
        return f[amount] if f[amount] != float('inf') else -1


res = Solution().coinChange([1, 2, 5], 11)
print(res)
