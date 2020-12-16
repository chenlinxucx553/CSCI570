__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/1/2020 8:36 PM'


def show(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(res)
        return res

    return wrapper


class Solution:
    @show
    def maxSubArray(self, nums) -> int:
        dp = [0] * len(nums)
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], dp[i])
        return max(dp)


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Solution().maxSubArray(arr)
