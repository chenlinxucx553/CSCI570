__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '2/26/2021 7:42 PM'

# arr = [1, 3, 2, 4, 6, 100]
arr = [1, 3, 2, 4, 6, 5]

dp = [-1] * len(arr)

dp[-1] = arr[-1]


def fun(arr, i):
    if i >= len(arr):
        return 0
    if dp[i] != -1:
        return dp[i]

    dp[i] = max(arr[i] + fun(arr, i + arr[i]), fun(arr, i + 1))
    return dp[i]


res = fun(arr, 0)
print(dp)
