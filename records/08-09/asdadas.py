__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/9/2020 10:27 PM'


class Solution:
    def minPathSum(self, grid) -> int:

        if not grid: return 0

        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]

        dp[0][0] = grid[0][0]

        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]

        return dp[-1][-1]


if __name__ == '__main__':
    grid = [[1,2,5],[3,2,1]]
    ss = Solution().minPathSum(grid)
    print(ss)
