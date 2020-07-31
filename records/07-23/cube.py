__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '7/23/2020 10:08 PM'


class Solution:
    def maximalSquare(self, matrix) -> int:
        if not matrix: return 0
        candidate = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    candidate.append((int(i), int(j)))

        max_area = 1
        for x, y in candidate:
            temp = 1
            while x < len(matrix) and y < len(matrix[0]):
                if (x + 1, y + 1) in candidate \
                        and (x + 1, y) in candidate \
                        and (x, y + 1) in candidate:
                    temp += 1
                    max_area = max(max_area, temp * temp)
                    x += 1
                    y += 1
                else:
                    break

        return max_area


class Solution2:
    def maximalSquare(self, matrix) -> int:
        res = 0
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1 if matrix[i - 1][j - 1] == "1" else 0
                res = max(res, dp[i][j])
        return res ** 2



if __name__ == '__main__':
    arr = [["1", "1", "1", "1", "0"],
           ["1", "1", "1", "1", "0"],
           ["1", "1", "1", "1", "1"],
           ["1", "1", "1", "1", "1"],
           ["0", "0", "1", "1", "1"]]

    Solution().maximalSquare(arr)
