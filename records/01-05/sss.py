__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '1/7/2021 9:28 PM'


class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        size = len(nums)
        nums[:] = nums[size - k:] + nums[:size - k]
        print(nums)


Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3)
