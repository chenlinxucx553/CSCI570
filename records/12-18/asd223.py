__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/18/2020 11:28 AM'


class Solution:
    def exchange(self, nums):

        left, right = 0, len(nums) - 1
        while left < right:
            while left < len(nums) and nums[left] % 2 != 0:
                left += 1

            while right >= 0 and nums[right] % 2 == 0:
                right -= 1

            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            else:
                break

        return nums


Solution().exchange([1, 3, 5])
