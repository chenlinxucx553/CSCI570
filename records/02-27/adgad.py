__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '2/26/2021 7:27 PM'

arr = [1, 3, 2, 4, 6, 100]

dp = [0] * len(arr)

dp[-1] = arr[-1]

for i in range(len(arr) - 2, -1, -1):
    if i + arr[i] < len(arr):
        dp[i] = max(arr[i] + dp[i + arr[i]], dp[i + 1])
    else:
        dp[i] = max(arr[i], dp[i + 1])

print(max(dp))
