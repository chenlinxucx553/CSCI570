__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/18/2020 12:09 PM'


class Solution:
    def spiralOrder(self, matrix):

        if matrix:

            if len(matrix) == 1:
                return matrix[0]

            x, y = 0, -1
            rows, cols = len(matrix), len(matrix[0])
            flag = 1
            res = []
            while rows > 0 and cols > 0:
                for _ in range(cols):
                    y += flag
                    res.append(matrix[x][y])

                for _ in range(rows - 1):
                    x += flag
                    res.append(matrix[x][y])

                rows -= 1
                cols -= 1
                flag *= -1
            return res

        return []


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
res = Solution().spiralOrder(matrix)
print(res)
