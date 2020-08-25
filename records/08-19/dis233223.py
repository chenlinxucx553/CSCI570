__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/19/2020 5:08 PM'


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        ans = 0

        while x or y:
            if x & 1 != y & 1:
                ans += 1

            x >>= 1
            y >>= 1

        return ans


if __name__ == '__main__':
    Solution().hammingDistance(1, 4)
