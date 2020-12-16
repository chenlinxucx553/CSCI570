__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '11/30/2020 10:32 PM'


def show(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(res)
        return res

    return wrapper


class Solution:
    @show
    def minDistance(self, word1: str, word2: str) -> int:

        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == -1: return j + 1
            if j == -1: return i + 1

            if word1[i] == word2[j]:
                memo[(i, j)] = dp(i - 1, j - 1)
            else:
                memo[(i, j)] = min(
                    dp(i, j - 1) + 1,
                    dp(i - 1, j) + 1,
                    dp(i - 1, j - 1) + 1
                )

            return memo[(i, j)]

        return dp(len(word1) - 1, len(word2) - 1)


Solution().minDistance("horse", 'ros')
