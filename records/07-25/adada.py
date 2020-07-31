__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '7/25/2020 3:29 PM'


class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums and k > 0:
            while k > 0:
                nums, val = nums[:-1], nums[-1]
                nums.insert(0, val)
                k -= 1

        print(nums)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    # Solution().rotate(arr, k)

    print(arr[4:5])

    import numpy as np
    ss = np.array(arr)
    print(ss[4:5])

    qw = ["flower","flow","flight"]
    for c in zip(*qw):
        print(c)