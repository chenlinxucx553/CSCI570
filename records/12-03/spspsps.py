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

        dp = [[False] * (half_sum + 1) for _ in range(len(nums))]

        for i in range(len(nums)):
            dp[i][0] = True

        for i in range(1, len(nums)):
            for j in range(half_sum + 1):
                if j < nums[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

        return dp[-1][-1]


arr = [1, 5, 11, 5]
res = Solution().canPartition(arr)
print(res)
