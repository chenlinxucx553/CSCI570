__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/21/2020 3:51 PM'


def show(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(res)

    return wrapper


class Solution:
    @show
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        all_length = len(nums1) + len(nums2)
        if all_length == 1:
            return nums1.pop(0) if nums1 else nums2.pop(0)
        target = 0
        is_even = False
        if all_length % 2 == 0:
            is_even = True
            target = all_length // 2
        else:
            target = all_length // 2 + 1

        index = target
        temp_arr = []
        while target > -1:
            if nums1 and nums2:
                temp_arr.append(nums1.pop(0) if nums1[0] < nums2[0] else nums2.pop(0))
            else:
                temp_arr.append(nums1.pop(0) if nums1 else nums2.pop(0))
            target -= 1

        if is_even:
            return (temp_arr[index] + temp_arr[index - 1]) / 2
        else:
            return temp_arr[index - 1]


if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3, 4]
    Solution().findMedianSortedArrays(nums1, nums2)
