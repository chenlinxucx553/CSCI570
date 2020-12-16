__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '9/5/2020 4:06 AM'


class Solution:
    def getHouses(self, t, xa):
        # write code here

        arr = []
        for i in range(0, len(xa), 2):
            left = xa[i] - xa[i + 1] // 2
            right = xa[i] + xa[i + 1] // 2
            arr.append((left, right))

        arr.sort(key=lambda item: item[1])

        dp = [1] * t
        ans = 1
        for i in range(t):
            for j in range(i - 1, -1, -1):
                if arr[i][0] >= arr[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    break
            dp[i] = max(dp[i], dp[i - 1])
            ans = max(ans, dp[i])
        return 2 * ans


if __name__ == '__main__':
    res = Solution().getHouses(2, [-1, 4, 5, 2])
    print(res)
