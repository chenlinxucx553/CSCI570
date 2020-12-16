__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '12/4/2020 10:09 PM'


class Solution:
    def searchRange(self, nums, target):

        if not nums :
            return [-1, -1]

        i = 0
        j = len(nums) - 1

        if nums[0] > target or nums[-1] < target:
            return [-1, -1]

        while i <= j:
            mid = (i + j) // 2
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1

        if nums[i] != target:
            return [-1, -1]

        res = [i, ]
        while i < len(nums):
            if nums[i] == target:
                i += 1
            else:
                break

        res.append(i - 1)
        return res


nums = [1]
target = 1
res = Solution().searchRange(nums, target)
print(res)
