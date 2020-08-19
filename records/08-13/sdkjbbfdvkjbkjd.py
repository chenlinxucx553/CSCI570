__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/13/2020 4:24 PM'


class Solution:
    def twoSum(self, nums, target: int):

        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # nums.sort()
        for i, val in enumerate(nums):
            temp = target - val
            left, right = i, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == temp:
                    return [i, mid]
                elif nums[mid] < temp:
                    left = mid + 1
                else:
                    right = mid - 1


if __name__ == '__main__':
    arr = [3, 2, 4]
    Solution().twoSum(arr, 6)
