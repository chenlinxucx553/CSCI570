__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/24/2020 11:04 PM'


class Solution:
    def findSubsequences(self, nums):

        self.res = []

        def backtrace(nums, temp):
            if len(temp) >= 2 and temp not in self.res:
                self.res.append(temp)
            if not nums:
                return

            for i in range(len(nums)):
                if not temp or nums[i] >= temp[-1]:
                    backtrace(nums[i + 1:], temp + [nums[i]])

        backtrace(nums, [])

        return self.res


if __name__ == '__main__':
    arr = [4, 6, 7, 7]
    result = Solution().findSubsequences(arr)
    print(result)
