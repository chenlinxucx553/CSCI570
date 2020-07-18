__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '7/17/2020 4:13 PM'


class Solution:
    def numTrees(self, n: int) -> int:
        memo = [0] * (n + 1)
        memo[0] = memo[1] = 1
        return self.helper(memo, n)

    def helper(self, memo, n):
        if memo[n] != 0:
            return memo[n]
        for i in range(n):
            memo[n] += self.helper(memo, i) * self.helper(memo, n - i - 1)

        return memo[n]


if __name__ == '__main__':
    res = Solution().numTrees(3)
    print(res)
