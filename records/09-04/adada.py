__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '9/4/2020 4:22 PM'


class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        self.data = list(range(1, n + 1))
        self.res = []

        checked = [0] * (n + 1)

        self.backtrace(self.data, [], checked, k)
        return "".join(map(str, self.res[-1]))

    def backtrace(self, nums, temp_res, checked, k):
        if len(temp_res) == len(nums):
            self.res.append(temp_res)
            return

        if len(self.res) >= k:
            return

        for i in range(len(nums)):
            if checked[i] == 1:
                continue

            checked[i] = 1
            self.backtrace(nums, temp_res + [nums[i]], checked, k)
            checked[i] = 0


class Solution2:
    def getPermutation(self, n: int, k: int) -> str:
        import math
        tokens = [str(i) for i in range(1, n + 1)]
        res = ''
        k = k - 1
        while n > 0:
            n -= 1
            a, k = divmod(k, math.factorial(n))
            res += tokens.pop(a)
        return res


if __name__ == '__main__':
    res = Solution2().getPermutation(4, 7)
    print(res)
