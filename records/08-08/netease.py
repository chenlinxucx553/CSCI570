__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/7/2020 11:41 PM'


# 凑零钱
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if (i >= coin):
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1] if (dp[-1] != float("inf")) else -1


# 最长回文子串
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        res = s[0]

        def extend(i, j, s):
            while (i >= 0 and j < len(s) and s[i] == s[j]):
                i -= 1
                j += 1
            return s[i + 1:j]

        for i in range(n - 1):
            e1 = extend(i, i, s)
            e2 = extend(i, i + 1, s)
            if max(len(e1), len(e2)) > len(res):
                res = e1 if len(e1) > len(e2) else e2
        return res