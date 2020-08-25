__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/19/2020 8:53 PM'


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m, n = len(word1) + 1, len(word2) + 1
        dp = [[float('inf')] * n for _ in range(m)]

        for i in range(m):
            dp[i][0] = i

        for i in range(n):
            dp[0][i] = i

        for i in range(1, m):
            for j in range(1, n):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j - 1], dp[i - 1][j]) + 1

        return dp[-1][-1]


if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"
    res = Solution().minDistance(word1, word2)
    print(res)
