__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '11/24/2020 10:09 PM'

nums = [4,10,4,3,8,9]

i = 0
j = 0

dp = [[0] * len(nums) for _ in range(len(nums))]

for k in range(len(dp)):
    dp[k][k] = 1

max_val = 0
for j in range(len(nums)):
    for i in range(j + 1, len(nums)):
        if nums[i] > nums[j]:
            if nums[i] > nums[i - 1]:
                dp[j][i] = dp[j][i - 1] + 1
            else:
                dp[j][i] = dp[j][i - 1]
        else:
            dp[j][i] = dp[j][i - 1]
    max_val = max(max_val, dp[j][i])

print(max_val)
