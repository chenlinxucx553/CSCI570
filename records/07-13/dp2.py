__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '7/13/2020 10:26 AM'

import collections


class Solution:
    def minPathSum(self, grid):
        f = [[0] * len(grid[0]) for _ in range(len(grid))]
        f[0][0] = grid[0][0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0: continue
                if i == 0: f[i][j] = f[i][j - 1] + grid[i][j]
                if j == 0:
                    f[i][j] = f[i - 1][j] + grid[i][j]
                else:
                    f[i][j] = min(f[i][j - 1], f[i - 1][j]) + grid[i][j]
        return f


class Solution2:
    def minPathSum(self, grid):
        row = len(grid)  # 行
        col = len(grid[0])  # 列
        dp = [[0] * col for _ in range(row)]

        dp[0][0] = grid[0][0]  # 初始化首位置

        # 因为第一行和第一列属于特殊状态，需要先处理

        # 处理第一行:
        for i in range(1, row):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        # 处理第一列:
        for j in range(1, col):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        # 遍历整个数组:
        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])  # 状态转移方程
        print(dp)
        return dp[-1][-1]


if __name__ == '__main__':
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    result = Solution().minPathSum(grid=grid)
    print(result)

    result2 = Solution2().minPathSum(grid=grid)
    print(result2)