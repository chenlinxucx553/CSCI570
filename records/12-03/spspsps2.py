__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/3/2020 10:44 PM'


class Solution:
    def canPartition(self, nums) -> bool:

        if not nums or len(nums) <= 1:
            return False

        arr_sum = sum(nums)
        if arr_sum % 2 != 0:
            return False

        half_sum = int(arr_sum / 2)
        length = len(nums)

        dp = [[False] * (half_sum + 1) for _ in range(length + 1)]

        for i in range(length + 1):
            dp[i][0] = True

        for i in range(1, length + 1):
            for j in range(1, half_sum + 1):
                if j < nums[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

        return dp[length][half_sum]


arr = [1, 5, 11, 5]
res = Solution().canPartition(arr)
print(res)
