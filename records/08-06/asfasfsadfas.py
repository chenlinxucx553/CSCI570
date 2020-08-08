__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/6/2020 5:18 PM'

from collections import deque


class Solution:
    def findKthLargest(self, nums, k: int) -> int:

        if not nums: return 0
        if len(nums) == 1: return nums[0]
        res = deque(maxlen=k)
        res.append(float('-inf'))

        for val in nums:
            if val >= res[-1]:
                res.append(val)

        return res[0]


ss = Solution().findKthLargest([2, 1], 2)

arr = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30],
    [18, 21, 23, 26, 30],
    [18, 21, 23, 26, 30],
    [18, 21, 23, 26, 30]
]

print([row[3] for index, row in enumerate(arr) if index <= 3])