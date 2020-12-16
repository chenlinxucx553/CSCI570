__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/1/2020 11:13 PM'


def show(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(res)
        return res

    return wrapper


class Solution:
    @show
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for k in range(n):
            dp[k][k] = 1

        for i in range(n):
            for j in range(i - 1, -1, -1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i - 1][j + 1] + 2
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j + 1])

        return dp[n - 1][0]


text1 = "bbbab"
Solution().longestPalindromeSubseq(text1)
