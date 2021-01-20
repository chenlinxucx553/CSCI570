__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/31/2020 12:02 PM'


def count_steps(total):
    dp = [1] * total

    for i in range(2, total):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[-1]


n = int(input())

for _ in range(n):
    total = int(input())
    print(count_steps(total))
