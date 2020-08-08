__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/1/2020 4:10 PM'


class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        k1 = (len(nums1) + len(nums2) + 1) // 2
        k2 = (len(nums1) + len(nums2) + 2) // 2

        def helper(arr1, arr2, k):  # 本质上是找第k小的数
            if len(arr1) < len(arr2):
                arr1, arr2 = arr2, arr1  # 保持arr1比较长
            if len(arr2) == 0:
                return arr1[k - 1]  # 短数组空，直接返回
            if k == 1:
                return min(arr1[0], arr2[0])  # 找最小数，比较数组首位
            t = min(k // 2, len(arr2))  # 保证不上溢
            if arr1[t - 1] >= arr2[t - 1]:
                return helper(arr1, arr2[t:], k - t)
            else:
                return helper(arr1[t:], arr2, k - t)

        return (helper(nums1, nums2, k1) + helper(nums1, nums2, k2)) / 2


if __name__ == '__main__':
    Solution().findMedianSortedArrays()
