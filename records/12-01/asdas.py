__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/1/2020 7:57 PM'


def show(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(res)
        return res

    return wrapper


class Solution:
    @show
    def maxEnvelopes(self, envelopes) -> int:
        if not envelopes:
            return 0
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = [0] * len(envelopes)
        dp[0] = 1
        for i in range(1, len(envelopes)):
            for j in range(i):
                if envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


arr = [[5, 4], [6, 4], [6, 7], [2, 3]]
Solution().maxEnvelopes(arr)
