__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/2/2020 10:49 PM'


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        row = len(word1)
        col = len(word2)
        dp = [[0] * (col + 1) for j in range(row + 1)]

        temp = 0
        for j in range(1, col + 1):
            temp += ord(word2[j - 1])
            dp[0][j] = temp

        temp = 0
        for i in range(1, row + 1):
            temp += ord(word1[i - 1])
            dp[i][0] = temp

        for i in range(1, row + 1):
            for j in range(1, col + 1):
                if word1[i - 1] != word2[j - 1]:
                    dp[i][j] = min(dp[i - 1][j] + ord(word1[i - 1]),
                                   dp[i][j - 1] + ord(word2[j - 1]))
                else:
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[-1][-1]


a = "sea"
b = "eat"
res = Solution().minDistance(a, b)
print(res)
