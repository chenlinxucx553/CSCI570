__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '9/4/2020 4:04 PM'


class Solution:
    def permuatation(self, nums):
        self.res = []
        checked = [0] * len(nums)

        self.backtrace(nums, [], checked, 3)
        print(self.res)
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


if __name__ == '__main__':
    arr = [1, 2, 3]
    res = Solution().permuatation(arr)
    print(res)
