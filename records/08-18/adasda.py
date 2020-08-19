__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/18/2020 3:14 PM'


class Solution:
    def maxSubArray(self, nums) -> int:
        dp = [[float('-inf')] * len(nums) for _ in range(len(nums))]

        ans = float('-inf')
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                dp[i][j] = max(nums[j], dp[i][j - 1] + nums[j])
                ans = max(ans, dp[i][j])

        return ans

    def maxSubArray2(self, nums) -> int:
        dp = [float('-inf')] * len(nums)
        dp[0] = nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
            ans = max(ans, dp[i])

        return ans


if __name__ == '__main__':
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    # res = Solution().maxSubArray(arr)
    # print(res)
    print(arr[:1])
