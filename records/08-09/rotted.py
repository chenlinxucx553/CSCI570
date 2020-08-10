__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/9/2020 4:58 PM'


class Solution:
    def orangesRotting(self, grid) -> int:

        if not grid or not grid[0]: return -1
        m = len(grid)
        n = len(grid[0])

        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def is_all_rotted(matrix):
            for row in matrix:
                if not all(map(lambda x: x == 0 or x >= 2, row)):
                    return False

            return True

        if is_all_rotted(grid):
            return 0

        import copy
        times = 0
        while True:
            next_grid = copy.deepcopy(grid)
            for i in range(m):
                for j in range(n):
                    if grid[i][j] >= 2:
                        for x, y in direction:
                            temp_x = i + x
                            temp_y = j + y
                            if 0 <= temp_x < m and 0 <= temp_y < n and next_grid[temp_x][temp_y] != 0:
                                next_grid[temp_x][temp_y] += 1

            grid = next_grid

            times += 1
            if is_all_rotted(grid):
                return times
            if times > m * n:
                return -1


if __name__ == '__main__':
    arr = [[2,1,1],[1,1,0],[0,1,1]]
    # print(is_all_rotted(arr))
    ss = Solution().orangesRotting(arr)
    print(ss)
