__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/13/2020 2:54 PM'


class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        if k <= len(nums):
            res = []
            while k:
                val = nums.pop()
                res.append(val)
                k -= 1

            for val in res:
                nums.insert(0, val)
        else:
            nums.reverse()

    def rotate2(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        from collections import deque
        ss = deque(nums)
        k %= len(nums)
        while k:
            val = ss.pop()
            ss.appendleft(val)
            k -= 1
        nums[:] = ss


if __name__ == '__main__':
    arr = [1, 2, 3]
    jk = 4
    Solution().rotate2(arr, jk)
    print(arr)
