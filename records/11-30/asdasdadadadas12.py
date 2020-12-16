__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '11/30/2020 10:47 PM'


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # memo = {}

        # def dp(i, j):
        #     if (i, j) in memo:
        #         return memo[(i, j)]

        #     if i == -1: return j + 1
        #     if j == -1: return i + 1

        #     if word1[i] == word2[j]:
        #         memo[(i, j)] = dp(i - 1, j - 1)
        #     else:
        #         memo[(i, j)] = min(
        #             dp(i, j - 1) + 1,
        #             dp(i - 1, j) + 1,
        #             dp(i - 1, j - 1) + 1
        #         )

        #     return memo[(i, j)]

        # return dp(len(word1) - 1, len(word2) - 1)

        dp = [[0] * int(len(word1) + 1) for _ in range(len(word2)+1)]

        # 第一行
        for j in range(1, len(word1) + 1):
            dp[0][j] = dp[0][j - 1] + 1
        # 第一列
        for i in range(1, len(word2) + 1):
            dp[i][0] = dp[i - 1][0] + 1

        for i in range(1, len(word2) + 1):
            for j in range(1, len(word1) + 1):
                if word1[j - 1] == word2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
        print(dp)


Solution().minDistance("horse", 'ros')
