__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/17/2020 3:31 PM'


class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if n != 0:
            nums1[m:m + n] = nums2

            def insertation_sort(arr):
                for i in range(len(arr)):
                    pre_idx = i - 1
                    current = arr[i]
                    while pre_idx >= 0 and arr[pre_idx] > current:
                        arr[pre_idx + 1] = arr[pre_idx]
                        pre_idx -= 1

                    arr[pre_idx + 1] = current
                return arr

            nums1[:] = insertation_sort(nums1[:m + n])

        if m == 0:
            nums1[:n] = nums2


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    Solution().merge(nums1, m, nums2, n)
    print(nums1)
