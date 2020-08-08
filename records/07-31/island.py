__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '7/31/2020 5:33 PM'


class Solution:
    def numIslands(self, grid) -> int:
        if not grid: return 0
        ans = 0

        extend_grid = [['0'] * len(grid[0])] + grid + [['0'] * len(grid[0])]
        for i in range(len(extend_grid)):
            extend_grid[i] = ['0'] + extend_grid[i] + ['0']

        def fill(x, y):
            if extend_grid[x][y] == '0': return
            extend_grid[x][y] = '0'
            fill(x - 1, y)
            fill(x, y - 1)
            fill(x, y + 1)
            fill(x + 1, y)

        for i in range(1, len(grid) + 1):
            for j in range(1, len(grid[0]) + 1):
                if extend_grid[i][j] == '1':
                    ans += 1
                    fill(i, j)

        return ans


if __name__ == '__main__':
    arr = [["1"], ["1"]]
    print(Solution().numIslands(arr))
    print((5 + 6) // 2)
